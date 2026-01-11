# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import logging

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

from ckan import plugins


log = logging.getLogger(__name__)


CONFIG_FROM_ENV_VARS = {
    'sentry.dsn': 'CKAN_SENTRY_DSN',  # Alias for SENTRY_DSN, used by sentry-sdk
    'sentry.log_level': 'CKAN_SENTRY_LOG_LEVEL',
}


class SentryPlugin(plugins.SingletonPlugin):
    '''A simple plugin that add the Sentry middleware to CKAN'''
    plugins.implements(plugins.IMiddleware, inherit=True)

    def make_middleware(self, app, config):
        if plugins.toolkit.check_ckan_version('2.3'):
            return app
        else:
            return self.make_error_log_middleware(app, config)

    def make_error_log_middleware(self, app, config):

        for option in CONFIG_FROM_ENV_VARS:
            from_env = os.environ.get(CONFIG_FROM_ENV_VARS[option], None)
            if from_env:
                config[option] = from_env
        if not config.get('sentry.dsn') and os.environ.get('SENTRY_DSN'):
            config['sentry.dsn'] = os.environ['SENTRY_DSN']

        log.debug('Adding Sentry middleware...')
        sentry_sdk.init(
            dsn=config.get('sentry.dsn'),
            integrations=[
                LoggingIntegration(
                    sentry_logs_level=config.get('sentry.log_level', logging.INFO),  # Capture INFO and above as logs
                    level=config.get('sentry.log_level', logging.INFO),              # Capture INFO and above as breadcrumbs
                    event_level=logging.ERROR,       # Send ERROR records as events
                ),
            ],
        )
        return app
