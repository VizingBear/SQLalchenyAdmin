FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt


COPY . .

CMD gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
