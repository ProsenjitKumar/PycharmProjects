from django.conf import settings
INSTALLED_APPS = [
    'sms_simple',
]


def get_required_apps():
    # ensure that there are no duplicate apps
    return [app for app in INSTALLED_APPS if app not in settings.INSTALLED_APPS]

