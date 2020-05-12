from __future__ import absolute_import

from fissix.fixes import fix_unicode
from libmodernize import add_future

class FixUnicodeFuture(fix_unicode.FixUnicode):
    def transform(self, node, results):
        res = super(FixUnicodeFuture, self).transform(node, results)
        if res:
            add_future(node, 'unicode_literals')
        return res
