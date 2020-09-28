from __future__ import generator_stop

from utils import check_on_input

OPEN = (
    """\
{0}('some/path')
""",
    """\
from io import open
open('some/path')
""",
)


def test_open():
    check_on_input(
        OPEN[0].format("open"),
        OPEN[1],
        extra_flags=["-f", "modernize.fixes.fix_open"],
    )


def test_open_optional():
    check_on_input(OPEN[0].format("open"), OPEN[0].format("open"))


def test_file():
    flags = ["-f", "modernize.fixes.fix_open", "-f", "modernize.fixes.fix_file"]
    check_on_input(OPEN[0].format("file"), OPEN[1], extra_flags=flags)
