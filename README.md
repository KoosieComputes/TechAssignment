# Demo CRM System

## About
This demo is a Django app which implements a Customer Relational Manager (CRM) system. Relationship Managers (RMs) log into the system and request documents from their customers.

## Setup
In the root of the project, install the vendor dependancies:
``` 
pip3 install -r requirements.txt
```
In the `settings_example.py` file, set the `SECRET_KEY` and mail server settings, and rename the file to `settings.py`. The app requires a mail service, the example configuration will work with MailHog, if you choose to use that.
Next make the database migrations, the project uses SQLite:
```
python manage.py makemigrations
python manage.py migrate

```
Next create a superuser:
```
python manage.py createsuperuser
```
Enter your username and email address and create a password.
Finally run the server with:
```
python manage.py runserver
```

## Usage
Ok thats it! You are now the RM, visit [localhost:8000](http://localhost:8000) to login. Functions supported are:
- RMs can login and inspect uploaded documents.
- Send document requests to customers.
- Manage customer info and documents.
