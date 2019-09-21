# Shrt

A URL shortener.

## Running

### Docker

Using `docker` is the preferred method to retrieve and run `shrt`, this is done
the usual way.

#### Environment

Variables to set the default address to bind to and the port to listen on are
available.

Variable | Default Value
-: | :-:
`SHRT_BIND` | 0.0.0.0
`SHRT_PORT` | 8000

```sh
docker pull geoffjay/shrt:latest
docker run --rm -p 8000:80 -it geoffjay/shrt:latest
```

### Virtual Environment

Using `venv` to setup the application and its dependencies is done by executing
the following steps.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -e .
```

If it's the first time the application has been started it's necessary to
apply the migrations to the database, and optionally load a piece of
sample data.

```sh
python manage.py migrate
python manage.py loaddata urls
```

After this running `shrt` is done with the `runserver` management command. By
default this binds to `127.0.0.1` and port `8000`, to change this to allow
connections on a different subnet and port it is possible to append something
similar to `0.0.0.0:80` to the command.

```sh
python manage.py runserver
```

## Queries

Submitting a new URL and reading one back are the only queries that have been
implemented.

### Create

```gql
mutation {
  createUrl(name: "https://github.com/geoffjay/shrt") {
    original
    shortened
	}
}
```

Result:

```json
{
  "data": {
    "createUrl": {
      "id": 3,
      "original": "https://github.com/geoffjay/shrt",
      "shortened": "7QoG"
    }
  }
}
```

### Read

```gql
query {
  url(shortened: "http://localhost/AMZQ") {
    original
  }
}
```

Result:

```json
{
  "data": {
    "url": {
      "id": "1",
      "original": "http://github.com/geoffjay/shrt",
      "shortened": "AMZQ"
    }
  }
}
```
