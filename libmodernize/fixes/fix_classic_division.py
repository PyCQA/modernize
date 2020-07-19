from __future__ import absolute_import

from fissix import fixer_base
from fissix import pytree
from fissix.pgen2 import token

import libmodernize


class FixClassicDivision(fixer_base.BaseFix):
    PATTERN = '''
    '/=' | '/'
    '''

    def start_tree(self, tree, name):
        super(FixClassicDivision, self).start_tree(tree, name)
        self.skip = "division" in tree.future_features

    def match(self, node):
        return node.value in ('/', '/=')

    def transform(self, node, results):
        if self.skip:
            return
        libmodernize.add_future(node, u'division')

        if node.value == '/':
            return pytree.Leaf(token.DOUBLESLASH, '//', prefix=node.prefix)
        else:
            return pytree.Leaf(token.DOUBLESLASHEQUAL, '//=', prefix=node.prefix)
