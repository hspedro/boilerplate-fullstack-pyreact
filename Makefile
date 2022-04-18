build_api:
	docker-compose build api

run_api: build_api
	docker-compose up
