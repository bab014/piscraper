"""
Contains the config class for storing a config object
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List
import yaml


@dataclass
class ScraperResult:
    """
    Result of scrape
    Meant to easily hold the rsults of the webscraping function
    """

    site: str
    product: str
    in_stock: bool
    price: float
    purchase_url: str
    date: datetime


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
