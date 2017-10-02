SOURCE_DIR=./refinery
TESTS_DIR=./tests
COVERAGE_HTML_REPORT_DIR?=./htmlcov/

all: help

help:
	@echo "clean - remove artifacts"
	@echo "test - run tests"
	@echo "coverage - run tests with code coverage"
	@echo "htmlcoverage - run tests with code coverage and generate html report"
	@echo "check - check code style"

clean:
	@find . -name '*.py[cod]' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*$py.class' -exec rm -rf {} +
	@rm -rf $(COVERAGE_HTML_REPORT_DIR)

test: clean
	@py.test -q

coverage: clean
	@py.test -q --cov=$(SOURCE_DIR)

htmlcoverage:
	@py.test -q --cov=$(SOURCE_DIR) --cov-report=html && google-chrome ./htmlcov/index.html

check: pep8

pep8:
	@pep8 $(SOURCE_DIR) $(TESTS_DIR)

docker-build:
	@docker build -t data-refinery .

docker-test: docker-build
	@docker run data-refinery:test
