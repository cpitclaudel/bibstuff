================================
 reStructuredText Test Document
================================

.. Above is the document title, and below is the subtitle.
   They are transformed from section titles after parsing.

--------------------------------
 Examples of Syntax Constructs
--------------------------------

.. bibliographic fields (which also require a transform):

:Author: Dylan Schwilk
:Author: Alan G. Isaac
:Address: 1 Line
          Line 2
          Line 3
:Contact: https://github.com/dschwilk/bibstuff
:date: 2014-04-26
:status: for illustration only
:version: 1.1
:copyright: 2008-2014


Introduction
============

This introduction will simply demonstrate some citations which can be found in
the ``example.bib`` database. To expand these citations or produce a
bibliography list, use ``bib4txt.py``. The output should look like
``testout.rst``.

We have noticed that some people running this example encounter a simpleparse
error with python 2.5. For example, Ubuntu users should download the SourceForge
``simpleparse`` code rather than the Ubuntu packages. Uninstall the
``python-simpleparse`` and ``python-simpleparse-mxtexttools`` packages, download
the SourceForge simpleparse, and do ``python setup.py install``.

Now for some citations. Originally reST only supported citation reference names
that were valid HTML and XML names [isaac.schwilk-2010]_. Recently reST added
support for colons and plus signs, since these are common in BibTeX databases
[schwilk+isaac:2010]_. (However, we recommend that you avoid these characters if
you are creating a new database.) Naturally ``bib4txt.py`` will recognize all
valid reST citation references. However, it will also recognize multiple
comma-separated cites [isaac.schwilk-2010, schwilk+isaac:2010, man-2010]_.
Bibstuff will process these into your reference list, but since this remains illegal
as reStructuredText, such multiple citation references will be missed by most
reStructuredText readers.

That should be enough for a test, but here are a couple more:
[martin-2008-jds]_, [doe-2525-tq]_.

Use an `include directive`_ if you want to include the ``testout.rst`` bibliography.

References
==========


.. include:: testout.rst

.. Links

.. _include directive: http://docutils.sourceforge.net/docs/ref/rst/directives.html#including-an-external-document-fragment

