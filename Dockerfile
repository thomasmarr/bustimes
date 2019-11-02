FROM python:3.8.0-alpine3.10

RUN adduser -D flaskapp

WORKDIR /home/flaskapp

COPY requirements.txt requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY flaskapp flaskapp
COPY run.py config.py start.sh ./
RUN chmod +x start.sh

ENV FLASK_APP run.py

RUN chown -R flaskapp:flaskapp ./
USER flaskapp

EXPOSE 5000
CMD ["/bin/sh", "./start.sh"]