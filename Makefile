build:
	docker-compose build --no-cache

import:
	docker-compose run --rm api bash -c "python start.py $(url)"

export:
		docker-compose run -v ${PWD}:/data --rm api python export.py
		cat app/application.csv > $(path)

down:
	docker-compose down

up:
	docker-compose up

test: ## Run all tests (pytest).
	@echo "--> Testing on Docker."
	docker-compose run --rm test py.test $(path) -s --cov-report term --cov-report html
