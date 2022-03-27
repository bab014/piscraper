from scraper import Config, create_config


def test_create_config():
    cfg = create_config("/home/bab14/develop/python/scraper/urls.yaml")
    assert isinstance(cfg, Config)
