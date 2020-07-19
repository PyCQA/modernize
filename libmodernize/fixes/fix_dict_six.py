"""Fixer for iterkeys() -> six.iterkeys(), and similarly for iteritems and itervalues."""
from __future__ import absolute_import

# Local imports
from fissix import fixer_util
from fissix import pytree
from fissix.fixes import fix_dict
import libmodernize


class FixDictSix(fix_dict.FixDict):

    def transform_iter(self, node, results):
        """Call six.(iter|view)items() and friends."""
        # Make sure six is imported.
        libmodernize.touch_import(None, u'six', node)

        # Copy of self.transform() from fissix.fix_dict with some changes to
        # use the six.* methods.

        head = results['head']
        method = results['method'][0] # Extract node for method name
        tail = results['tail']
        syms = self.syms
        method_name = method.value
        name = fixer_util.Name(u'six.' + method_name, prefix=node.prefix)
        assert method_name.startswith((u'iter', u'view')), repr(method)
        assert method_name[4:] in (u'keys', u'items', u'values'), repr(method)
        head = [n.clone() for n in head]
        tail = [n.clone() for n in tail]
        new = pytree.Node(syms.power, head)
        new.prefix = u''
        new = fixer_util.Call(name, [new])
        if tail:
            new = pytree.Node(syms.power, [new] + tail)
        new.prefix = node.prefix
        return new

    def transform(self, node, results):
        method = results['method'][0]
        method_name = method.value
        if method_name in ('keys', 'items', 'values'):
            return super(FixDictSix, self).transform(node, results)
        else:
            return self.transform_iter(node, results)

    def in_special_context(self, node, isiter):
        # Redefined from parent class to make "for x in d.items()" count as
        # in special context; 2to3 only counts for loops as special context
        # for the iter* methods.
        return super(FixDictSix, self).in_special_context(node, True)
