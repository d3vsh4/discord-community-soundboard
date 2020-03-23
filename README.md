# Discord Community Soundboard

A discord bot built for "enriching" your discord experience playing custom soundclips -
The main feature is a web interface that allows you to control the bot, manage users and upload custom sound clips.


# Getting Started

## Fontend


### Prerequisites

A recent version of [Node](https://nodejs.org/en/download/) is required.


### Installing
From the project root, run the following

```
cd frontend
npm install
```

###Running

Run the app in the development mode with

```
npm start
```
in the ```fronted``` directory.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.

## Deployment

To build the react app, run
```
npm run build
```

in the ```fronted``` directory.

!TODO: Webserver

## Backend



### Prerequisites

The backend of the bot is built on Django 3.0, so [Python 3.6+](https://www.python.org/downloads/) is required.
If you are on Windows, be sure to [add Python to PATH](https://datatofish.com/add-python-to-windows-path/).

To self-host/develop the bot, you will also need to create a bot application [here](https://discordapp.com/developers/applications/) 
and retreive the token (New Application > Bot > Add Bot > Copy Token).



### Installing

From the project root, run the following

```
cd backend
pip install -r requirements.txt
```

#####Next, you will need to configure two secret keys for the project: 

In `backend/backend/settings.py` replace the placeholder string 

```
SECRET_KEY = 'YOUR_SECRET_KEY_HERE'
```

with a secret key created at [djecrety](https://djecrety.ir/).

In `backend/discord_bot/discord_interface/config/config.py` replace

```
TOKEN: str = "YOUR_TOKEN_HERE"
```

with your discord bot token.

#### Database Setup

Get [PostgreSQL 10.12](https://www.postgresql.org/download/).


In psql, setup a database and a user while replacing your_password_here with a strong password of your own:
```
CREATE DATABASE discordbotbackend;
CREATE USER discordbotuser WITH PASSWORD 'your_password_here';
ALTER ROLE discordbotuser SET client_encoding TO 'utf8';
ALTER ROLE discordbotuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE discordbotuser SET timezone TO 'CET';
GRANT ALL PRIVILEGES ON DATABASE discordbotbackend TO discordbotuser;
```

Finally replace the PASSWORD field in the DATABASES entry in ```backend/backend/setting.py```:
```
. . .

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'discordbotbackend',
        'USER': 'discordbotuser',
        'PASSWORD': 'your_password_here',
        'HOST': 'localhost',
        'PORT': '',
    }
}

. . .

```

Afterwards, run

```
python manage.py makemigrations
python manage.py migrate
``` 

in the ```backend``` directory to  configure the database.


###Running

Start the backend with

```
python run.py
```

in the ```backend``` directory.

The server will be listening on [http://localhost:8080](http://localhost:8080)


## Authors

* **Adrian Steffan** - [adriansteffan](https://github.com/adriansteffan)

