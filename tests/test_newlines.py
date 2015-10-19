from __future__ import absolute_import

import os
from utils import check_on_input, expect_error

TESTCASE = ("""\
# sample code
isinstance(x, basestring)
""", """\
# sample code
from __future__ import absolute_import
import six
isinstance(x, six.string_types)
""")


def test_to_native_line_endings():
    foreign_linesep = '\r\n' if (os.linesep == '\n') else '\n'
    check_on_input(TESTCASE[0], TESTCASE[1].replace('\n', os.linesep),
                   write_newline=foreign_linesep, read_newline='')

def test_windows_to_unix_line_endings():
    check_on_input(TESTCASE[0], TESTCASE[1],
                   extra_flags=['--unix-line-endings'],
                   write_newline='\r\n', read_newline='')

def test_unix_to_windows_line_endings():
    check_on_input(TESTCASE[0], TESTCASE[1].replace('\n', '\r\n'),
                   extra_flags=['--windows-line-endings'],
                   write_newline='\n', read_newline='')

def test_options_conflict():
    expect_error(TESTCASE[0],
                 extra_flags=['--unix-line-endings', '--windows-line-endings'])
