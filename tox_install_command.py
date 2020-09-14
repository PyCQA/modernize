from __future__ import generator_stop

import contextlib
import hashlib
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile


class _Hashfile:
    def __init__(self, update):
        self.write = update


def hash_file(f):
    hasher = hashlib.sha256()
    shutil.copyfileobj(f, _Hashfile(hasher.update))
    return f"--hash=sha256:{hasher.hexdigest()}"


_EXTRAS_RE = re.compile(r"\[[^\]]*\]\Z")


def maybe_hash_path_requirement(arg):
    """
    Hash a requirement if it looks like a path and return it.

    otherwise return None.
    """
    if os.sep not in arg:
        return None

    fixed_path = pathlib.Path(_EXTRAS_RE.sub(string=arg, repl=""))
    with contextlib.ExitStack() as stack:
        try:
            f = stack.enter_context(fixed_path.open(mode="rb"))
        except FileNotFoundError:
            return None
        return f"{arg} {hash_file(f)}"


@contextlib.contextmanager
def tmp_path(*args, **kwargs):
    with tempfile.TemporaryDirectory(*args, **kwargs) as tmp:
        yield pathlib.Path(tmp)


@contextlib.contextmanager
def tmp_requirements(hashed_reqs):
    with tmp_path(suffix=__spec__.name) as tmp:
        requirements = tmp / "requirements.txt"
        requirements.write_text(hashed_reqs)
        yield ("-r", os.fsdecode(requirements))


def main(argv=sys.argv):
    _prog, *args = argv
    processed_args = [(arg, maybe_hash_path_requirement(arg)) for arg in args]
    hashed_reqs = "\n".join(hashed for _, hashed in processed_args if hashed)
    # pip considers a duplicate requirement without a `--hash` as all duplicates
    # missing hashes
    not_hashed_reqs = [arg for (arg, hashed) in processed_args if not hashed]

    with contextlib.ExitStack() as stack:
        requirements = (
            stack.enter_context(tmp_requirements(hashed_reqs)) if hashed_reqs else ()
        )
        # pip does not process `--hash` args unless in a requirements.txt
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--require-hashes",
                *requirements,
                *not_hashed_reqs,
            ],
            check=True,
        )


if __name__ == "__main__":
    sys.exit(main())
