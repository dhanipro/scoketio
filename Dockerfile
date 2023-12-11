FROM python:3.9-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install eventlet


COPY . /home

WORKDIR /home

ENV PYTHONUNBUFFERED=1

ENV FLASK_APP=app.py

CMD ["gunicorn", "-b", "0.0.0.0:8000", "--worker-class", "eventlet", "run:app"]