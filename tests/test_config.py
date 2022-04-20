import scraper
import scraper.models.response as models
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
import pytest


@pytest.fixture
def cfg() -> scraper.Config:
    return scraper.create_config("/home/bab14/develop/python/scraper/urls.yaml")


@pytest.fixture
def engine() -> Engine:
    return create_engine(scraper.DATABASE_URI)


def test_config_type(cfg: scraper.Config) -> None:
    assert isinstance(cfg, scraper.Config)


def test_config_sites_len(cfg: scraper.Config) -> None:
    assert len(cfg.sites) == 3


def test_connection(engine: Engine) -> None:
    assert models.Base.metadata.create_all(engine) is None


def test_insert(engine: Engine) -> None:
    sr = models.ScraperResult(
        site="test_site",
        product="test_product",
        in_stock=True,
        price=39.99,
        purchase_url="test.url",
    )

    response = None
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(sr)
    response = session.commit()
    session.close()

    assert response is None

