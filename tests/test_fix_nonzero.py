from __future__ import absolute_import

from utils import check_on_input


NONZERO_DEF = ("""\
class Foo:
    def other(self):
        return false

    def __nonzero__(self):
        return true

    def another(self):
        return false
""", """\
from __future__ import absolute_import
import six
class Foo:
    def other(self):
        return false

    def __bool__(self):
        return true

    if six.PY2:
        __nonzero__ = __bool__

    def another(self):
        return false
""")

NONZERO_DEF_2_SPACE_INDENT = ("""\
class Foo:
  def other(self):
    return false

  def __nonzero__(self):
    return true

  def another(self):
    return false
""", """\
from __future__ import absolute_import
import six
class Foo:
  def other(self):
    return false

  def __bool__(self):
    return true

  if six.PY2:
    __nonzero__ = __bool__

  def another(self):
    return false
""")

MULTI_CLASS_NONZERO_DEF = ("""\
class Foo:
    def __nonzero__(self):
        return true


class Bar:
    pass
""", """\
from __future__ import absolute_import
import six
class Foo:
    def __bool__(self):
        return true

    if six.PY2:
        __nonzero__ = __bool__


class Bar:
    pass
""")

INNER_CLASS_NONZERO_DEF = ("""\
class Baz:
    class Foo:
        def __nonzero__(self):
            return true
""", """\
from __future__ import absolute_import
import six
class Baz:
    class Foo:
        def __bool__(self):
            return true

        if six.PY2:
            __nonzero__ = __bool__
""")


def test_nonzero_def():
    check_on_input(*NONZERO_DEF)

def test_nonzero_def_2_space_indent():
    check_on_input(*NONZERO_DEF_2_SPACE_INDENT)

def test_multi_class_nonzero_def():
    check_on_input(*MULTI_CLASS_NONZERO_DEF)

def test_inner_class_nonzero_def():
    check_on_input(*INNER_CLASS_NONZERO_DEF)
