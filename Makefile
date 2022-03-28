.PHONY: tree tests

tree:
	@tree -I .venv

tests:
	@pytest
