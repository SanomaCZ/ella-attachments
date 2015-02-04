"""
Setup for ella-attachments tests.

"""

import os
import django

test_runner = None
old_config = None

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_ella_attachments.settings.base'


def setup():
    try:
        global test_runner
        global old_config

        try:
            from django.test.runner import DiscoverRunner as TestRunner
        except ImportError:
            from django.test.simple import DjangoTestSuiteRunner as TestRunner
        try:
            django.setup()
        except AttributeError:
            pass
        test_runner = TestRunner()
        test_runner.setup_test_environment()
        old_config = test_runner.setup_databases()

        from django.utils.translation import activate
        activate('cs')

        import ella.core.register

    except Exception:
        import traceback, pprint
        pprint.pprint(traceback.print_exc())
        raise


def teardown():
    from shutil import rmtree
    from django.conf import settings
    test_runner.teardown_databases(old_config)
    test_runner.teardown_test_environment()
    if os.path.exists(settings.MEDIA_ROOT):
        rmtree(settings.MEDIA_ROOT)
