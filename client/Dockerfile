FROM python:3.8

RUN pip install pipenv

COPY ./ ~/app

WORKDIR ~/app

RUN pipenv sync

CMD ["pipenv", "run", "python", "main.py"]