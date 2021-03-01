FROM python:3
WORKDIR /code
COPY requirements /code/requirements
RUN pip install -r requirements/development.txt
COPY . /code/