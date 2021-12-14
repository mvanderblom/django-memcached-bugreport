FROM python:3.9

RUN pip install pipenv

COPY ./ ~/app

WORKDIR ~/app

RUN pipenv sync

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "--log-level", "DEBUG", "django_memcached.wsgi:application"]