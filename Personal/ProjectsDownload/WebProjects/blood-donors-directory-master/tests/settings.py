SECRET_KEY = 'blah'
INSTALLED_APPS = [
    'bdd',
    'tests',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_database',
    }
}
