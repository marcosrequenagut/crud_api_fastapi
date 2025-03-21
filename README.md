# APP crud API
This is a REST API CRUD application to manage the time you dedicate to your company's projects.

Using a REST API, you'll be able to create and delete projects, log the time spent on tasks, and view a summary of the total hours dedicated to each project.

# How to use

First, install the dependencies
```
$ python -m venv .venv
$ . .venv/bin/activate
$ python -m pip install -r requirements.txt
```

To run the app you can run:
```
$ fastapi dev src/main.py
```

Now to use the API you can go to the documentation page of the api at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)