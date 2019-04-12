.PHONY: clean install tests all

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf dist
	rm -rf build
	rm -rf .tox
	rm -rf *egg-info
	rm -rf *coverage

install:
	pip install -r requirements/all.txt

tests:
	coverage run --source='./bdd' runtests.py
	coverage report

all: clean install tests
