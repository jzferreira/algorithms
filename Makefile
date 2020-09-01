.PHONY: typehint test lint checklist

typehint:
	@mypy algorithms/ tests/
 
test:
	@pytest tests/
 
lint:
	@pylint algorithms/ tests/
 
checklist: lint typehint test