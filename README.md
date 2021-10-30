# Covid Vaccine Scheduled

A simple program that verify if a person is scheduled to receive the Covid-19 vaccine in Fortaleza.

## Dependencies

### OS

These instructions assume you're using Python 3 on a Debian OS.

```
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
```

### Python

```
pip install requests selenium pdftotext
```

## Configuring

While using the script, it is necessary to configure three variables located at ```config.py``` file:

 - NAMES: an array with the names to search;
 - CHAT_ID: unique identifier for the target chat;
 - BOT_TOKEN: is a string required to authorize the bot to send requests.

You can also load those values from enviroment variables.

## Running

Use the following command to run:

```
python main.py
```


