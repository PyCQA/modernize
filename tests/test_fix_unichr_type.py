from __future__ import generator_stop

from utils import check_on_input

UNICHR_METHOD_REF = (
    """\
converter = unichr
""",
    """\
from __future__ import absolute_import
from six import unichr
converter = unichr
""",
)

UNICHR_METHOD_CALL = (
    """\
unichr(42)
""",
    """\
from __future__ import absolute_import
from six import unichr
unichr(42)
""",
)

UNICHR_USER_CALL = (
    """\
foobar.unichr(42)
""",
    """\
foobar.unichr(42)
""",
)


def test_unichr_method_ref():
    check_on_input(*UNICHR_METHOD_REF)


def test_unichr_method_call():
    check_on_input(*UNICHR_METHOD_CALL)


def test_unichr_user_call():
    check_on_input(*UNICHR_USER_CALL)
