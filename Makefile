VENV := .venv
PYTHON := $(VENV)/bin/python

.PHONY: setup serve build clean

setup: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt

serve: setup
	$(PYTHON) -m mkdocs serve

build: setup
	$(PYTHON) -m mkdocs build

clean:
	rm -rf $(VENV) site
