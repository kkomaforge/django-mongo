=====
Mongo
=====

Mongo is a simple Django app to conduct Web-based mongodb.
For each question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "mongo" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'mongo',
    )

2. Include the mongo URLconf in your project urls.py like this::

    url(r'^mongo/', include('mongo.urls')),

