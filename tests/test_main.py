from __future__ import generator_stop

import contextlib
import io

from utils import check_on_input

from modernize.__main__ import main as modernize_main


def test_list_fixers():
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        returncode = modernize_main(["-l"])
    assert returncode == 0
    assert "xrange_six" in stdout.getvalue()


def test_nofix_fixers(tmp_path):
    stdout = io.StringIO()
    stderr = io.StringIO()
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        returncode = modernize_main(["--nofix=ham", str(tmp_path)])

    assert returncode == 2
    assert stderr.getvalue() == "Error: fix 'ham' was not found\n"
    assert stdout.getvalue() == ""


NO_SIX_SAMPLE = """\
a = range(10)

class B(object):
    __metaclass__ = Meta
"""

EXPECTED_SIX_RESULT = """\
from __future__ import absolute_import
import six
from six.moves import range
a = list(range(10))

class B(six.with_metaclass(Meta, object)):
    pass
"""


def test_no_six():
    check_on_input(
        NO_SIX_SAMPLE, NO_SIX_SAMPLE, extra_flags=["--no-six"], expected_return_code=0
    )


def test_enforce():
    check_on_input(
        NO_SIX_SAMPLE,
        EXPECTED_SIX_RESULT,
        extra_flags=["--enforce"],
        expected_return_code=2,
    )
