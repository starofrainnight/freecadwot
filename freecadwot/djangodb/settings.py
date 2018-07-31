import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        # Database driver
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.abspath(os.curdir), 'freecadwot.sqlite'),
    },
}

CURRENT_MODULE_DIR = '.'.join(__name__.split('.')[:-1])

INSTALLED_APPS = (
    CURRENT_MODULE_DIR + '.freecadwot',
)

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = '6faw3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa'
