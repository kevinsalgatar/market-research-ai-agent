# Makefile for Market Research AI Agent

.PHONY: install test run docker-build docker-run clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/

run:
	python main.py

docker-build:
	docker build -t market-research-agent .

docker-run:
	docker run -v $(PWD)/reports:/app/reports --env-file .env market-research-agent

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache
	rm -rf reports/*
