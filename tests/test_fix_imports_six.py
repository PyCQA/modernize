from __future__ import generator_stop


try:
    from six.moves import tkinter
except ImportError:
    tkinter = None

from utils import check_on_input


MOVED_MODULE = (
    """\
import ConfigParser
ConfigParser.ConfigParser()
""",
    """\
from __future__ import absolute_import
import six.moves.configparser
six.moves.configparser.ConfigParser()
""",
)

MOVED_MODULE_FROMLIST = (
    """\
from ConfigParser import ConfigParser
ConfigParser()
""",
    """\
from __future__ import absolute_import
from six.moves.configparser import ConfigParser
ConfigParser()
""",
)


def test_moved_module():
    check_on_input(*MOVED_MODULE)


def test_moved_module_fromlist():
    check_on_input(*MOVED_MODULE_FROMLIST)
