from __future__ import absolute_import

import ctypes

from macdict.foundation import (
    objc, sel_name, CFStringCreateWithBytes, CFStringEncodingUTF8, CFRange,
    DCSCopyTextDefinition)


def lookup_word(word):
    word_bytes = word.encode('utf-8')
    word_cfstring = CFStringCreateWithBytes(
        None, word_bytes, len(word_bytes), CFStringEncodingUTF8, False)
    definition_nsstring = DCSCopyTextDefinition(
        None, word_cfstring, CFRange(0, len(word_bytes)))
    definition = ctypes.c_char_p(objc.objc_msgSend(
        definition_nsstring, sel_name('UTF8String')))
    if definition.value:
        return definition.value.decode('utf-8')


def ensure_unicode(text, encoding):
    if isinstance(text, bytes):
        return text.decode(encoding)
    return text
