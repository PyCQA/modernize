from __future__ import generator_stop

from fissix import fixer_base, fixer_util

import libmodernize


class FixIntLongTuple(fixer_base.BaseFix):

    run_order = 4  # Must run before fix_long.

    PATTERN = """
    pair=atom < '(' testlist_gexp < (
        ('int' ',' 'long') |
        ('long' ',' 'int')
    ) > ')' >
    """

    def transform(self, node, results):
        libmodernize.touch_import(None, "six", node)
        pair = results["pair"]
        pair.replace(fixer_util.Name("six.integer_types", prefix=pair.prefix))
