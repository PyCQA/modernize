from __future__ import generator_stop

from fissix.fixes import fix_unicode

import libmodernize


class FixUnicodeFuture(fix_unicode.FixUnicode):
    def transform(self, node, results):
        res = super().transform(node, results)
        if res:
            libmodernize.add_future(node, "unicode_literals")
        return res
