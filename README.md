# What is Strange Sweets?

Strange Sweets is a webstore built with Python, Django, and jQuery, and deployed via Heroku. It was developed by Keith Brandtjen, Britt Johnson, and Rachael Wisecarver.

You can find our site deployed at https://django-sweets-store.herokuapp.com 

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
- *Deployed using Heroku, thanks to Britt's incredibly hard work and with help from Rick, Chris, and Munir.*

## Future Development

We had big goals with this project, and sadly did not accomplish all of them. If we had just a little more time, we would have implemented the following features:
- A fully functional login and registration feature, with full email and password authentication and email marketing capabilities
- A fully functional order form. Once the user adds items to their cart, they should be able to proceed to an order form where they can review and modify their order, if need be, add their billing and shipping address, and process their payment using the Braintree API. The user would then receive an email confirmation of their order status.
- More developed styling so that the page both looks and functions like a real-world e-commerce site
- A chat feature, so that if a user has been browsing products for X amount of time, a chat box would open up asking if they have any questioned that can be answered by either a store employee or by a bot.

## Thank you to:

- Rick Patci
- Munir Ibrahim
- Cris Ewing
- Two Scoops of Django
- Full Stack Python Website: https://www.fullstackpython.com/django.html
- Justin Mitchell for his Try Django tutorials
- Will Weatherford
- Documentation (Django Docs, Python Docs, jQuery Docs, Django Registration Redux, etc.)
