from __future__ import absolute_import

import io
import os.path
import tempfile
import shutil
import sys

PY3 = sys.version_info[0] >= 3

from libmodernize.main import main as modernize_main


def check_on_input(input_content, expected_content, extra_flags = [],
                    write_newline=None, read_newline=None):
    """
    Check that input_content is fixed to expected_content, idempotently.

    Writes input_content to a temporary file, runs modernize on it with any
    extra arguments as given in extra_flags, and asserts that the resulting file
    matches expected_content. Then, runs modernize again with any extra arguments,
    and asserts that the second run makes no changes.
    """
    if not PY3 and isinstance(input_content, bytes):
        # Allow native strings as input on Python 2
        input_content = input_content.decode('ascii')

    tmpdirname = tempfile.mkdtemp()
    try:
        test_input_name = os.path.join(tmpdirname, "input.py")
        with io.open(test_input_name, "wt", newline=write_newline) as input_file:
            input_file.write(input_content)

        def _check(this_input_content, which_check):
            modernize_main(extra_flags + ["-w", test_input_name])

            output_content = ""
            with io.open(test_input_name, "rt", newline=read_newline) as output_file:
                for line in output_file:
                    if line:
                        output_content += line

            if output_content != expected_content:
                raise AssertionError("%s\nInput:\n%sOutput:\n%s\nExpecting:\n%s" %
                                     (which_check, this_input_content, output_content, expected_content))

        _check(input_content, "output check failed")
        if input_content != expected_content:
            _check(expected_content, "idempotence check failed")
    finally:
        shutil.rmtree(tmpdirname)

def expect_error(input_content, extra_flags=[]):
    tmpdirname = tempfile.mkdtemp()
    try:
        test_input_name = os.path.join(tmpdirname, "input.py")
        with open(test_input_name, "wt") as input_file:
            input_file.write(input_content)

        ret = modernize_main(extra_flags + ["-w", test_input_name])
        if ret == 0:
            raise AssertionError("didn't expect to succeed")
    finally:
        shutil.rmtree(tmpdirname)
