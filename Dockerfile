# syntax=docker/dockerfile:1
FROM python:3.12.0rc1-alpine3.18
WORKDIR /code

COPY requirements.txt requirements.txt
COPY . .
RUN apk add --no-cache gcc musl-dev linux-headers libpq-dev && \
    pip install -r requirements.txt
CMD ["ash", "-c", "python app.py"]

