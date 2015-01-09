from __future__ import absolute_import

from utils import check_on_input


CLASSIC_DIVISION = ("""\
1 / 2
""",
"""\
from __future__ import division
1 // 2
""")

NEW_DIVISION = ("""\
from __future__ import division
1 / 2
""",
"""\
from __future__ import division
1 / 2
""")


def test_optional():
    check_on_input(CLASSIC_DIVISION[0], CLASSIC_DIVISION[0])

def test_fix_classic_division():
    check_on_input(*CLASSIC_DIVISION,
            extra_flags=['-f', 'libmodernize.fixes.fix_classic_division'])

def test_new_division():
    check_on_input(*NEW_DIVISION,
            extra_flags=['-f', 'libmodernize.fixes.fix_classic_division'])
