Fixers
======

Fixers come in two types: Default_ and Opt-in_. Default fixers should not break
code except for corner cases, and are idempotent (applying them more than once
to given source code will make no changes after the first application). Opt-in
fixers are allowed to break these rules.

Python 2 code from Python 2.6 and older will be upgraded to code that is
compatible with Python 2.6, 2.7, and Python 3.

If code is using a feature unique to Python 2.7, it will not be downgraded to
work with Python 2.6. For example, ``dict.viewitems()`` usage will not be
removed to make the code compatible with Python 2.6.

Some fixers rely on the latest release of the `six project`_ to work
(see `Fixers requiring six`_).
If you wish to turn off these fixers to avoid an external dependency on ``six``,
then use the ``--no-six`` flag.

Fixers use the API defined by fissix. For details of how this works, and how to
implement your own fixers, see `Creating a fixer, at python3porting.com
<https://web.archive.org/web/20200903114908/python3porting.com/fixers.html#creating-a-fixer>`_.
``python -m modernize`` will try to load fixers whose full dotted-path is specified
as a ``-f`` argument, but will fail if they are not found. By default, fixers
will not be found in the current directory; use ``--fixers-here`` to make
``python -m modernize`` look for them there, or see the `Python tutorial on
modules <https://docs.python.org/3/tutorial/modules.html>`_ (in particular,
the parts on the `search path
<https://docs.python.org/3/tutorial/modules.html#the-module-search-path>`_
and `packages <https://docs.python.org/3/tutorial/modules.html#packages>`_)
for more info on how Python finds modules.


Default
-------

A default fixer will be enabled when:

- Either no ``-f``/``--fix`` options are used, or ``-f default``/``--fix=default``
  is used, or the fixer is listed explicitly in an ``-f``/``--fix`` option; and
- The fixer is not listed in an ``-x``/``--nofix`` option; and
- For fixers that are dependent on the `six project`_, ``--no-six`` is *not* specified
  (see `Fixers requiring six`_).

The ``-x``/``--nofix`` and ``--no-six`` options always override fixers specified
using ``-f``/``--fix``. The ``--six-unicode`` and ``--future-unicode`` options
also disable fixers that are not applicable for those options.


Fixers requiring six
++++++++++++++++++++

The `six project`_ provides the ``six`` module which contains various tidbits in
helping to support Python 2/3 code. All ``six``-related fixers assume the latest
version of ``six`` is installed.

.. attribute:: basestring

   Replaces all references to :func:`basestring` with :data:`six.string_types`.

   .. versionadded:: 0.4

.. attribute:: dict_six

   Fixes various methods on the ``dict`` type for getting all keys, values, or
   items. E.g.::

       x.values()
       x.itervalues()
       x.viewvalues()

   becomes::

       list(x.values())
       six.itervalues(x)
       six.viewvalues(x)

   Care is taken to only call ``list()`` when not in an iterating context
   (e.g. not the iterable for a ``for`` loop).

.. attribute:: filter

   When a call to :func:`filter <python2:filter>` is discovered, ``from six.moves import filter`` is
   added to the module. Wrapping the use in a call to ``list()`` is done when
   necessary.

.. attribute:: imports_six

   Uses :mod:`six.moves` to fix various renamed modules, e.g.::

       import ConfigParser
       ConfigParser.ConfigParser()

   becomes::

       import six.moves.configparser
       six.moves.configparser.ConfigParser()

   The modules in Python 2 whose renaming in Python 3 is supported are:

   - ``__builtin__``
   - ``_winreg``
   - ``BaseHTTPServer``
   - ``CGIHTTPServer``
   - ``ConfigParser``
   - ``copy_reg``
   - ``Cookie``
   - ``cookielib``
   - ``cPickle``
   - ``Dialog``
   - ``dummy_thread``
   - ``FileDialog``
   - ``gdbm``
   - ``htmlentitydefs``
   - ``HTMLParser``
   - ``httplib``
   - ``Queue``
   - ``repr``
   - ``robotparser``
   - ``ScrolledText``
   - ``SimpleDialog``
   - ``SimpleHTTPServer``
   - ``SimpleXMLRPCServer``
   - ``SocketServer``
   - ``thread``
   - ``Tix``
   - ``tkColorChooser``
   - ``tkCommonDialog``
   - ``Tkconstants``
   - ``Tkdnd``
   - ``tkFileDialog``
   - ``tkFont``
   - ``Tkinter``
   - ``tkMessageBox``
   - ``tkSimpleDialog``
   - ``ttk``
   - ``xmlrpclib``

   .. versionadded:: 0.4

.. attribute:: input_six

   Changes::

       input(x)
       raw_input(x)

   to::

       from six.moves import input
       eval(input(x))
       input(x)

   .. versionadded:: 0.4

.. attribute:: int_long_tuple

   Changes ``(int, long)`` or ``(long, int)`` to :data:`six.integer_types`.

   .. versionadded:: 0.4

