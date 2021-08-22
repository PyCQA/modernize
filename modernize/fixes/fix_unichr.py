from __future__ import generator_stop

from fissix import fixer_base, fixer_util
from fissix.fixer_util import is_probably_builtin


class FixUnichr(fixer_base.ConditionalFix):
    BM_compatible = True

    skip_on = "six.moves.unichr"
    PATTERN = """'unichr'"""

    def transform(self, node, results):
        if self.should_skip(node):
            return  # pragma: no cover
        if is_probably_builtin(node):
            fixer_util.touch_import("six", "unichr", node)
