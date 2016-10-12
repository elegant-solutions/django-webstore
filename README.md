# What is this Django Webstore?

This webstore was built with Python, Django, and jQuery, and deployed via Heroku. It was developed by Keith Brandtjen, Britt Johnson, Rachael Wisecarver, and Sonnet Lauberth. We are using Django REST Framework for our API.

### You can find our site deployed at: https://django-sweets-store.herokuapp.com
### You can read our API docs at: https://django-sweets-store.herokuapp.com/docs
### You can read our developer docs at: http://django-webstore.readthedocs.io/en/latest/

## Developer Instructions

To download our site locally, do the following in your command line:

1. `git clone https://github.com/elegant-solutions/django-webstore.git`
2. `pip install virtualenv`
3. `mkvirutalenv store`
4. `cd store`
5. `source bin/activate`
6. `cd django-webstore`
7. `pip install -r requirements.txt`
8. `python manage.py makemigrations`
9. `python manage.py migrate`
10. `python manage.py runserver`
11. Congrats! You should be able to go to `localhost:8000` in your browser and view our site!

## Testing the Braintree API via Our Site

We are currently using a sandbox account with our Braintree API, so we don't take actual credit cards as
we are still testing and improving this project. To see how the payments work, use this test credit card information:

- Credit Card: 4111 1111 1111 1111
- Expiration Date: 11/19

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise
- Search functionality using Django's Q Lookup
- Prototype-level user login and registration using Django Registration Redux
- A fully functional admin page that allows the store owner/admins to add, delete, and modify product offerings
- Dynamic content loaded using Django templates
- Persistence maintained using a PostgreSQL Database
- Key features loaded asynchronously using Ajax
- RESTful framework implemented using Django routing
- Responsive, mobile-first design
- A fully functional order form. Once the user adds items to their cart, they should be able to proceed to an order form where they can review and modify their order, if need be, add their billing and shipping address, and process their payment using the Braintree API.
- *Deployed using Heroku, thanks to Britt's incredibly hard work and with help from Rick, Chris, and Munir.*

## Future Development

In time, we will implement the following features:

- A fully functional login and registration feature, with full email and password authentication and email marketing capabilities
- The user would then receive an email confirmation of their order status.
- More developed styling so that the page both looks and functions like a real-world e-commerce site.
- Adding/improving analytics, testing, SEO, and speed/optimization
- A chat feature, so that if a user has been browsing products for X amount of time, a chat box would open up asking if they have any questions that can be answered by either a store employee or by a bot.

## Thank you to:

- Rick Patci
- Munir Ibrahim
- Cris Ewing
- Will Weatherford
- Two Scoops of Django
- Django Docs
- Python Docs
- jQuery Docs
- jQuery UI Docs
- AJAX and Mozilla Docs
- Learn Python Book
- Python Reference Book
- Full Stack Python Website: https://www.fullstackpython.com/django.html
- Official Django Tutorial
- Caktus Blog on Various Django Topics (Templating, Heroku, Static File Setup, etc.)
- Justin Mitchell for his Django tutorials
- Django Registration Redux Docs
- Django Model Manager Docs
- Django Templates Docs
- Django Admin Bootstrapped Docs
- Django Crispy Forms
- Heroku-Django Starter Template (White Noise & Gunicorn Docs)
- Django Cookie Cutter Template via Daniel and Audrey Roy Greenfield
- Django Docs on Signals
- Django Docs on Sessions
- Django Docs of Queryset API and Q Lookups
- Django Docs on SMTP
- Bootstrap & Bootstrap Docs
- Font Awesome
- Django HTTP Libraries and Docs
- RegExr Docs and Testing Site
- Adobe Color Wheel
