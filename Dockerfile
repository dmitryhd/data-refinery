FROM python:latest
MAINTAINER Dmitrii Khodakov <>
# TODO: add labels maybe?


# Apt packages (for pyodbc package)
# RUN apt-get update && apt-get -y install \
#     unixodbc \
#     unixodbc-dev

# Install python requirements
COPY requirements.txt /tmp/requirements.txt
# COPY requirements-dev.txt /tmp/requirements-dev.txt

RUN pip install -r /tmp/requirements.txt -U
# RUN pip install -r /tmp/requirements-dev.txt -U
RUN pip install --force-reinstall -U colorama

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*

COPY . /app
WORKDIR /app

CMD ["py.test", "-q"]
