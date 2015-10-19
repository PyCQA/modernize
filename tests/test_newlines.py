from __future__ import absolute_import

import os
from utils import check_on_input, expect_error
from test_fix_basestring import BASESTRING as TESTCASE


def test_mixed_to_native_line_endings():
    check_on_input('\r\n' + TESTCASE[0],
                   ('\n' + TESTCASE[1]).replace('\n', os.linesep),
                   mode="b"),
         
def test_windows_to_unix_line_endings():
    check_on_input(TESTCASE[0].replace('\n', '\r\n'),
                   TESTCASE[1],
                   extra_flags=['--unix-line-endings'],
                   mode="b")

def test_unix_to_windows_line_endings():
    check_on_input(TESTCASE[0],
                   TESTCASE[1].replace('\n', '\r\n'),
                   extra_flags=['--windows-line-endings'],
                   mode="b")

def test_options_conflict():
    expect_error(TESTCASE[0],
                 extra_flags=['--unix-line-endings', '--windows-line-endings'])
