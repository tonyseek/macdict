from __future__ import absolute_import

from macdict import pool


def test_lookup_word():
    with pool() as p:
        definition = p.lookup_word(u'apple')
        assert u'an apple a day keeps the doctor away' in definition
