FROM python:3.12

COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

STOPSIGNAL SIGKILL

CMD [ -d alembic ] && reflex db migrate; \
    exec reflex run
