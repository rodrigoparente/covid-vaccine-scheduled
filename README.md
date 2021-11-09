# Covid Vaccine Scheduled

A program that verify if a person is scheduled to receive the Covid-19 vaccine in Fortaleza, and send this information by Telegram.

Table of contents:

- [How to use the program without Docker](#how-to-use-the-program-without-docker)
- [How to use the program with Docker](#how-to-use-the-program-with-docker)


---
## How to use the program without Docker

### Dependencies

These instructions assume you're using Python 3 on a Debian OS, and have a [Telegram Bot](https://core.telegram.org/bots).

#### OS packages

```
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
```

#### Python packages 

```
pip install requests selenium pdftotext
```

### Configuring

It is necessary to configure four variables located at ```config.py``` file:

 - NAMES: an array with the names to search;
 - CHAT_ID: unique identifier for the target chat;
 - BOT_TOKEN: is a string required to authorize the bot to send requests;
 - DAYS: number of days past you want to check.

You can also load those values from enviroment variables, for example:

```
export NAMES="['FRANCISCO SANTOS', 'MARIA SILVA']"
export CHAT_ID="1234"
export BOT_TOKEN="1234"
export DAYS=1
```

### Running

Use the following command to run:

```
python main.py
```


---
## How to use the program with Docker

### Dependencies

You only need to have Docker version 20.10.0+ installed.

### Configuring

It is necessary to create an ```.env file``` at the root of the project, and set four variables in the file:

 - NAMES: an array with the names to search;
 - CHAT_ID: unique identifier for the target chat;
 - BOT_TOKEN: is a string required to authorize the bot to send requests;
 - DAYS: number of days past you want to check.

Example:
```
#.env
NAMES="['FRANCISCO SANTOS', 'MARIA SILVA']"
CHAT_ID="1234"
BOT_TOKEN="1234"
DAYS=1
```

### Running

```
docker image build . -t vaccine-app
docker container run --rm --env-file .env vaccine-app
```
