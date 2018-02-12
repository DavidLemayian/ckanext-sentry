.. image:: https://travis-ci.org/ViderumGlobal/ckanext-sentry.svg?branch=master
    :target: https://travis-ci.org/ViderumGlobal/ckanext-sentry

.. image:: https://coveralls.io/repos/github/ViderumGlobal/ckanext-sentry/badge.svg?branch=master
    :target: https://coveralls.io/github/ViderumGlobal/ckanext-sentry?branch=master

Sentry CKAN extension
======================

The Sentry CKAN extension allows to add a `Sentry`_ middleware to the CKAN and stack and optionally configure a Sentry log handler.

This extension builds on top of the previous work of:

* @noirbizarre on https://github.com/etalab/ckanext-sentry
* @rshk on https://github.com/opendatatrentino/ckanext-sentry

Installation
------------

To install the extension, activate your virtualenv and run::

    pip install ckanext-sentry

Alternative, you can install a development version with::

    git clone https://github.com/okfn/ckanext-sentry.git
    cd ckanext-sentry
    python setup.py develop
    pip install -r requirements.txt

Configuration
-------------


To activate the plugin, add ``sentry`` to the ``ckan.plugins`` key in your ini file::

    ckan.plugins = sentry <other-plugins>

You must provide a Sentry DSN::

    sentry.dsn = https://xxxxxx:xxxxxx@sentry.domain.com/1

You can see a full list of supported options for the Sentry client on the `official Raven documentation`_.

If you want Sentry to record your log messages, you can turn it on adding the following options::

    sentry.configure_logging=True
    sentry.log_level=WARN

The default log level if not provided in the configuration is INFO.

All these configuration options can also be passed via environment variables:

* ``SENTRY_DSN`` or ``CKAN_SENTRY_DSN``
* ``CKAN_SENTRY_CONFIGURE_LOGGING``
* ``CKAN_SENTRY_LOG_LEVEL``

The configuration also supports env vars named like the `ckanext-envvars`_ extension convention (eg ``CKAN___SENTRY__LOG_LEVEL``).




.. _Sentry: http://getsentry.com/
.. _official Raven documentation: http://raven.readthedocs.org/en/latest/advanced.html#configuring-the-client
.. _ckanext-envvars: https://github.com/okfn/ckanext-envvars
