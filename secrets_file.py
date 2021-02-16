from dotenv import load_dotenv
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV['KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mindfull',
        'USER': 'postgres',
        'HOST': ENV['HOST'],
        'PORT': ENV['PORT']
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ENV['PASS1'],
    },
    {
        'NAME': ENV['PASS2'],
    },
    {
        'NAME': ENV['PASS3'],
    },
    {
        'NAME': ENV['PASS4'],
    },
]
