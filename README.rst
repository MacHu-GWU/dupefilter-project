.. image:: https://travis-ci.org/MacHu-GWU/dupefilter-project.svg?branch=master

.. image:: https://img.shields.io/pypi/v/dupefilter.svg

.. image:: https://img.shields.io/pypi/l/dupefilter.svg

.. image:: https://img.shields.io/pypi/pyversions/dupefilter.svg


Welcome to dupefilter Documentation
===============================================================================
dupefilter is a extendable library for job scheduler.

Problem we solve:

    Suppose you have a batch job to do, it has n-items, and it follows ``input`` -> ``output`` model. The job processor could be interrupted anytime, and you want to resume your work and avoid to process items that already processed.


**Quick Links**
-------------------------------------------------------------------------------
- `GitHub Homepage <https://github.com/MacHu-GWU/dupefilter-project>`_
- `Online Documentation <https://pypi.python.org/pypi/dupefilter>`_
- `PyPI download <https://pypi.python.org/pypi/dupefilter>`_
- `Install <install_>`_
- `Issue submit and feature request <https://github.com/MacHu-GWU/dupefilter-project/issues>`_
- `API reference and source code <http://pythonhosted.org/dupefilter/py-modindex.html>`_


.. _install:

Install
-------------------------------------------------------------------------------

``dupefilter`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install dupefilter

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade dupefilter