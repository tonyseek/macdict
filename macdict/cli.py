from __future__ import absolute_import

import sys
import argparse

from macdict.dictionary import lookup_word, ensure_unicode


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    return parser.parse_args()


def abort(text):
    sys.stderr.write(u'%s\n' % text)
    sys.exit(1)


def report(text):
    sys.stdout.write(u'%s\n' % text)
    sys.exit(0)


def main():
    args = parse_args()
    word = ensure_unicode(args.word, 'utf-8')
    definition = lookup_word(word)
    if definition is None:
        abort(u'Definition not found for "%s"' % word)
    else:
        report(definition)
