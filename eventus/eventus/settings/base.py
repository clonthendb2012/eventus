from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'g#^y7x%2ilu*laa_76eg9b$*14t794$fw4=e0%%5p_v=-3p7-3'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DJANGO_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    )
    
LOCAL_APPS = (
        'apps.events',
        'apps.users',
    )    

THIRD_PARTY_APPS = (

    )

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS +THIRD_PARTY_APPS
    

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eventus.urls'

WSGI_APPLICATION = 'eventus.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.User'