.PHONY: tree tests

tree:
	@tree -I ".venv, *.egg-info"

tests:
	@pytest -v

