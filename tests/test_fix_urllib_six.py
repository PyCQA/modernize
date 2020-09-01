from __future__ import generator_stop

from utils import check_on_input

URLLIB_MODULE_REFERENCE = (
    """\
import urllib
urllib.quote_plus('hello world')
""",
    """\
from __future__ import absolute_import
import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error
six.moves.urllib.parse.quote_plus('hello world')
""",
)


URLLIB_FUNCTION_REFERENCE = (
    """\
from urllib2 import urlopen
urlopen('https://www.python.org')
""",
    """\
from __future__ import absolute_import
from six.moves.urllib.request import urlopen
urlopen('https://www.python.org')
""",
)


URLLIB_MULTI_IMPORT_REFERENCE = (
    """\
from urllib2 import HTTPError, urlopen
""",
    """\
from __future__ import absolute_import
from six.moves.urllib.error import HTTPError
from six.moves.urllib.request import urlopen
""",
)


URLLIB_IMPORT_AS = (
    """\
from urllib2 import urlopen as urlo
from urllib2 import HTTPError, URLError as urle
""",
    """\
from __future__ import absolute_import
from six.moves.urllib.request import urlopen as urlo
from six.moves.urllib.error import HTTPError, URLError as urle
""",
)


# Can't be converted; translation would emit a warning.
URLIB_INVALID_CODE = (
    """\
from urllib2 import *
from urllib2 import foobarraz
from urllib2 import foo, bar as raz
import urllib as urllib_py2
import urllib
urllib.foobarraz('hello world')
""",
    """\
from __future__ import absolute_import
from urllib2 import *
from urllib2 import foobarraz
from urllib2 import foo, bar as raz
import urllib as urllib_py2
import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error
urllib.foobarraz('hello world')
""",
)


def test_urllib_module_reference():
    check_on_input(*URLLIB_MODULE_REFERENCE)


def test_urllib_function_reference():
    check_on_input(*URLLIB_FUNCTION_REFERENCE)


def test_urllib_multi_import():
    check_on_input(*URLLIB_MULTI_IMPORT_REFERENCE)


def test_urllib_import_as():
    check_on_input(*URLLIB_IMPORT_AS)


def test_urllib_invalid_imports():
    check_on_input(*URLIB_INVALID_CODE)
