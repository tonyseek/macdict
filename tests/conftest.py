from __future__ import absolute_import

from pytest import fixture
from macdict.foundation import autorelease_pool as _autorelease_pool


@fixture
def autorelease_pool():
    with _autorelease_pool() as pool:
        yield pool
