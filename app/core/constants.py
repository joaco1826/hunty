from os import environ


APP_ENV = environ.get('APP_ENV', 'local')
SENTRY_DSN = environ.get('SENTRY_DSN', '')
MONGO_URI = environ.get('MONGO_URI', '')
