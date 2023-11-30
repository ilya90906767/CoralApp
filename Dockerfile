FROM python:3.10-alpine3.13
LABEL maintainer="@betyaev-ilya"

ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt /tmp/requirements.txt
COPY ./web /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /venv 
RUN /venv/bin/pip install --upgrade pip 
RUN apk add --update --no-cache postgresql-client 
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev 
RUN /venv/bin/pip install -r /tmp/requirements.txt
RUN rm -rf /tmp
RUN apk del .tmp-build-deps 


ENV PATH="/venv/bin:$PATH"
