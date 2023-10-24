FROM python:3.8.10

WORKDIR /docker-app

COPY . .

RUN pip install \
        wheel \
        setuptools \
        twine

RUN chmod +x ./run-script.sh
