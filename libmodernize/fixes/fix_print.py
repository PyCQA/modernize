from __future__ import absolute_import
from fissix.fixes import fix_print
import libmodernize


class FixPrint(fix_print.FixPrint):

    def transform(self, node, results):
        result = super(FixPrint, self).transform(node, results)
        libmodernize.add_future(node, u'print_function')
        return result
