"""
The main class for scraping
"""
from bs4 import BeautifulSoup
import requests
import scraper.config.config as cfg
from scraper.models.response import ScraperResult
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# from scraper.errors import InvalidWebsite


def price_to_float(price: str) -> float:
    return float(price.replace("$", ""))


class Scraper:
    """
    The base scraper for scraping the web
    """

    def __init__(self, cfg: cfg.Config) -> None:
        self.cfg = cfg

    def __str__(self) -> str:
        return f"{self.cfg.product} scraper"

    def scrape(self) -> None:
        """
        Loops through the sites in config and scrapes.
        Returns a list of ScraperResults
        """

        scrape_results = []
        for site in self.cfg.sites:
            for url in site.prepare_urls():

                resp = requests.get(url)
                if resp.status_code != 200:
                    return

                html = resp.text
                soup = BeautifulSoup(html, "html.parser")

                # CanaKit website
                so = "Sold Out"
                if site.name == "CanaKit":

                    tbl = soup.find(
                        "table", class_="pdtHeadTable"
                    )  # Table with information
                    rows = tbl.find_all("tr")
                    for row in rows:
                        product = row.findChild("b").text  # product name
                        price = price_to_float(
                            row.findChild("span", class_="priceListPrice").text
                        )  # price
                        sold_out = row.findChild("div", id="ProductAddToCartDiv")
                        sold_out_index = sold_out.text.find(so)
                        link_to_buy = ""
                        if sold_out_index == -1:
                            link_to_buy = f'https://www.canakit.com{sold_out.findChild("a")["href"]}'
                        end_index = sold_out_index + len(so)
                        in_stock = sold_out.text[sold_out_index:end_index] != "Sold Out"

                        sr = ScraperResult(
                            site=site.name,
                            product=product,
                            in_stock=in_stock,
                            price=price,
                            purchase_url=link_to_buy,
                        )
                        scrape_results.append(sr)

                # Pishop
                elif site.name == "PiShop":
                    product = soup.find("h1", class_="productView-title").text
                    price = price_to_float(
                        soup.find("span", class_="price price--withoutTax").text
                    )
                    in_stock = (
                        soup.find("input", id="form-action-addToCart")["value"]
                        != "Out of stock"
                    )
                    link_to_buy = ""
                    if in_stock:
                        # TODO: find example of when in stock
                        link_to_buy = url

                    sr = ScraperResult(
                        site=site.name,
                        product=product,
                        in_stock=in_stock,
                        price=price,
                        purchase_url=link_to_buy,
                    )
                    scrape_results.append(sr)

                # Vilros
                elif site.name == "Vilros":
                    product = soup.find("h1", class_="product-detail__title").text
                    price = price_to_float(soup.find("span", class_="theme-money").text)
                    payment_tag = soup.find("div", class_="payment-buttons")
                    in_stock = payment_tag.findChild("span").text.strip() != "Sold Out"
                    link_to_buy = ""
                    if in_stock:
                        link_to_buy = url

                    sr = ScraperResult(
                        site=site.name,
                        product=product,
                        in_stock=in_stock,
                        price=price,
                        purchase_url=link_to_buy,
                    )

                    scrape_results.append(sr)

        results = [result.to_dict() for result in scrape_results]
        engine = create_engine(cfg.DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add_all(scrape_results)
        session.commit()
        session.close()

        return results

        # raise InvalidWebsite("invalid website provided for scraping")

    def save_results(self) -> None:
        """
        TODO: Build save results functionality
        """
        raise NotImplementedError
