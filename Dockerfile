FROM python:3.10-slim

WORKDIR /code

ENV ACTIVE_PROFILE=prod

COPY ./requirements.txt /code/requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./version.txt /code/version.txt
COPY ./app /code/app

EXPOSE 8000

CMD ["fastapi", "run", "--port", "8000"]