from __future__ import absolute_import

import ctypes

from macdict.foundation import (
    objc, CFStringCreateWithBytes, CFStringEncodingUTF8, CFRange,
    DCSCopyTextDefinition)


def lookup_word(word):
    word_bytes = word.encode('utf-8')
    word_cfstring = CFStringCreateWithBytes(
        None, word_bytes, len(word_bytes), CFStringEncodingUTF8, False)
    definition_nsstring = DCSCopyTextDefinition(
        None, word_cfstring, CFRange(0, len(word_bytes)))
    definition = ctypes.c_char_p(objc.objc_msgSend(
        definition_nsstring, objc.sel_registerName('UTF8String')))
    return definition.value.decode('utf-8')
