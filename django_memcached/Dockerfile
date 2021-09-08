FROM python:3.8

RUN pip install pipenv

COPY ./django_memcached ~/app

WORKDIR ~/app

RUN pipenv install

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "--log-level", "DEBUG", "django_memcached.wsgi:application"]