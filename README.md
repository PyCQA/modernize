```
  Python           _              _        
     _ __  ___  __| |___ _ _ _ _ (_)______ 
    | '  \/ _ \/ _` / -_) '_| ' \| |_ / -_)
    |_|_|_\___/\__,_\___|_| |_||_|_/__\___|
```

This library is a very thin wrapper around `lib2to3` to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

It does not guarantee, but it attempts to spit out a Python 2/3
compatible codebase.  The code that it generates has a runtime
dependency on `six`, unless the `--no-six` option is used.


##Unicode Literal Control:

- By default modernize will wrap literals with the six helpers.
  This is useful if you want to support Python 3.1 and Python 3.2
  without bigger changes.
- Alternatively there is the ``--compat-unicode`` flag which
  does not change unicode literals at all which means that you
  can take advantage of PEP 414.
- The last alternative is the ``--future-unicode`` flag which
  imports the ``unicode_literals`` from the ``__future__`` module.
  This requires Python 2.6 and later and will require that you
  mark bytestrings with ``b''`` and native strings in ``str(b'')``
  or something similar that survives the transformation.


[![Build Status](https://travis-ci.org/python-modernize/python-modernize.png)](https://travis-ci.org/python-modernize/python-modernize)
