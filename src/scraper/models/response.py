from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Float, String, DateTime, Boolean
from typing import Any, Dict
import uuid


Base = declarative_base()


class ScraperResult(Base):
    """
    Result of scrape
    Meant to easily hold the results of the webscraping function
    """

    __tablename__ = "scraper_results"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    site = Column(String(30))
    product = Column(String(60))
    in_stock = Column(Boolean)
    price = Column(Float)
    purchase_url = Column(String(120))
    date = Column(DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<ScraperResult(site={self.site}, product={self.product}, in_stock={self.in_stock}, price={self.price})>"

    def to_dict(self) -> Dict[str, Any]:
        d = {}
        d["site"] = self.site
        d["product"] = self.product
        d["in_stock"] = self.in_stock
        d["price"] = self.price
        d["purchase_url"] = self.purchase_url

        return d
