=======
Is ISBN
=======


.. image:: https://img.shields.io/pypi/v/is_isbn.svg
        :target: https://pypi.python.org/pypi/is_isbn

.. image:: https://img.shields.io/travis/khimsh/is_isbn.svg
        :target: https://travis-ci.org/khimsh/is_isbn

.. image:: https://readthedocs.org/projects/is-isbn/badge/?version=latest
        :target: https://is-isbn.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/khimsh/is_isbn/shield.svg
     :target: https://pyup.io/repos/github/khimsh/is_isbn/
     :alt: Updates


Description
-----------

**Is ISBN** provides a single function to test if a given string is valid ISBN.


Installation
------------


::

    pip install is-isbn


With pipenv:
::

    pipenv install is-isbn


Usage
-----

Import:
::

    from is_isbn.is_isbn import is_isbn


Use:
::

    is_isbn('978-9941-445-51-4')


or
**

Import:
::

    from is_isbn import is_isbn


Use:
::

    is_isbn.is_isbn('978-9941-445-51-4')

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


* Free software: MIT license
* Documentation: https://is-isbn.readthedocs.io.