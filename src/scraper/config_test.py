from datetime import datetime
from scraper.config import ScraperResult


def main():

    # pishop = config.Site('Pishop', ['https://www.pishop.us/product/raspberry-pi-4-model-b-REPLACE_MEgb/?src=raspberrypi'], [2,4,8])

    # cfg = config.Config(product='Raspi', sites=[pishop])

    # print(cfg)

    # cfg = config.create_config('scraper/config/urls.yaml')

    # print(cfg.sites[2].prepare_urls())

    res = ScraperResult(
        date=datetime(2022, 3, 25),
        site="PiShop",
        product="Raspi 8GB",
        in_stock=False,
        price=75.99,
        purchase_url="https://www.pishop.us/product/raspberry-pi-4-model-b-REPLACE_MEgb/?src=raspberrypi",
    )

    print(res.product)

    print(ScraperResult.__doc__)


if __name__ == "__main__":
    main()
