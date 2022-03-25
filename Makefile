.PHONY: tree script

tree:
	tree -I .venv

script:
	python src/scrape.py
