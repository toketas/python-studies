FROM python:3.8.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip

COPY . /app
COPY utils/entrypoint.sh /

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["/entrypoint.sh"]
