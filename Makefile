
default: develop

.PHONY: build
build:
	docker-compose build

.PHONY: develop
develop: build
	docker-compose up -d --remove-orphans

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: stop
stop:
	docker-compose kill -s SIGINT
