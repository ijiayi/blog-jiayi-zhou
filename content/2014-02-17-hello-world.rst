Hello Pelican
################

:date: 2014-02-17
:tags: hello, pelican
:category: misc
:slug: hello-pelican
:author: Jiayi Zhou
:summary: First contact with Pelican



Hello
=====

* Dear Daniel
* Some ``code`` inline

"Hello Kitty"

This will be turned into :abbr:`HTML (HyperText Markup Language)`.

Link to `page <{filename}/pages/python.rst>`_

`<www.hinet.net>`_

Link to tags
`<{tag}hello>`_

Link to category
`<{category}misc>`_

.. image:: {filename}images/ice.jpg
  :width: 400px


Kitty
=====

.. code-block:: python
  :linenos: table


    def main(argv=None):
        """Run as a command-line script: colorize a python file or stdin using ANSI
        color escapes and print to stdout.

        Inputs:

          - argv(None): a list of strings like sys.argv[1:] giving the command-line
            arguments. If None, use sys.argv[1:].
        """

        usage_msg = """%prog [options] [filename]

    Colorize a python file or stdin using ANSI color escapes and print to stdout.
    If no filename is given, or if filename is -, read standard input."""

        import optparse
        parser = optparse.OptionParser(usage=usage_msg)
        newopt = parser.add_option
        newopt('-s','--scheme',metavar='NAME',dest='scheme_name',action='store',
               choices=['Linux','LightBG','NoColor'],default=_scheme_default,
               help="give the color scheme to use. Currently only 'Linux'\
     (default) and 'LightBG' and 'NoColor' are implemented (give without\
     quotes)")

        opts,args = parser.parse_args(argv)

        if len(args) > 1:
            parser.error("you must give at most one filename.")

        if len(args) == 0:
            fname = '-' # no filename given; setup to read from stdin
        else:
            fname = args[0]

        if fname == '-':
            stream = sys.stdin
        else:
            try:
                stream = open(fname)
            except IOError as msg:
                print(msg, file=sys.stderr)
                sys.exit(1)

        parser = Parser()

        # we need nested try blocks because pre-2.5 python doesn't support unified
        # try-except-finally
        try:
            try:
                # write colorized version to stdout
                parser.format(stream.read(),scheme=opts.scheme_name)
            except IOError as msg:
                # if user reads through a pager and quits, don't print traceback
                if msg.args != (32,'Broken pipe'):
                    raise
        finally:
            if stream is not sys.stdin:
                stream.close() # in case a non-handled exception happened above

    if __name__ == "__main__":
        main()

.. code-block:: python 

  def hello_kitty():
    return 'dear daniel'


.. code-block:: json

  {
  'key': 'value',
  'key2': ['list', 'value', 1, 2, 3]
  }
