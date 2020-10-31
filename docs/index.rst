:tocdepth: 3

Modernize
/////////

.. toctree::
   :maxdepth: 2

   fixers


Purpose of the project
======================

Modernize is a Python program that reads Python 2 source code
and applies a series of fixers to transform it into source code
that is valid on both Python 3 and Python 2.7.

This allows you to run your test suite on Python 2.7 and Python 3
so you can gradually port your code to being fully Python 3
compatible without slowing down development of your Python 2
project.

The ``python -m modernize`` command works like
``python -m fissix``, see `fissix <https://github.com/jreese/fissix>`_.
Here's how you'd rewrite a
single file::

    python -m modernize -w example.py

It does not guarantee, but it attempts to spit out a codebase compatible
with Python 2.6+ or Python 3. The code that it generates has a runtime
dependency on `six <https://pypi.python.org/pypi/six>`_, unless the
``--no-six`` option is used. Version 1.9.0 or later of ``six`` is
recommended. Some of the fixers output code that is not compatible with
Python 2.5 or lower.

Once your project is ready to run in production on Python 3 it's
recommended to drop Python 2.7 support using
`pyupgrade <https://pypi.org/project/pyupgrade/>`_

See the ``LICENSE`` file for the license of ``modernize``.
Using this tool does not affect licensing of the modernized code.

This library is a very thin wrapper around `fissix
<https://github.com/jreese/fissix>`_, a fork of lib2to3.

The `project website`_ can be found on GitHub and the PyPI project name is
modernize_

A note about handling text literals
===================================

.. TODO Explain what a "native string" is if it is going to be referenced

- By default modernize does not change Unicode literals at all, which means that
  you can take advantage of
  `PEP 414 <https://www.python.org/dev/peps/pep-0414/>`_.
  This is the simplest option if you only want to support Python 3.3 and above
  along with Python 2.
- Alternatively, there is the ``--six-unicode`` flag which will wrap Unicode
  literals with the six helper function ``six.u()`` using the
  ``modernize.fixes.fix_unicode`` fixer. This is useful if you want
  to support Python 3.1 and Python 3.2 without bigger changes.
- The last alternative is the ``--future-unicode`` flag which
  imports the ``unicode_literals`` from the ``__future__`` module using the
  ``modernize.fixes.fix_unicode_future`` fixer.
  This requires Python 2.6 and later, and will require that you
  mark bytestrings with ``b''`` and native strings in ``str('')``
  or something similar that survives the transformation.

Indices and tables
//////////////////

* :ref:`genindex`
* :ref:`search`


.. _modernize: https://pypi.python.org/pypi/modernize
.. _project website: https://github.com/pycqa/modernize
