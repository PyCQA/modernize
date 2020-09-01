from __future__ import generator_stop

from utils import check_on_input

NO_IMPORTS = (
    """\
""",
    """\
""",
)

ONLY_FUTURE_IMPORTS = (
    """\
from __future__ import print_function
""",
    """\
from __future__ import print_function
""",
)

ONLY_NORMAL_IMPORTS = (
    """\
import foo
""",
    """\
from __future__ import absolute_import
import foo
""",
)

NORMAL_AND_FUTURE_IMPORTS = (
    """\
from __future__ import print_function
import foo
""",
    """\
from __future__ import print_function
from __future__ import absolute_import
import foo
""",
)

DOCSTRING = (
    """\
\"""
Docstring
\"""
import foo
""",
    """\
\"""
Docstring
\"""
from __future__ import absolute_import
import foo
""",
)

SHEBANG = (
    """\
#!/usr/bin/env python
import foo
""",
    """\
#!/usr/bin/env python
from __future__ import absolute_import
import foo
""",
)

DOCSTING_AND_SHEBANG = (
    """\
#!/usr/bin/env python
\"""
Docstring
\"""
import foo
""",
    """\
#!/usr/bin/env python
\"""
Docstring
\"""
from __future__ import absolute_import
import foo
""",
)

COPYRIGHT_AND_SHEBANG = (
    """\
#!/usr/bin/env python

#
# Copyright notice
#

import foo
""",
    """\
#!/usr/bin/env python

#
# Copyright notice
#

from __future__ import absolute_import
import foo
""",
)


COPYRIGHT_AND_DOCSTRING = (
    """\
#
# Copyright notice
#

\"""Docstring\"""

import foo
""",
    """\
#
# Copyright notice
#

\"""Docstring\"""

from __future__ import absolute_import
import foo
""",
)


def test_no_imports():
    check_on_input(*NO_IMPORTS)


def test_only_future_imports():
    check_on_input(*ONLY_FUTURE_IMPORTS)


def test_only_normal_imports():
    check_on_input(*ONLY_NORMAL_IMPORTS)


def test_normal_and_future_imports():
    check_on_input(*NORMAL_AND_FUTURE_IMPORTS)


def test_import_with_docstring():
    check_on_input(*DOCSTRING)


def test_import_with_shebang():
    check_on_input(*SHEBANG)


def test_import_with_docstring_and_shebang():
    check_on_input(*DOCSTING_AND_SHEBANG)


def test_import_with_copyright_and_shebang():
    check_on_input(*COPYRIGHT_AND_SHEBANG)


def test_import_with_copyright_and_docstring():
    check_on_input(*COPYRIGHT_AND_DOCSTRING)
