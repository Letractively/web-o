import logging

from settings import *


logging.disable(logging.ERROR)

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

CELERY_ALWAYS_EAGER = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(ROOT_PATH, 'test_cache'),
    }
}

TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'
COVERAGE_PATH_EXCLUDES = [r'.+/datasets', r'.+/fixtures', r'.+/migrations', r'.+/tests',
                            r'.+/features', r'.+/templates', r'.+/static',]
