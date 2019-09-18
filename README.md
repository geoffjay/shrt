# Shrt

A URL shortener.

## Running

### Docker

```sh
docker pull geoffjay/shrt:latest
docker run --rm -p 8000:80 -it geoffjay/shrt:latest
```

### Virtual Environment

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -e .
```

## Queries

### Create

```sh
mutation {
  createUrl(name: "https://github.com/geoffjay/shrt") {
    original
    shortened
	}
}
```

### Read

```sh
query {
  url(shortened: "http://localhost/AMZQ") {
    original
  }
}
```
