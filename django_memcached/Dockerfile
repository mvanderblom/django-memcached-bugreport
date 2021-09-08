FROM python:3.8-alpine

RUN pip install pipenv

COPY ./ ~/app

WORKDIR ~/app

RUN pipenv sync

CMD ["pipenv", "run", "gunicorn", "django_memcached.wsgi:application"]