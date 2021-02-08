FROM python:3.7.4


RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

ENV PYTHONUNBUFFERD=1

EXPOSE 8080

CMD ["python","-u","program.py"]
