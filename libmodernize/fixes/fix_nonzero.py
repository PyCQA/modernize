"""Fixer for `__nonzero__` -> `__bool__`, adding an alias for PY2 compatibility.

Based on Lib/lib2to3/fixes/fix_nonzero.py.

"""
# This is a derived work of Lib/lib2to3/fixes/fix_nonzero.py. That file
# is under the copyright of the Python Software Foundation and licensed
# under the Python Software Foundation License 2.
#
# Copyright notice:
#
#     2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
#     2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020
#     Python Software Foundation; All Rights Reserved.

# Author: Collin Winter, James Bowman

from __future__ import absolute_import
from lib2to3 import fixer_base
from lib2to3.fixer_util import Assign, Dot, find_indentation, Leaf, Name, Newline, Node, syms
from lib2to3.pygram import token
import libmodernize


class FixNonzero(fixer_base.BaseFix):
    BM_compatible = True

    PATTERN = """
    classdef< 'class' any+ ':'
              suite< any*
                     funcdef< 'def' name='__nonzero__'
                              parameters< '(' NAME ')' > any+ >
                     any* > >
    """

    def transform(self, node, results):
        # Start by making the same transformation as lib2to3.fix_nonzero, purely
        # renaming the method:

        name = results["name"]
        bool_funcdef = name.parent
        new_name = Name("__bool__", prefix=name.prefix)
        name.replace(new_name)

        # Then, import six and add a conditional PY2-enabled function alias:

        libmodernize.touch_import(None, u'six', node)

        suite = bool_funcdef.parent
        bool_funcdef_suite = bool_funcdef.children[-1]
        old_dedent = bool_funcdef_suite.children[-1]
        new_dedent = Leaf(token.DEDENT, '', prefix='\n' + find_indentation(bool_funcdef))
        bool_funcdef_suite.children[-1].replace(new_dedent)

        reassignment = Node(syms.suite, [
            Newline(),
            Leaf(token.INDENT,
                 find_indentation(bool_funcdef.children[-1].children[1])),
            Node(syms.simple_stmt,
                 [Assign(Name('__nonzero__'), Name('__bool__')),
                  Newline()]), old_dedent
        ])

        if_stmt = Node(syms.if_stmt, [
            Name('if'),
            Node(syms.power,
                 [Name(' six'),
                  Node(syms.trailer, [Dot(), Name('PY2')])]),
            Leaf(token.COLON, ':'), reassignment
        ])

        suite.insert_child(suite.children.index(bool_funcdef) + 1, if_stmt)
