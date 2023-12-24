from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

# Create a Celery instance
celery_app = Celery('your_project')

# Load task modules from all registered Django app configs.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
celery_app.autodiscover_tasks()

# Configuration for the message broker (Redis in this example)
celery_app.conf.broker_url = 'redis://localhost:6379/0'

# Configuration for the result backend (optional, you can omit this if not using result backend)
celery_app.conf.result_backend = 'redis://localhost:6379/0'

# Concurrency configuration
celery_app.conf.worker_concurrency = 4  # Adjust based on your server resources

# List of modules to import when Celery starts.
celery_app.conf.imports = ('your_project.tasks', )  # Add your task modules here

# Task Serialization Configuration
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'json'
celery_app.conf.accept_content = ['json']

# Task Time Limits Configuration
celery_app.conf.task_soft_time_limit = 300  # 5 minutes
celery_app.conf.task_time_limit = 600  # 10 minutes

# Task Retry Configuration
celery_app.conf.task_retry_delay = 300  # 5 minutes
celery_app.conf.task_max_retries = 3

# Task Queues Configuration
celery_app.conf.task_queues = {
    'default': {
        'exchange': 'default',
        'routing_key': 'default',
    },
    'priority_high': {
        'exchange': 'priority_high',
        'routing_key': 'priority_high',
    },
}

# Middleware Configuration
celery_app.conf.task_create_missing_queues = True
celery_app.conf.worker_prefetch_multiplier = 1
celery_app.conf.worker_disable_rate_limits = True

# Beat Scheduler Configuration (if using Celery Beat for periodic tasks)
celery_app.conf.beat_schedule = {
    'some-periodic-task': {
        'task': 'your_project.tasks.some_periodic_task',
        'schedule': 300,  # Every 5 minutes
    },
}

# Django Settings Configuration
celery_app.conf.update(
    result_expires=3600,  # Task results expire in 1 hour
    result_persistent=True,  # Task results are persistent
    worker_task_log_format=(
        '[%(asctime)s: %(levelname)s/%(processName)s] %(task_name)s[%(task_id)s]: %(message)s'
    ),
)

# Task Decorators and Bindings
@celery_app.task(bind=True)
def your_bound_task(self, *args, **kwargs):
    # Your task logic here
    pass

# Task Signal Handling
@celery_app.task_success_handler.connect
def task_success_handler(sender=None, result=None, **kwargs):
    # Handle task success
    pass

@celery_app.task_failure_handler.connect
def task_failure_handler(sender=None, exception=None, **kwargs):
    # Handle task failure
    pass

# Logging Configuration
celery_app.conf.worker_log_format = (
    '[%(asctime)s: %(levelname)s/%(processName)s] %(task_name)s[%(task_id)s]: %(message)s'
)
# Configuration for Celery Sentry for error tracking
celery_app.conf['sentry_dsn'] = 'YOUR_SENTRY_DSN'
celery_app.conf['sentry_environment'] = 'production'
celery_app.conf['sentry_release'] = 'your_project_version'

# Configuration for Celery Redis for result backend (if using Redis as the result backend)
celery_app.conf['result_backend'] = 'redis://localhost:6379/1'

# Configuration for Celery Flower for monitoring (if using Celery Flower)
celery_app.conf['flower_url'] = 'http://localhost:5555'