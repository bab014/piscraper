"""
The main class for scraping
"""
from scraper import Config, ScraperResult
from scraper.errors import InvalidWebsite


class Scraper:
    """
    The base scraper for scraping the web
    """

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg

    def scrape(self) -> ScraperResult:
        """
        TODO: Build the scrape functionality
        """
        raise InvalidWebsite("invalid website provided for scraping")

    def save_results(self) -> None:
        """
        TODO: Build save results functionality
        """
        raise NotImplementedError
