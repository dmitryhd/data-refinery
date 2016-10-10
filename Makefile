PYTHON?=python3
PYTHONPATH?=./
SOURCE_DIR=./refinery
TESTS_DIR=./tests
TESTS_ARGS=-m pytest $(TESTS_DIR) -v
COVERAGE=coverage
COVERAGE_HTML_REPORT_DIR?=./htmlcov/
PEP8=pep8

clean: clean-pyc clean-test

clean-pyc:
	@find . -name '*.py[cod]' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*$py.class' -exec rm -rf {} +

clean-test:
	@rm -rf $(COVERAGE_HTML_REPORT_DIR)

test: clean
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) $(TESTS_ARGS)

coverage: clean
	py.test --cov=refinery

htmlcoverage: clean
	py.test --cov=refinery --cov-report=html

pep8:
	@$(PEP8) $(SOURCE_DIR) $(TESTS_DIR)
