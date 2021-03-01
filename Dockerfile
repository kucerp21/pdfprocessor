FROM python:3
WORKDIR /code
COPY requirements /code/requirements
RUN pip install -r requirements/development.txt
RUN apt-get -y update && apt-get install -y poppler-utils
COPY . /code/