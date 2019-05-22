from __future__ import absolute_import

import sys
import unittest

from libmodernize.tests.utils import check_on_input


SHA_NEW = ("""\
import sha
sha.new(data1)
obj = sha.new()
""", """\
import hashlib
hashlib.sha1(data1)
obj = hashlib.sha1()
""")


MD5_NEW = ("""\
import md5
foo = md5.new(data1)
""", """\
import hashlib
foo = hashlib.md5(data1)
""")


SHA_SHA = ("""\
import sha
digest = sha.sha(data1).digest()
""", """\
import hashlib
digest = hashlib.sha1(data1).digest()
""")


MD5_MD5 = ("""\
import md5
digest = md5.md5(data1).digest()
""", """\
import hashlib
digest = hashlib.md5(data1).digest()
""")


NO_IMPORT = ("""\
foo = md5.new(data1)
""", """\
foo = md5.new(data1)
""")


EXTRA_FLAGS = ['-f', 'libmodernize.fixes.fix_sha_md5']


def _check(testcase):
  input_code, expected = testcase
  check_on_input(input_code, expected, EXTRA_FLAGS)


def test_sha_new():
    _check(SHA_NEW)


def test_md5_new():
    _check(MD5_NEW)


def test_sha_sha():
    _check(SHA_SHA)


def test_md5_md5():
    _check(MD5_MD5)


def test_no_import():
    _check(NO_IMPORT)

