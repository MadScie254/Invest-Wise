import os
import logging
import logging.config
from raven.contrib.django.raven_compat import handlers as sentry_handlers


# Default logging settings
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(settings.LOG_DIR, 'app.log'),
            'formatter': 'verbose'
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'your_project.views': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        
    },
}


# Update logging configuration with environment variables
def update_logging_config(config):
    level = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    config['handlers']['console']['level'] = level
    config['handlers']['file']['level'] = level
    config['loggers']['']['level'] = level
    return config


# Configure logging
logging.config.dictConfig(update_logging_config(LOGGING_CONFIG))