.. attribute:: map

   If a call to :func:`map <python2:map>` is discovered, ``from six.moves import map`` is added to
   the module. Wrapping the use in a call to ``list()`` is done when necessary.

.. attribute:: metaclass

   Changes::

       class Foo:
           __metaclass__ = Meta

   to::

       import six
       class Foo(six.with_metaclass(Meta)):
           pass

   .. seealso::
      :func:`six.with_metaclass`

.. attribute:: raise_six

   Changes ``raise E, V, T`` to ``six.reraise(E, V, T)``.

.. attribute:: unicode_type

   Changes all reference of :func:`unicode <python2:unicode>` to
   :data:`six.text_type`.

.. attribute:: urllib_six

   Changes::

       from urllib import quote_plus
       quote_plus('hello world')

   to::

       from six.moves.urllib.parse import quote_plus
       quote_plus('hello world')

.. attribute:: unichr

   Changes all reference of :func:`unichr <python2:unichr>` to
   :data:`six.unichr`.

.. attribute:: xrange_six

   Changes::

       w = xrange(x)
       y = range(z)

   to::

       from six.moves import range
       w = range(x)
       y = list(range(z))

   Care is taken not to call ``list()`` when ``range()`` is used in an iterating
   context.

.. attribute:: zip

   If :func:`zip <python2:zip>` is called, ``from six.moves import zip`` is added to the module.
   Wrapping the use in a call to ``list()`` is done when necessary.


``fissix`` fixers
+++++++++++++++++

Some :doc:`fixers from fissix <fissix:fixers>`
in Python's standard library are run by default unmodified as their
transformations are Python 2 compatible.

- :attr:`apply <fissix:apply>`
- :attr:`except <fissix:except>`
- :attr:`exec <fissix:exec>`
- :attr:`execfile <fissix:execfile>`
- :attr:`exitfunc <fissix:exitfunc>`
- :attr:`funcattrs <fissix:funcattrs>`
- :attr:`has_key <fissix:has_key>`
- :attr:`idioms <fissix:idioms>`
- :attr:`long <fissix:long>`
- :attr:`methodattrs <fissix:methodattrs>`
- :attr:`ne <fissix:ne>`
- :attr:`numliterals <fissix:numliterals>`
- :attr:`operator <fissix:operator>`
- :attr:`paren <fissix:paren>`
- :attr:`reduce <fissix:reduce>`
- :attr:`repr <fissix:repr>`
- :attr:`set_literal <fissix:set_literal>`
- :attr:`standarderror <fissix:standarderror>`
- :attr:`sys_exc <fissix:sys_exc>`
- :attr:`throw <fissix:throw>`
- :attr:`tuple_params <fissix:tuple_params>`
- :attr:`types <fissix:types>`
- :attr:`ws_comma <fissix:ws_comma>`
- :attr:`xreadlines <fissix:xreadlines>`

Fixers with no dependencies
+++++++++++++++++++++++++++

.. attribute:: file

   Changes all calls to :func:`file <python2:file>` to :func:`open <python2:open>`.

   .. versionadded:: 0.4

.. attribute:: import

   Changes implicit relative imports to explicit relative imports and adds
   ``from __future__ import absolute_import``.

   .. versionadded:: 0.4

.. attribute:: next

   Changes all method calls from ``x.next()`` to ``next(x)``.

.. attribute:: print

   Changes all usage of the ``print`` statement to use the :func:`print` function
   and adds ``from __future__ import print_function``.

.. attribute:: raise

   Changes comma-based ``raise`` statements from::

       raise E, V
       raise (((E, E1), E2), E3), V

   to::

       raise E(V)
       raise E(V)


Opt-in
------

To specify an opt-in fixer while also running all the default fixers, make sure
to specify the ``-f default`` or ``--fix=default`` option, e.g.::

    python -m modernize -f default -f libmodernize.fixes.fix_open

.. attribute:: classic_division

   When a use of the division operator -- ``/`` -- is found, add
   ``from __future__ import division`` and change the operator to ``//``.
   If ``from __future__ import division`` is already present, this fixer is
   skipped.

   This is intended for use in programs where ``/`` is conventionally only used
   for integer division, or where it is intended to do a manual pass after running
   ``python -m modernize`` to look for cases that should not have been changed to ``//``.
   The results of division on non-integers may differ after running this fixer:
   for example, ``3.5 / 2 == 1.75``, but ``3.5 // 2 == 1.0``.

   Some objects may override the ``__div__`` method for a use other than division,
   and thus would break when changed to use a ``__floordiv__`` method instead.

   This fixer is opt-in because it may change the meaning of code as described
   above.

   .. versionadded:: 1.0

.. attribute:: open

   When a call to :func:`open <python2:open>` is discovered, add ``from io import open`` at the top
   of the module so as to use :func:`io.open` instead. This fixer is opt-in because it
   changes what object is returned by a call to ``open()``.

   .. versionadded:: 0.4

.. _six project: https://six.readthedocs.io/
