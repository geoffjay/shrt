FROM python:3.7-alpine3.10
MAINTAINER Geoff Johnson <geoff.jay@gmail.com>

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apk update \
    && apk upgrade \
    && apk add \
        build-base \
        gcc \
        python3-dev \
        py3-setuptools \
        sqlite

WORKDIR /app
COPY . .

ENV SHRT_BIND=0.0.0.0
ENV SHRT_PORT=8000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate \
    && python manage.py migrate

EXPOSE "$SHRT_PORT"
CMD python manage.py runserver $SHRT_BIND:$SHRT_PORT
