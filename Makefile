.PHONY: tree script config

tree:
	tree -I .venv

script:
	@python scraper/scrape.py

config:
	@python src/scraper/config_test.py
