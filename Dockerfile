FROM python:3.8.11-slim-buster

ENV DISPLAY=:99

RUN mkdir /app/files/ -p \
    # Install debian packages
    && apt-get -y -q update \
    && apt-get install -y -q --\
        chromium \
        chromium-driver \
        build-essential \
        libpoppler-cpp-dev \
        pkg-config \
        python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    # install pip packages
    && pip install --upgrade pip \
    && pip3 install -r requirements.txt

WORKDIR /app

COPY . .

CMD ["python3", "./main.py"]