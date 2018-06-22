# How to separate the python files with request url

## Usage

`apps/controller/__init__.py` have `app` wsgi application. It use for all controller files.

Example for start the server.

```sh
$ make start
[*] Start service program.
$ make stop
[*] Stop service program.
```

You can accsess `http://localhost:8080` and `http://localhost:8080/fetch`.
