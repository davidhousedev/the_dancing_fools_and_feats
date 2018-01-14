
default: develop

.PHONY: build
build:
	docker build -f Dockerfile-gulp -t dev_gulp .

.PHONY: develop
develop: build
	docker run --rm -d -v $$(pwd)/static:/project/static dev_gulp

.PHONY: stop
stop:
	-docker kill $$(docker ps -q)
