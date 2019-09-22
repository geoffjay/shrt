# Shrt

A URL shortener with a GraphQL API.

After a new URL has been submitted a shortened tag value is generated and
returned, it can be used to recall the original value used to create the entry.
The tag can also be used directly with the host address to redirect to the
original URL. For example, if the server was running locally using default
settings, visiting the address http://localhost:8000/abcd would redirect to
the original URL if one exists with a tag value matching `abcd`.

## Configuration

The shortened URL when provided is built using variables from the application
`settings.py` file. The defaults used during development are given in this
table.

Variable | Default Value
:-: | :-:
`SITE_DOMAIN` | localhost
`SITE_PORT` | 8000
`SITE_PROTOCOL` | http

This will generate a site address of http://localhost:8000 to use with the
shortened URL.

## Running

### Docker

Using `docker` is the preferred method to retrieve and run `shrt`, this is done
the usual way with the `pull` and `run` commands.

```sh
docker pull geoffjay/shrt:latest
docker run --rm -p "8000:8000" -it geoffjay/shrt:latest
```

#### Environment

Variables to change the address to bind to and the port to listen on are
available.

Variable | Default Value
:-: | :-:
`SHRT_BIND` | 0.0.0.0
`SHRT_PORT` | 8000

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

### Testing

Simple schema tests have been added and can be executed using the `django`
management command `test`.

```sh
python manage.py test
```

## Queries

Queries are available to submit a new URL, read all entries, read a single
entry back by ID or by tag, and to delete a single entry by ID.

### Create

```gql
mutation {
  createUrl(original: "https://github.com/geoffjay/shrt") {
    id
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
      "id": 2,
      "original": "https://github.com/geoffjay/shrt",
      "shortened": "http://localhost:8000/jkBa"
    }
  }
}
```

### Read

#### By ID

```gql
query {
  url(id: 1) {
    original
    tag
    shortened
  }
}
```

Result:

```json
{
  "data": {
    "url": {
      "original": "http://github.com/geoffjay/shrt",
      "tag": "AMzy",
      "shortened": "http://localhost:8000/AMzy"
    }
  }
}
```

#### By Tag

```gql
query {
  url(tag: "AMzy") {
    id
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
    }
  }
}
```

#### By Shortened URL

```gql
query {
  url(shortened: "http://localhost:8000/AMzy") {
    id
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
    }
  }
}
```

### Read All

```gql
query ReadAllUrls {
  allUrls {
    id
    original
    tag
    shortened
  }
}
```

Result:

```json
{
  "data": {
    "allUrls": [
      {
        "id": "1",
        "original": "https://github.com/geoffjay/shrt",
        "tag": "AMzy"
        "shortened": "http://localhost:8000/AMzy"
      },
      {
        "id": "2",
        "original": "https://github.com/geoffjay/shrt",
        "tag": "jkBa"
        "shortened": "http://localhost:8000/jkBa"
      }
    ]
  }
}
```

### Delete

```gql
mutation DeleteUrl {
  deleteUrl(id:2) {
    id
  }
}
```

Result:

```json
{
  "data": {
    "deleteUrl": {
      "id": 2
    }
  }
}
```
