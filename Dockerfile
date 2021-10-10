FROM python:3
EXPOSE 8000
ENV PYTHONUNBUFFERED 1 \
    PORT=8000
RUN mkdir /code
WORKDIR /code
RUN pip install "gunicorn==20.0.4"
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
