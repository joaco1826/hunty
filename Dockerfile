FROM python:3.9.13-alpine
WORKDIR /www

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /www

RUN pip3.9 install -r requirements.txt

RUN pytest

CMD ["uvicorn", "config.settings:app", "--host", "0.0.0.0", "--port", "8001", "--reload", "--log-level", "info"]