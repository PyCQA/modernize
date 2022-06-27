from fissix import fixer_base, fixer_util


class FixUnicodeType(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """'unicode'"""

    def transform(self, node, results):
        fixer_util.touch_import(None, "six", node)
        return fixer_util.Name("six.text_type", prefix=node.prefix)
