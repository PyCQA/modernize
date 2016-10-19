from __future__ import absolute_import

from utils import check_on_input


URLLIB_MODULE_REFERENCE = ("""\
import urllib
urllib.quote_plus('hello world')
""", """\
from __future__ import absolute_import
import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error
six.moves.urllib.parse.quote_plus('hello world')
""")


URLLIB_FUNCTION_REFERENCE = ("""\
from urllib2 import urlopen
urlopen('https://www.python.org')
""", """\
from __future__ import absolute_import
from six.moves.urllib.request import urlopen
urlopen('https://www.python.org')
""")


def test_urllib_module_reference():
    check_on_input(*URLLIB_MODULE_REFERENCE)


def test_urllib_function_reference():
    check_on_input(*URLLIB_FUNCTION_REFERENCE)

