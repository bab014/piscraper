"""
Contains the config class for storing a config object
"""
from dataclasses import dataclass
import os
from typing import List
import yaml

PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
PGPORT = os.getenv("PGPORT")
PGHOST = os.getenv("PGHOST")
PGDATABASE = os.getenv("PGDATABASE")
DATABASE_URI = (
    f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"
)


# class ScraperResult:
#     """
#     Result of scrape
#     Meant to easily hold the results of the webscraping function
#     """

#     id: uuid.UUID
#     site: str
#     product: str
#     in_stock: bool
#     price: float
#     purchase_url: str
#     date: datetime

#     def to_dict(self) -> Dict[str, Any]:
#         d = {}
#         d["id"] = str(self.id)
#         d["site"] = self.site
#         d["product"] = self.product
#         d["in_stock"] = self.in_stock
#         d["price"] = self.price
#         d["purchase_url"] = self.purchase_url
#         d["date"] = self.date.strftime("%Y-%m-%d")

#         return d


@dataclass
class Site:
    """
    A site defined in a yaml config file
    """

    name: str
    urls: List[str]
    models: List[int]

    def prepare_urls(self) -> List[str]:
        """
        Prepares the urls for usage by request
        """
        urls = []
        if self.name == "Vilros":
            for model in self.models:
                urls.append(self.urls[0].replace("REPLACE_ME", str(model)))
            urls.append(self.urls[1])
            return urls
        else:
            for model in self.models:
                urls.append(self.urls[0].replace("REPLACE_ME", str(model)))
            return urls


@dataclass
class Config:
    """
    Config Dataclass for storing
    the configuration
    """

    product: str
    sites: List[Site]


def create_config(yml: str) -> Config:
    """
    Takes in a yaml file and returns a Config object
    """
    try:
        with open(yml, "r") as f:
            raw_yaml = f.read()
            yaml_obj = yaml.safe_load(raw_yaml)
    except Exception as e:
        print("Error loading the config file:", e)
        return

    sites = [Site(x["name"], x["urls"], x["models"]) for x in yaml_obj["sites"]]
    config = Config(product=yaml_obj["product"], sites=sites)

    return config
