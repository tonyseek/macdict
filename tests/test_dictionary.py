from __future__ import absolute_import

from macdict.dictionary import lookup_word


def test_lookup_word():
    definition = lookup_word(u'apple')
    assert u'fruit' in definition


def test_lookup_nothing():
    definition = lookup_word(u'foobarbaz')
    assert definition is None
