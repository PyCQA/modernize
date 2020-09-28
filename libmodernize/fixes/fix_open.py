from __future__ import generator_stop

from fissix import fixer_base, fixer_util


class FixOpen(fixer_base.BaseFix):

    BM_compatible = True
    # Fixers don't directly stack, so make sure the 'file' case is covered.
    PATTERN = """
    power< ('open' | 'file') trailer< '(' any+ ')' > >
    """

    def transform(self, node, results):
        fixer_util.touch_import("io", "open", node)
