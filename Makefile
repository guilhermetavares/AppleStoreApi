build:
	docker-compose build --no-cache

load:
	docker-compose run --rm api bash -c "cd /app && python start.py /path/to/data.csv"

down:
	docker-compose down

up:
	docker-compose up

test: ## Run all tests (pytest).
	@echo "--> Testing on Docker."
	docker-compose run --rm test py.test $(path) -s --cov-report term --cov-report html
