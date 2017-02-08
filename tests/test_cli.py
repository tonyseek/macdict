from __future__ import absolute_import

import sys
import pkg_resources

from pytest import fixture, raises


@fixture
def entry_point():
    return next(
        ep for ep in pkg_resources.iter_entry_points(group='console_scripts')
        if ep.name == 'macdict-lookup'
    )


def test_lookup_word(entry_point, mocker):
    mocker.patch('sys.argv', [entry_point.name, 'apple'])
    mocker.patch('sys.stdout', autospec=True)
    mocker.patch('sys.stderr', autospec=True)

    main = entry_point.load()
    with raises(SystemExit) as error:
        main()
    assert error.value.args[0] == 0
    assert u'fruit' in sys.stdout.write.call_args[0][0]


def test_lookup_nothing(entry_point, mocker):
    mocker.patch('sys.argv', [entry_point.name, 'foobarbaz'])
    mocker.patch('sys.stdout', autospec=True)
    mocker.patch('sys.stderr', autospec=True)

    main = entry_point.load()
    with raises(SystemExit) as error:
        main()
    assert error.value.args[0] == 1
    assert u'not found' in sys.stderr.write.call_args[0][0]
