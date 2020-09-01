from __future__ import generator_stop

from utils import check_on_input

CLASSIC_DIVISION = (
    """\
a /= 3
1 / 2
""",
    """\
from __future__ import division
a //= 3
1 // 2
""",
)

NEW_DIVISION = (
    """\
from __future__ import division
1 / 2
a /= 3
""",
    """\
from __future__ import division
1 / 2
a /= 3
""",
)


def test_optional():
    check_on_input(CLASSIC_DIVISION[0], CLASSIC_DIVISION[0])


def test_fix_classic_division():
    check_on_input(
        *CLASSIC_DIVISION, extra_flags=["-f", "libmodernize.fixes.fix_classic_division"]
    )


def test_new_division():
    check_on_input(
        *NEW_DIVISION, extra_flags=["-f", "libmodernize.fixes.fix_classic_division"]
    )
