PYTHON?=python3
PYTHONPATH?=./
SOURCE_DIR=./refinery
TESTS_DIR=./tests
BIN_DIR=./bin
TESTS_ARGS=-m pytest $(TESTS_DIR) -v
COVERAGE=coverage
COVERAGE_HTML_REPORT_DIR?=./htmlcov/
PEP8=pep8

all: help

help:
	@echo "clean - remove artifacts"
	@echo "test - run tests"
	@echo "coverage - run tests with code coverage"
	@echo "htmlcoverage - run tests with code coverage and generate html report"
	@echo "check - check code style"

clean: clean-pyc clean-test

clean-pyc:
	@find . -name '*.py[cod]' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*$py.class' -exec rm -rf {} +

clean-test:
	@rm -rf $(COVERAGE_HTML_REPORT_DIR)

deploy: test
	@echo "Push"
	git push
	@echo "Deploy"
	@./bin/deploy.sh

test: clean
	@CONFIG_PATH=$(TEST_CONFIG_PATH) PYTHONPATH=$(PYTHONPATH) $(PYTHON) $(TESTS_ARGS)

coverage: clean
	@CONFIG_PATH=$(TEST_CONFIG_PATH) \
	PYTHONPATH=$(PYTHONPATH) $(COVERAGE) run --branch \
	                --source=$(SOURCE_DIR) \
	                $(TESTS_ARGS)

htmlcoverage: coverage
	$(COVERAGE) html

check: pep8

pep8:
	$(PEP8) $(SOURCE_DIR) $(TESTS_DIR) $(BIN_DIR)
