FROM python:3.9-slim

LABEL maintainer="Django-Stripe_API"

WORKDIR /app

COPY requirements.txt .

RUN pip3 install gunicorn
RUN pip3 install -r requirements.txt

COPY . .

ADD .env ./

VOLUME ["/data"]

EXPOSE 8001

CMD ["gunicorn", "config.wsgi", "-w", "4", "-t", "600", "-b", "0.0.0.0:8001"]