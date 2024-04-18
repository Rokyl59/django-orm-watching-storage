import os
import dj_database_url
from environs import Env


env = Env()
env.read_env()

DATABASES = {
    'default': dj_database_url.parse(env.str(
        "DATABASE_URL",
        default="postgres://user:password@localhost/dbname"))
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str("SECRET_KEY", "default_secret_key")


DEBUG = env.bool("DEBUG", default=False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", [])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
