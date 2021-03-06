try:
    from unittest import TestCase, skip
except ImportError:
    from unittest2 import TestCase, skip

try:
    from unittest import mock
except ImportError:
    import mock

import os
import logging

from anaconda_mode import anaconda


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT = os.path.realpath(BASE_DIR) + os.path.sep

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('anaconda_mode')

if not os.path.isdir(ROOT + 'log'):
    os.mkdir(ROOT + 'log')

handler = logging.FileHandler(ROOT + 'log/test.log')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.propagate = False  # Not echo to console

# Helper methods.


def editor(path, line, column, command):
    """Execute user request."""

    with open(ROOT + path) as f:
        lines = f.readlines()
        source = ''.join(lines)

    request = {
        'command': command,
        'attributes': {
            'source': source,
            'line': line,
            'column': column,
            'path': path,
        }
    }

    return anaconda.process(**request)
