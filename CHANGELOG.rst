Version 0.8rc2-dev
==================

Unreleased.

* add ``modernize`` console_script
* move project to https://github.com/PyCQA/modernize/

Version 0.8rc1
==============

Released 2020-07-20.

* use fissix instead of deprecated lib2to3

Version 0.5-0.7
===============

* Added the opt-in classic_division fixer.
* Updated the ``dict_six`` fixer to support ``six.viewitems()`` and friends.
* New fixer for ``unichr``, changed to ``six.unichr``.
* Documentation corrections.


Version 0.4
===========

Released 2014-10-14.

* `Documentation`_ has been added.
* All fixers are now idempotent, which allows modernize to safely be applied
  more than once to the same source code.
* The option to include default fixers when ``-f`` options are used is now
  spelled ``-f default``, rather than ``-f all``.
* Added a ``--version`` option to the modernize command.
* Calls to ``zip``, ``map``, and ``filter`` are now wrapped with ``list()``
  in non-iterator contexts, to preserve Python 2 semantics.
* Improved fixer for ``xrange`` using ``six.moves.range``.
* Simplified use of ``six.with_metaclass`` for classes with more than
  one base class.
* New fixer for imports of renamed standard library modules, using
  ``six.moves``.
* New fixer to add ``from __future__ import absolute_import`` to all
  files with imports, and change any implicit relative imports to explicit
  (see PEP 328).
* New fixer for ``input()`` and ``raw_input()``, changed to ``eval(input())``
  and ``input()`` respectively.
* New fixer for ``file()``, changed to ``open()``. There is also an
  opt-in fixer that changes both of these to ``io.open()``.
* New fixer for ``(int, long)`` or ``(long, int)``, changed to
  ``six.integer_types``. Other references to ``long`` are changed to ``int``.
* New fixer for ``basestring``, changed to ``six.string_types``.
* New fixer for ``unicode``, changed to ``six.text_type``.
* The ``fix_next`` fixer uses the ``next()`` builtin rather than
  ``six.advance_iterator``.
* There is test coverage for all ``libmodernize`` fixers.
* Simplified the implementation of many ``libmodernize`` fixers by extending
  similar fixers from ``lib2to3``.
* Fixed a bug where ``fix_raise_six`` was adding an incorrect import
  statement.
* Support for targeting Python 2.5 or lower has been officially dropped.
  (Previously some fixers did output constructs that were only added in
  Python 2.6, such as the ``except ... as`` construct, but this was not
  documented.)

.. _Documentation: http://modernize.readthedocs.org/en/latest/


Version 0.3
===========

Released 2014-08-12.

* New fixer for ``raise E, V, T``, changed to ``six.reraise(E, V, T)``.
* New fixer for metaclasses, using ``six.with_metaclass``.
* Avoid adding redundant parentheses to ``print(x)``.
* modernize can now be installed and run on Python 3.
* Fixed a bug where ``__future__`` imports were added multiple times.
* Fixed a bug where fixer for ``zip()`` was recognising ``map()``.
* The default is now to leave Unicode literals unchanged.
  (In previous versions this required the ``--compat-unicode`` option,
  which has now been removed.) A new ``--six-unicode`` option has been
  added to obtain the previous behaviour of adding ``six.u`` wrappers
  around Unicode literals.
