from __future__ import generator_stop

import os
import re

from setuptools import setup

module_file = open(
    os.path.join(os.path.dirname(__file__), "libmodernize", "__init__.py")
).read()
version_match = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", module_file, re.M)
if not version_match:
    raise Exception("couldn't find version number")
version = version_match.group(1)

setup(version=version)
