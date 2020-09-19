from __future__ import generator_stop

from fissix import refactor

from libmodernize import fixes

FISSIX_FIXES_PKG = "fissix.fixes"
LIBMODERNIZE_FIXES_PKG = "libmodernize.fixes"


def check_existence(prefix, module_names):
    """Check that module_names have the expected prefix and exist."""
    dotted_prefix = prefix + "."
    for module_name in module_names:
        if not module_name.startswith(dotted_prefix):
            msg = f"{module_name!r} does not start with {prefix!r}"
            raise AssertionError(msg)
        try:
            __import__(module_name)
        except ImportError:
            raise AssertionError(f"{module_name!r} cannot be imported")


def test_fissix_fix_names():
    check_existence(FISSIX_FIXES_PKG, fixes.fissix_fix_names)


def test_six_fix_names():
    check_existence(LIBMODERNIZE_FIXES_PKG, fixes.six_fix_names)


def test_fixers_importable():
    fixers = refactor.get_fixers_from_package(LIBMODERNIZE_FIXES_PKG)
    for module_name in fixers:
        try:
            __import__(module_name)
        except ImportError:
            raise AssertionError(f"{module_name!r} cannot be imported")
