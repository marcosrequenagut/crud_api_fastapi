# APP crud API
This is a REST API CRUD application to manage the time you dedicate to your company's projects.

Using a REST API , you'll be able to create and delete projects, log the time spent on tasks, and view a summary of the total hours dedicated to each project.

# How to use

First, install python package
```
$ python -m venv .venv
$ . .venv/bin/activate
$ python -m pip install -e .
```

To run the app you can run:
```
$ python -m src/crud_api
```

To configure how to run the app you can check the help page:
```

```

Now to use the API you can go to the documentation page of the api at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### To run in Docker

To build the image run:

```
$ docker build -t crud_api:latest .
```

Then to run the API use:
```
$ docker run -p 8000:8000 -v ./database:/db crud_api:latest
```
# Development tips
To develop on this project there are additional tooling to support tests.

You can install them with:
```
$pip install -e ".[dev]"
```

Then you can run the tests:

```
$ pytest tests/
```