build_api:
	docker build -f api/Dockerfile -t bp-api --target dev_stage .

run_api: build_api
	docker run --env-file=api/env -p 8080:8080 bp-api
