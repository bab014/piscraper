"""
Initial module for scraping
"""
from bs4 import BeautifulSoup
import requests

list_of_models = [1, 2, 4, 8]
urls = [
    (
        "canakit",
        "https://www.canakit.com/raspberry-pi-4-REPLACE_MEgb.html",
        list_of_models,
    ),
    (
        "pishop",
        "https://www.pishop.us/product/raspberry-pi-4-model-b-REPLACE_MEgb/?src=raspberrypi",
        list_of_models,
    ),
    (
        "vilros",
        "https://vilros.com/products/raspberry-pi-4-model-b-REPLACE_MEgb-ram?src=raspberrypi",
        list_of_models,
    ),
]
# url = 'https://www.pishop.us/product/raspberry-pi-4-model-b-8gb/?src=raspberrypi'


def main():
    """
    The main function of the scrape script
    mainly using for testing purposes
    """
    print("Scraping pishop.us")

    for model in list_of_models:

        response = requests.get(
            url=f"https://www.pishop.us/product/raspberry-pi-4-model-b-{str(model)}gb/?src=raspberrypi"
        )

        soup = BeautifulSoup(response.text, "html.parser")

        print("GB:", model)
        print(soup.find("span", class_="price price--withoutTax").text)
        print(
            soup.find("input", class_="button button--primary button--addtocart")[
                "value"
            ]
        )
        print("--------------------------")


if __name__ == "__main__":
    main()
