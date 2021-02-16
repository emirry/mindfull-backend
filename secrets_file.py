from dotenv import load_dotenv
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mindfull',
        'USER': 'postgres',
        'HOST': os.environ['HOST'],
        'PORT': os.environ['PORT']
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': os.environ['PASS1'],
    },
    {
        'NAME': os.environ['PASS2'],
    },
    {
        'NAME': os.environ['PASS3'],
    },
    {
        'NAME': os.environ['PASS4'],
    },
]
