# boilerplate-fullstack-pyreact

Boilerplate fullstack project with Python and React

## Running

To run the API dockerized, one can run:

```bash
make run_api
```

Which will start the API, watching any changes, and bind to port 8080:

```bash
docker run --env-file=api/env -p 8080:8080 bp-api
INFO:     Will watch for changes in these directories: ['/code/api']
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [7] using watchgod
INFO:     Started server process [9]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

```bash
$ curl localhost:8080/status
{"status":"ok"}
```

## Contributing

The project uses linters, and other checks, to enforce style and maintain code quality.
To enable/install them, I recommend using [pre-commit](https://pre-commit.com/) to do
it so:

```bash
pip install pre-commit
pre-commit install -t pre-commit -t commit-msg
```

## Source Code Tree

- [api](api/): Backend files. Currently using Python - FastAPI.
