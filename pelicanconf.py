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
SITESUBTITLE = 'elegance maker'

SITEURL = 'http://jiayi.ideaera.com'

TIMEZONE = 'Asia/Taipei'

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DISPLAY_CATEGORIES_ON_MENU = False

# OUTPUT_RETENTION = ('.git')
RELATIVE_URLS = True
PYGMENTS_RST_OPTIONS = {'linenos': 'none'}  # 'linenos': 'table'

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

FEED_ATOM = 'feeds/atom.xml'
#FEED_ALL_ATOM = 'feeds/all.atom.xml'

LINKS = ()
SOCIAL = ()

GOOGLE_ANALYTICS = 'UA-49479618-1'


# ==========================================================
THEME = 'theme/pelican-elegant'

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))  # add search, 404

PLUGIN_PATH = 'plugin'
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']

SITEMAP = {
    'format': 'xml',
}

