from os import environ


APP_ENV = environ.get('APP_ENV', 'local')
SENTRY_DSN = environ.get('SENTRY_DSN', '')
MONGO_URI = environ.get('MONGO_URI', '')

INTERNAL_SERVER_ERROR = 'Internal server error'
NOT_FOUND = 'Not Found'
