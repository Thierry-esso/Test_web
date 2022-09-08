# Test_web
Code source de l'app django web dans le cadre du recrutement d'un developpeur full-stack à ANADEB


==============
django-web
==============

1. Introduction_
2. Requirements_
3. Installation_
4. Others_

Introduction
============

**django-web** is the Django_ database adapter for Sqlite.

.. _Django: http://www.djangoproject.com/
.. 

Requirements
============
Python 3.10
Django 4.0
djangorestframework
sqlite


Installation
============

To use this adapter in your Django project:

pip install djangorestframework

- Set::

   'ENGINE': 'django.db.backends.sqlite3'

  in your project settings module.
  
  # Application definition

INSTALLED_APPS = [
    ---------------
    'capsules',
    'rest_framework',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
    },
]

- That's all.

Others
======

;)

