import sys
try:
    from StringIO import StringIO  # Python 2
except ImportError:
    from io import StringIO  # Python 3

from libmodernize.main import main as modernize_main
from utils import check_on_input

def test_list_fixers():
    sio = StringIO()
    real_stdout = sys.stdout
    sys.stdout = sio
    try:
        exitcode = modernize_main(['-l'])
    finally:
        sys.stdout = real_stdout
    assert exitcode == 0, exitcode
    assert 'xrange_six' in sio.getvalue()

NO_SIX_SAMPLE = """\
a = range(10)

class B(object):
    __metaclass__ = Meta
"""

EXPECTED_SIX_RESULT = """\
from __future__ import absolute_import
import six
from six.moves import range
a = list(range(10))

class B(six.with_metaclass(Meta, object)):
    pass
"""


def test_no_six():
    check_on_input(NO_SIX_SAMPLE, NO_SIX_SAMPLE,
                   extra_flags=['--no-six'],
                   expected_return_code=0)


def test_enforce():
    check_on_input(NO_SIX_SAMPLE, EXPECTED_SIX_RESULT,
                   extra_flags=['--enforce'],
                   expected_return_code=2)
