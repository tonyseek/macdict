from __future__ import absolute_import

from macdict.dictionary import lookup_word


def test_lookup_word(autorelease_pool):
    definition = lookup_word(u'apple')
    assert u'an apple a day keeps the doctor away' in definition
