|Build Status| |Coverage Status| |PyPI Version|

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


CLI Usage
---------

::

    $ macdict-lookup apple
    apple | BrE ˈap(ə)l, AmE ˈæpəl | noun (fruit) ...


API Usage
---------

.. code-block:: python

   from macdict import lookup_word

   definition = lookup_word(u'apple')
   print(definition)


Contributing
------------

If you want to report bugs or request features, please feel free to open issues
or create pull requests on GitHub_.


.. _Dictionary Services: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/DictionaryServicesProgGuide/
.. _ctypes: https://docs.python.org/dev/library/ctypes.html
.. _pipsi: https://github.com/mitsuhiko/pipsi
.. _GitHub: https://github.com/tonyseek/macdict/issues
.. |Build Status| image:: https://img.shields.io/travis/tonyseek/macdict.svg?style=flat
   :target: https://travis-ci.org/tonyseek/macdict
   :alt: Build Status
.. |Coverage Status| image:: https://img.shields.io/coveralls/tonyseek/macdict.svg?style=flat
   :target: https://coveralls.io/r/tonyseek/macdict
   :alt: Coverage Status
.. |PyPI Version| image:: https://img.shields.io/pypi/v/macdict.svg?style=flat
   :target: https://pypi.python.org/pypi/macdict
   :alt: PyPI Version
