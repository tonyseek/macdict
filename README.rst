macdict
=======

*macdict* is a command line utility and library to look up dictionary in macOS.

It is built on the `Dictionary Services`_ (``CoreServices.framework``)
and ctypes_. So we have a pure Python implementation without any compile-time
dependency.

Installation
------------

::

    $ pip install macdict

or with pipsi_ for using its CLI only::

    $ pipsi install macdict

.. _Dictionary Services: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/DictionaryServicesProgGuide/
.. _ctypes: https://docs.python.org/dev/library/ctypes.html
.. _pipsi: https://github.com/mitsuhiko/pipsi

CLI Usage
---------

::

    $ macdict-lookup apple
    apple | BrE ˈap(ə)l, AmE ˈæpəl | noun (fruit) ...

API Usage
---------

.. code-block:: python

   from macdict import pool

   with pool() as p:
       definition = p.lookup_word(u'apple')
   print(definition)
