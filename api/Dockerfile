FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
RUN pip install --upgrade pip
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src/