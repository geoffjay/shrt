FROM python:3.7-alpine3.10
MAINTAINER Geoff Johnson <geoff.jay@gmail.com>

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apk update \
    && apk upgrade \
    && apk add \
        py3-setuptools \
        sqlite

WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
