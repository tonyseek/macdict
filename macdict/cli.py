from __future__ import absolute_import

import sys
import argparse

from macdict.foundation import autorelease_pool
from macdict.dictionary import lookup_word


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
    with autorelease_pool():
        definition = lookup_word(args.word)
    if definition is None:
        abort(u'Definition not found for "%s"' % args.word)
    else:
        report(definition)
