# encoding: utf-8

from __future__ import unicode_literals

AUTHOR = 'Shrikant Sharat Kandula'
SITENAME = '(shrikant-sharat)'
SITEURL = '.'

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/all.atom.xml'

DIRECT_TEMPLATES = [
    'index',
    'tags',
    # 'categories',
    'archives',
    'labs',
    'about',
]

TIMEZONE = 'Asia/Kolkata'
DEFAULT_DATE_FORMAT = '%d %b, %Y'
DATE_FORMATS = {
    'en': '%d %b, %Y',
}

# Markdown extensions at http://pythonhosted.org/Markdown/extensions/index.html
MD_EXTENSIONS = 'extra codehilite toc sane_lists'.split()

PLUGINS = 'minify'.split()

DISQUS_SITENAME = 'sharats-me'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = False

THEME = 'theme'

# TODO: Typogrify depends on Django. Cut it and then use it.
# TYPOGRIFY = True

TWITTER_USERNAME = 'sharat87'

MENUITEMS = [
    ('About', 'about.html'),
    ('Labs', 'labs.html'),
    ('Archives', 'archives.html'),
    ('Tags', 'tags.html'),
    ('Atom Feed', FEED_ATOM),
]

# Blogroll
LINKS = [
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    ('Jinja2', 'http://jinja.pocoo.org'),
]

# Social widget
SOCIAL = [
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
]

# Labs, along with their descriptions to be listed on the homepage. Triplets
# of (`name`, `url`, `description`).
LABS = [
    ('antigen', 'http://github.com/zsh-users/antigen',
        '''A plugin manager for zsh, inspired by oh-my-zsh and vundle.'''),

    ('virtualenvman', 'http://github.com/sharat87/virtualenvman',
        '''A lightweight alternative to virtualenvwrapper.'''),

    ('keyboard-fu', 'http://github.com/sharat87/keyboard-fu',
        '''A chrome extension for all powerful hotkeys.'''),

    ('ti', 'http://github.com/sharat87/ti',
        '''A simple light weight command line time tracker (currently in under
        150 lines of bash).'''),

    ('scrite', 'http://github.com/sharat87/scrite',
        '''A tool to regularly take screenshots and save them, to help me see
        what the hell I've been doing all day.'''),

    ('classypants', 'http://github.com/sharat87/classypants',
        '''A tool to visualise PATH like environment variables, filter ones that
        exist, search through them, search inside them, and other goodness.'''),

    ('zsh-vim-mode', 'http://github.com/sharat87/zsh-vim-mode',
        '''Sane bindings for zsh's vi mode so it behaves more vim like.'''),

    ('mastered-minds', 'http://github.com/sharat87/mastered-minds',
        '''A chrome app, a clone of the masterminds game.'''),

    ('lightaby', 'http://github.com/sharat87/lightaby',
        '''A simple lights-off game written using the LÖVE-2D engine for
        Lua.'''),

    ('figs', 'http://github.com/sharat87/figs',
        '''Figs is a library for reading ini like configuration files easily.
        Figs leverages the ConfigParser module from python's standard
        libraries.'''),

    ('PypMsg', 'http://github.com/sharat87/PypMsg',
        '''A simple cross-platform LAN file sharing utility. Inspired by
        ipmsg.'''),

]
