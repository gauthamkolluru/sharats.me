# encoding: utf-8

"""A Pelican plugin which minifies HTML pages.

Original from https://github.com/rdegges/pelican-minify/blob/master/minify.py
"""


from __future__ import print_function
from __future__ import unicode_literals

from logging import getLogger
from os import walk
from os.path import join
import fnmatch
import sys

from htmlmin import minify
from pelican import signals


# We need save unicode strings to files.
if sys.version_info[0] < 3:
    from codecs import open


logger = getLogger(__name__)


def minify_html(pelican):
    """Minify all HTML files.

    :param pelican: The Pelican instance.
    """
    for dirpath, _, filenames in walk(pelican.settings['OUTPUT_PATH']):
        for filename in fnmatch.filter(filenames, '*.html'):
            create_minified_file(join(dirpath, filename))


def create_minified_file(filename):
    """Create a minified HTML file, overwriting the original.

    :param str filename: The file to minify.
    """

    with open(filename, encoding='utf-8') as f:
        raw = f.read()

    with open(filename, 'w', encoding='utf-8') as f:
        logger.debug('Minifying: %s' % filename)
        f.write(minify(raw))


def register():
    """Run the HTML minification stuff after all articles have been generated,
    at the very end of the processing loop.
    """
    signals.finalized.connect(minify_html)
