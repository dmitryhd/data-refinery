FROM python:3.5.2
MAINTAINER Dmitrii Khodakov <>

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["py.test", "-q"]
