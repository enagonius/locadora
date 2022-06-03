from python:3.8.13-slim-bullseye
RUN mkdir -p /opt/app
COPY . /opt/app/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
EXPOSE 8000
cmd ["./manage.py","runserver","0.0.0.0:8000"]