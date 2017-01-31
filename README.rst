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

Usage
-----

::

    $ macdict-lookup apple
