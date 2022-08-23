FROM python:3.9.13-alpine
WORKDIR /www
COPY . /www
USER 0
RUN pip3.9 install -r requirements.txt

USER 1001

CMD ["uvicorn", "config.settings:app --host=localhost --port=8001 --reload --log-level=info"]