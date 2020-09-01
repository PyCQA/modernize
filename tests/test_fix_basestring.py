from __future__ import generator_stop

from utils import check_on_input

BASESTRING = (
    """\
isinstance(x, basestring)
""",
    """\
from __future__ import absolute_import
import six
isinstance(x, six.string_types)
""",
)


def test_basestring():
    check_on_input(*BASESTRING)
