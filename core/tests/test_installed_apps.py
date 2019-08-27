from django.conf import settings

INSTALLED_APPS = settings.INSTALLED_APPS


def test_all_installed_apps():
    """ 
    Make sure that both local and third party apps are installed properly. 
    """

    assert 'debug_toolbar' in INSTALLED_APPS
    assert 'django_filters' in INSTALLED_APPS
    assert 'rest_framework' in INSTALLED_APPS
    assert 'rest_framework_swagger' in INSTALLED_APPS
