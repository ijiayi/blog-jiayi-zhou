#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jiayi Zhou'
SITENAME = u'Jiayi Zhou'
#SITEURL = 'http://jiayi.ideaera.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# ==========================================================
AUTHOR = u'Jiayi Zhou'
SITENAME = u'Jiayi Zhou'
SITEURL = 'http://jiayi.ideaera.com'

TIMEZONE = 'Asia/Taipei'

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DISPLAY_CATEGORIES_ON_MENU = False

# OUTPUT_RETENTION = ('.git')
RELATIVE_URLS = True
PYGMENTS_RST_OPTIONS = {'linenos': 'none'}  # 'linenos': 'table'

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

STATIC_PATHS = ['images', 'extra/hello.txt']
EXTRA_PATH_METADATA = {
    'extra/hello.txt': {'path': 'hello.txt'},
}

FEED_ATOM = 'feeds/atom.xml'
#FEED_ALL_ATOM = 'feeds/all.atom.xml'


# ==========================================================
# Theme

SITESUBTITLE = 'elegance maker'

LINKS = ()
SOCIAL = ()

THEME = 'pelican-bootstrap3'
THEME = 'pelican-simplegrey'
THEME = 'plumage'
