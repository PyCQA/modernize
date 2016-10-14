from __future__ import absolute_import

from utils import check_on_input


UNICHR_TYPE_REF = ("""\
isinstance(u'a', unichr)
""", """\
from __future__ import absolute_import
from six import unichr
isinstance(u'a', unichr)
""")

UNICHR_TYPE_CALL = ("""\
unichr(42)
""", """\
from __future__ import absolute_import
from six import unichr
unichr(42)
""")

UNICHR_USER_CALL = ("""\
foobar.unichr(42)
""", """\
foobar.unichr(42)
""")

def test_unichr_type_ref():
    check_on_input(*UNICHR_TYPE_REF)


def test_unichr_type_call():
    check_on_input(*UNICHR_TYPE_CALL)


def test_unichr_user_call():
    check_on_input(*UNICHR_USER_CALL)
