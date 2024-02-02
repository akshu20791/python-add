FROM python:3.10.6-alpine
WORKDIR /usr/src/app
COPY . .
RUN apk update
RUN chmod a+x ./*.py
ENTRYPOINT ["python", "-u", "./application.py" ]


