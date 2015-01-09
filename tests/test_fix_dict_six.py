from __future__ import absolute_import

from utils import check_on_input


TYPES = 'keys', 'items', 'values'

DICT_ITER = ("""\
x.iter{type}()
""", """\
from __future__ import absolute_import
import six
six.iter{type}(x)
""")

DICT_VIEW = ("""\
x.view{type}()
""", """\
from __future__ import absolute_import
import six
six.view{type}(x)
""")

DICT_PLAIN = ("""\
x.{type}()
""", """\
list(x.{type}())
""")


def check_all_types(input, output):
    for type_ in TYPES:
        check_on_input(input.format(type=type_), output.format(type=type_))

def test_dict_iter():
    check_all_types(*DICT_ITER)

def test_dict_view():
    check_all_types(*DICT_VIEW)

def test_dict_plain():
    check_all_types(*DICT_PLAIN)
