from __future__ import absolute_import

from fissix import fixer_base
from fissix import fixer_util
import libmodernize


class FixBasestring(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """'basestring'"""

    def transform(self, node, results):
        libmodernize.touch_import(None, u'six', node)
        return fixer_util.Name(u'six.string_types', prefix=node.prefix)
