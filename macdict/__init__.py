from __future__ import absolute_import

import contextlib

import macdict.dictionary
import macdict.foundation


__version__ = '0.0.0'
__all__ = ['pool']


class Pool(object):
    """The high-level wrap of the Objective-C autorelease pool."""

    def __init__(self, ptr):
        self.ptr = ptr

    def lookup_word(self, *args, **kwargs):
        """Looks up the definition of specific word."""
        return macdict.dictionary.lookup_word(*args, **kwargs)


@contextlib.contextmanager
def pool():
    """A context manager for autorelease pool.

    :returns Pool: The wrap of the raw pointer of autorelease pool.
    """
    with macdict.foundation.autorelease_pool() as pool_ptr:
        yield Pool(pool_ptr)
