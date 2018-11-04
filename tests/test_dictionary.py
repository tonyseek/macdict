from __future__ import absolute_import

from macdict.dictionary import lookup_word, ensure_unicode


def test_lookup_word():
    definition = lookup_word(u'apple')
    assert u'fruit' in definition


def test_lookup_nothing():
    definition = lookup_word(u'foobarbaz')
    assert definition is None


def test_ensure_unicode():
    assert ensure_unicode(u'\u7784', 'utf-8') == u'\u7784'
    assert ensure_unicode(b'\xe7\x9e\x84', 'utf-8') == u'\u7784'
