"""
WSGI config for movie_collection project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

# from dotenv import load_dotenv   #for python-dotenv method
# load_dotenv()                    #for python-dotenv method

# user_name = os.environ.get('USER')
# password = os.environ.get('password')

# print(user_name,password,"------")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_collection.settings')

application = get_wsgi_application()
