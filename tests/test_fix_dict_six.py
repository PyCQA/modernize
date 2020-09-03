from __future__ import generator_stop

from utils import check_on_input

TYPES = "keys", "items", "values"

DICT_ITER = (
    """\
x.iter{type}()
""",
    """\
from __future__ import absolute_import
import six
six.iter{type}(x)
""",
)

DICT_VIEW = (
    """\
x.view{type}()
""",
    """\
from __future__ import absolute_import
import six
six.view{type}(x)
""",
)

DICT_PLAIN = (
    """\
x.{type}()
""",
    """\
list(x.{type}())
""",
)

DICT_IN_LOOP = (
    """\
for k in x.items():
    pass
""",
    """\
for k in x.items():
    pass
""",
)

DICT_ITER_IN_LOOP = (
    """\
for k in x.iter{type}():
    pass
""",
    """\
from __future__ import absolute_import
import six
for k in six.iter{type}(x):
    pass
""",
)

DICT_ITER_IN_LIST = (
    """\
for k in list(x.iter{type}()):
    pass
""",
    """\
from __future__ import absolute_import
import six
for k in list(six.iter{type}(x)):
    pass
""",
)

CHAINED_CALLS = (
    """\
(x + y).foo().iter{type}().bar()
""",
    """\
from __future__ import absolute_import
import six
six.iter{type}((x + y).foo()).bar()
""",
)


def check_all_types(input, output):
    for type_ in TYPES:
        check_on_input(input.format(type=type_), output.format(type=type_))


def test_dict_iter():
    check_all_types(*DICT_ITER)


def test_dict_view():
    check_all_types(*DICT_VIEW)


def test_dict_plain():
    check_all_types(*DICT_PLAIN)


def test_dict_in_loop():
    check_on_input(*DICT_IN_LOOP)


def test_dict_iter_in_loop():
    check_all_types(*DICT_ITER_IN_LOOP)


def test_dict_iter_in_list():
    check_all_types(*DICT_ITER_IN_LIST)


def test_chained_calls():
    check_all_types(*CHAINED_CALLS)
