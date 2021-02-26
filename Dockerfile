FROM python:3
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=pdfprocessor.settings.development
ENV SECRET_KEY=pdfprocessor.settings.development
WORKDIR /code
COPY requirements /code/requirements
RUN pip install -r requirements/development.txt
COPY . /code/