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

from htmlmin import minify as htmlmin
from cssmin import cssmin
from pelican import signals


# We need save unicode strings to files.
if sys.version_info[0] < 3:
    from codecs import open


logger = getLogger(__name__)


def minify(pelican):
    """Minify all HTML and CSS files.

    :param pelican: The Pelican instance.
    """

    for dirpath, _, filenames in walk(pelican.settings['OUTPUT_PATH']):
        for filename in fnmatch.filter(filenames, '*.html'):
            minify_html_file(join(dirpath, filename))
        for filename in fnmatch.filter(filenames, '*.css'):
            minify_css_file(join(dirpath, filename))


def minify_html_file(filename):
    """Create a minified HTML file, overwriting the original.

    :param str filename: The file to minify.
    """

    with open(filename, encoding='utf-8') as f:
        raw = f.read()

    with open(filename, 'w', encoding='utf-8') as f:
        logger.debug('Minifying: %s' % filename)
        f.write(htmlmin(raw))


def minify_css_file(filename):
    """Create a minified CSS file, overwriting the original.

    :param str filename: The file to minify.
    """

    with open(filename, encoding='utf-8') as f:
        raw = f.read()

    with open(filename, 'w', encoding='utf-8') as f:
        logger.debug('Minifying: %s' % filename)
        f.write(cssmin(raw))


def register():
    """Run the HTML minification stuff after all articles have been generated,
    at the very end of the processing loop.
    """
    signals.finalized.connect(minify)
