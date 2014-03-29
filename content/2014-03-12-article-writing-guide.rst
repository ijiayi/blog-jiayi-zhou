Article writing guide
#####################

:category: guide
:tags: pelican, rst, guide, template


Template
========

.. code-block:: rst

   Title
   #####

   :category: category1
   :tags: tag1, tag2

   .. contents::


   Heading 1
   =========

   .. code-block:: python

      def foo(): pass


   Heading 1.1
   -----------


   Heading 1.1.1
   ^^^^^^^^^^^^^


   Heading 1.1.1.1
   """""""""""""""

Pelican
=======

#. `Pelican getting started`_

.. _Pelican getting started: http://docs.getpelican.com/en/latest/getting_started.html

Syntax
------

#. Use ``:status: hidden`` to hide the article / page.
#. Use ``:status: draft`` to craete draft page (under ``/drafts``).
#. Use ``<{filename}/cat/article2.rst>`` to link to content root.
#. Use ``<{filename}cat/article2.rst>`` to link to current root.
#. Using ``{tag}tagname`` and ``{category}foobar`` to link to tags and categories.


reStructuredText
================

#. `A ReStructuredText Primer`_
#. `Quick reStructuredText`_
#. `reStructuredText`_
#. `Documenting Python <http://docs.python.org/devguide/documenting.html>`_

.. _A ReStructuredText Primer: http://docutils.sourceforge.net/docs/user/rst/quickstart.html
.. _Quick reStructuredText: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _reStructuredText: http://docutils.sourceforge.net/rst.html


Online tools
============

#. Pygments demo http://pygments.org/demo/
#. Pygments lexers http://pygments.org/docs/lexers/
#. Online reStructuredText editor http://rst.ninjs.org/


