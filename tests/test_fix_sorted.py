from __future__ import absolute_import

from utils import check_on_input


# py2, sorted(iterable[, cmp[, key[, reverse]]])
SORTED_CALL = ("""\
sorted(a_list, cmp_function)
sorted(a_list, lambda x,y: x-y)
sorted(a_list, key=key_function, reverse=True)
""", """\
from __future__ import absolute_import
from functools import cmp_to_key
sorted(a_list, key=cmp_to_key(cmp_function))
sorted(a_list, key=cmp_to_key(lambda x,y: x-y))
sorted(a_list, key=key_function, reverse=True)
""")


LIST_SORT_CALL = ("""\
a_list.sort(cmp_function)
a_list.sort(lambda x,y: x-y)
a_list.sort(key=key_function, reverse=True)
""", """\
from __future__ import absolute_import
from functools import cmp_to_key
a_list.sort(key=cmp_to_key(cmp_function))
a_list.sort(key=cmp_to_key(lambda x,y: x-y))
a_list.sort(key=key_function, reverse=True)
""")


def test_sorted_call():
    check_on_input(*SORTED_CALL)

def test_list_sort_call():
    check_on_input(*LIST_SORT_CALL)
