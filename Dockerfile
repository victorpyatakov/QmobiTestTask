FROM python:3.7.4


RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

EXPOSE 8080

CMD ["python","program.py"]
