from __future__ import absolute_import

import sys
import os.path
import tempfile
import shutil

from libmodernize.main import main as modernize_main


def check_on_input(input_content, expected_content, extra_flags=[], mode="t"):
    """
    Check that input_content is fixed to expected_content, idempotently.

    Writes input_content to a temporary file, runs modernize on it with any
    extra arguments as given in extra_flags, and asserts that the resulting file
    matches expected_content. Then, runs modernize again with any extra arguments,
    and asserts that the second run makes no changes.
    """
    tmpdirname = tempfile.mkdtemp()
    try:
        test_input_name = os.path.join(tmpdirname, "input.py")
        with open(test_input_name, "w" + mode) as input_file:
            input_file.write(input_content)

        def _check(this_input_content, which_check):
            ret = modernize_main(extra_flags + ["-w", test_input_name])
            if ret != 0:
                raise AssertionError("didn't expect to fail (returned %r)" % (ret,))

            with open(test_input_name, "r" + mode) as output_file:
                if mode == "b":
                    output_content = output_file.read()
                else:
                    output_content = "".join([line for line in output_file if line])

            if output_content != expected_content:
                fmt = "%r" if mode == "b" else "%s"
                raise AssertionError(("%s\nInput:\n"+fmt+"\nOutput:\n"+fmt+"\nExpecting:\n"+fmt) %
                                     (which_check, this_input_content, output_content, expected_content))

        _check(input_content, "output check failed")
        if input_content != expected_content:
            _check(expected_content, "idempotence check failed")
    finally:
        shutil.rmtree(tmpdirname)


def expect_error(input_content, extra_flags=[], mode="t"):
    tmpdirname = tempfile.mkdtemp()
    try:
        test_input_name = os.path.join(tmpdirname, "input.py")
        with open(test_input_name, "w" + mode) as input_file:
            input_file.write(input_content)

        ret = modernize_main(extra_flags + ["-w", test_input_name])
        if ret == 0:
            raise AssertionError("didn't expect to succeed")
    finally:
        shutil.rmtree(tmpdirname)
