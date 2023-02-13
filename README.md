# Stripe payment (Django + Stripe)    

## Technologies:

- Django 4.1.6
- Python 3.8.5
- Stripe 5.1.1
- HTML, CSS, JavaScript
- PostgreSQL

## Description

The project of an online store include Stripe API for on-line payment.    
Through the admin panel, you can view, add and delete products, as well as a description of them.    
Users can select products, add to the cart, place an order and go to the online payment page.    

## Setup

Clone this project    
```
https://github.com/ReVadim/Stripe_payment.git
```    
Create virtual environment
```
python -m virtualenv venv
```
Activate virtual environment    

WINDOWS:    
```
venv\Scripts\activate
```
LINUX:    
```
source venv\bin\activate
```
Installing the required dependencies    
```
pip install -r requirements.txt    
```    
Create database and .env file with your personal data    
```
SECRET_KEY = 'django-insecure-ogv*%m#+d)1#&5q*@n0w7*&%r7f%h-a_ybw1l3f1@tmiu7$+er'

# database settings
DATABASE_NAME = ' '
DATABASE_USER = ' '
DATABASE_PASSWORD = ' '
HOST = 127.0.0.1
PORT = 5432

# debug settings
DEBUG = 1
DJANGO_ALLOWED_HOSTS = 127.0.0.1

# stripe settings
STRIPE_PUBLIC_KEY = ' '
STRIPE_SECRET_KEY = ' '
```
Next, perform database migrations and create a superuser.     
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ready
