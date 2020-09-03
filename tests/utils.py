from __future__ import generator_stop

import os.path
import shutil
import tempfile

from libmodernize.main import main as modernize_main


def check_on_input(
    input_content, expected_content, extra_flags=[], expected_return_code=None
):
    """
    Check that input_content is fixed to expected_content, idempotently:
        Writes input_content to a temporary file
        Runs modernize on it with any extra arguments as given in extra_flags
        Runs modernize again with the same arguments, to flush out cumulative effects
            (e.g., 'import' fixer isn't triggered until an import exists)
        Asserts that the resulting file matches expected_content
        Runs modernize again with any extra arguments
        Asserts that the final run makes no changes
    """
    tmpdirname = tempfile.mkdtemp()
    try:
        test_input_name = os.path.join(tmpdirname, "input.py")
        with open(test_input_name, "wt") as input_file:
            input_file.write(input_content)

        def _check(this_input_content, which_check, check_return_code=True):
            return_code = modernize_main(extra_flags + ["-w", test_input_name])

            if check_return_code and expected_return_code is not None:
                if expected_return_code != return_code:
                    raise AssertionError(
                        "Actual return code: %s\nExpected return code: %s"
                        % (return_code, expected_return_code)
                    )

            # Second pass to deal with cumulative effects that affect 'import'
            return_code = modernize_main(extra_flags + ["-w", test_input_name])

            if check_return_code and expected_return_code is not None:
                if expected_return_code != return_code:
                    raise AssertionError(
                        "Actual return code: %s\nExpected return code: %s"
                        % (return_code, expected_return_code)
                    )

            output_content = ""
            with open(test_input_name) as output_file:
                for line in output_file:
                    if line:
                        output_content += line

            if output_content != expected_content:
                raise AssertionError(
                    "%s\nInput:\n%sOutput:\n%s\nExpecting:\n%s"
                    % (
                        which_check,
                        this_input_content,
                        output_content,
                        expected_content,
                    )
                )

        _check(input_content, "output check failed")
        if input_content != expected_content:
            _check(
                expected_content, "idempotence check failed", check_return_code=False
            )
    finally:
        shutil.rmtree(tmpdirname)
