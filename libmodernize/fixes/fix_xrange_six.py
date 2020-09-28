# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.

from __future__ import generator_stop

from fissix import fixer_base, fixer_util
from fissix.fixes import fix_xrange


class FixXrangeSix(fixer_base.ConditionalFix, fix_xrange.FixXrange):

    skip_on = "six.moves.range"

    def transform(self, node, results):
        if self.should_skip(node):
            return
        fixer_util.touch_import("six.moves", "range", node)
        return super().transform(node, results)
