import os
from dotenv import load_dotenv
import dj_database_url
from environs import Env


load_dotenv()

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG", default=False)

ROOT_URLCONF = os.getenv('ROOT_URLCONF')

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS', '').split(',')]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')

TIME_ZONE = os.getenv('TIME_ZONE')

USE_TZ = True

DEFAULT_AUTO_FIELD = os.getenv('DEFAULT_AUTO_FIELD')
