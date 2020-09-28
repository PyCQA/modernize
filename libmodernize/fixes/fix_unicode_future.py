from __future__ import generator_stop

from fissix.fixes import fix_unicode

from .. import utils


class FixUnicodeFuture(fix_unicode.FixUnicode):
    def transform(self, node, results):
        res = super().transform(node, results)
        if res:
            utils.add_future(node, "unicode_literals")
        return res
