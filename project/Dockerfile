# pull official base image
FROM python:3.8.3-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc --no-install-recommends \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# install python dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# add app
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
