"""Replace sha and md5 with hashlib."""

from __future__ import absolute_import
from lib2to3 import fixer_base


class FixShaMd5(fixer_base.BaseFix):

    import_found = False

    PATTERN = """
        import_name< 'import' (modulename='sha' | modulename='md5') >
        |
        power< sha='sha' trailer< '.' (new='new' | new='sha') > trailer< '(' [any] ')' > [trailer<  '.' any > trailer< '(' ')' >] >
        |
        power< md5='md5' trailer< '.' (new='new' | new='md5') > trailer< '(' [any] ')' > [trailer<  '.' any > trailer< '(' ')' >] >
        """

    def transform(self, node, results):
        if 'modulename' in results:
            node = results['modulename']
            node.value = 'hashlib'
            node.changed()
            self.import_found = True
        if not self.import_found:
            return  # only fix names if we've imported them.
        if 'sha' in results:
            node = results['sha']
            node.value = 'hashlib'
            node.changed()
            if 'new' in results:
                node = results['new']
                node.value = 'sha1'
                node.changed()
        if 'md5' in results:
            node = results['md5']
            node.value = 'hashlib'
            node.changed()
            if 'new' in results:
                node = results['new']
                node.value = 'md5'
                node.changed()

