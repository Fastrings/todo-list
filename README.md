
# Python web application using Django

This is a simple web application emulating a to-do list. This application was implemented following Harry Percival's "Test-Driven Web Development with Python", available [here](https://www.obeythetestinggoat.com/)

## PREREQUISITES

This project uses packages that are not in the python standard library, meaning it is needed to install them (using *pip* for example).
Please refer to the [requirements](requirements.txt) file for a list of all the packages needed to make the project work properly.

## USAGE

First and foremost, you need to launch the local server in a terminal, by using the command:

&emsp;python manage.py runserver.

Afterwards, open a window in your favorite browser and enter localhost:8000 (or 127.0.0.1:8000) and you will be able to see the web application.

## TESTS

The test suite is divided in two separate types of tests : functional tests and unit tests. There is a total of 77 tests, with 68 unit tests and 9 functional tests. If you wish to launch the entire test suite (this might take a while), run this command:

&emsp;python manage.py test

If you wish to launch solely the functional tests, run this command:

&emsp;python manage.py test functional_tests

Finally, if you wish to launch only the unit tests, run this command:

&emsp;python manage.py test *module*

Where *module* is the name of the module whose unit tests you want to launch. The modules are 'lists' and 'accounts'