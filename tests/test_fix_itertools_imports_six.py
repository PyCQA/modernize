from __future__ import generator_stop

from utils import check_on_input

IZIP_AND_CHAIN_REFERENCE = (
    """\
from itertools import izip_longest, chain
izip_longest([1, 2], [1])
""",
    """\
from __future__ import absolute_import
from itertools import chain
from six.moves import zip_longest
zip_longest([1, 2], [1])
""",
)

REMOVE_ITERTOOLS_REFERENCE = (
    """\
from itertools import izip
izip([1, 2], [1])
""",
    """\
from __future__ import absolute_import

from six.moves import zip
zip([1, 2], [1])
""",
)

IMAP_TO_MAP_MODULE_IMPORT = (
    """\
import itertools
itertools.imap(lambda x: x * 2, [1, 2])
""",
    """\
from __future__ import absolute_import
import itertools
from six.moves import map
map(lambda x: x * 2, [1, 2])
""",
)


def test_izip_longest_and_chain():
    check_on_input(*IZIP_AND_CHAIN_REFERENCE)


def test_removes_import_line():
    check_on_input(*REMOVE_ITERTOOLS_REFERENCE)


def test_imap_to_map_module_import():
    check_on_input(*IMAP_TO_MAP_MODULE_IMPORT)
