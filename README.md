# Microservice Hunty Test

-   Language: Python3
-   Framework: FastApi
-   Database: MongoDB
-   Container: Docker


# Installation for Ubuntu 20.04

Install docker

Documentation for install docker [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)

Install docker-compose for development

Documentation for install docker-compose [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)

Copy .env.example to .env
```
cp .env.example .env
```

**Env vars**

```
APP_ENV=local
PORT=8000
SENTRY_DSN=

# Connect Mongo
MONGO_URI=
```

**Run Server**
```
docker-compose up --build
```

# Instalation virtualenv

1.  Install Virtualenv and activate it

```
virtualenv - p python3 venv
```

```
source venv/bin/activate
```

2.  Install requirements.txt

```
pip3 install -r requirements.txt
```
-   Libraries:
    - fastApi
    - mongoengine
    - mongoengine-goodjson
    - pydantic
    - pytest
    - sentry-sdk
    - spectree
    - uvicorn

**run Server**
```
$ uvicorn config.settings:app --host=localhost --port=8001 --reload --log-level=info
```


3. Status services [health](https://0.0.0.0:8001/health)


4. Documentation
[here](https://0.0.0.0:8001/docs)


5. Author: Joaquin Forero
