FROM python:3.13

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /prdprf
COPY . .

# Install app requirements and reflex in the container
RUN pip install -r requirements.txt

RUN reflex init

RUN reflex export --frontend-only --no-zip

STOPSIGNAL SIGKILL

CMD [ -d alembic ] && reflex db migrate; \
    exec reflex run --env prod
