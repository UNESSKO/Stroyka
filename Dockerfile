FROM python:3.10


SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update  && apt install -y sqlite3 libsqlite3-dev

RUN useradd -rms /bin/bash sa

WORKDIR /sa

RUN mkdir /sa/static && mkdir /sa/media && chown -R sa:sa /sa && chmod 755 /sa

COPY --chown=sa:sa . .

RUN pip install -r requirements.txt

USER sa

CMD ["gunicorn", "-b", "0.0.0.0:8001", "soaqaz.wsgi:application"]