# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.


from fissix import fixer_util
from fissix.fixes import fix_filter

from .. import utils


class FixFilter(fix_filter.FixFilter):
    skip_on = "six.moves.filter"

    def transform(self, node, results):
        result = super().transform(node, results)
        if not utils.is_listcomp(result):
            # Keep performance improvement from six.moves.filter in iterator
            # contexts on Python 2.7.
            fixer_util.touch_import("six.moves", "filter", node)
        return result
