from scraper import Config, create_config
import pytest


@pytest.fixture
def cfg() -> Config:
    return create_config("/home/bab14/develop/python/scraper/urls.yaml")


def test_config_type(cfg: Config) -> None:
    assert isinstance(cfg, Config)


def test_config_sites_len(cfg: Config) -> None:
    assert len(cfg.sites) == 3
