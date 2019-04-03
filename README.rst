# Hannah
Test code to validate API response with three conditions

Dependency
==========
Code is written in Python. It uses `reqests` module of python

`python3`

Installation
============

Do the following in your virtualenv::

  pip3 install requests

API Acceptance Criterion
========================
GET response of the API must meet below conditions:

.. code-block:: python

    1. "Name": "Carbon credits"
    2. "CanRelist": True
    3. The Promotions element with Name = "Gallery" has a Description that contains the text "2x larger image"

API returns ``True`` when all the above three conditions are satisfied.

Execution
=========
Update the file ``main.py`` by modifying the API:

.. code-block:: python

    API_URL='https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'

Run the script on bash shell:

``$ python main.py``
