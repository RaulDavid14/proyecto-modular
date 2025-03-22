from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-$!w2v!_z*q21u8-7q-!4z^)d-8gyuq2e$wi&7(b!!ltu=wcns-'

#CLOUDINARY_URL=cloudinary://743488436471177:-vVeNLPnyiJa6TMSFBl31VKw6Kc@dqqoht6ge

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dqqoht6ge',
    'API_KEY': '743488436471177',
    'API_SECRET': '-vVeNLPnyiJa6TMSFBl31VKw6Kc',
}

cloudinary.config( 
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],  
    api_key=CLOUDINARY_STORAGE['API_KEY'],  
    api_secret=CLOUDINARY_STORAGE['API_SECRET']  
)

INSTALLED_APPS = [
    'imagenes',
    'cfca_webhook',
    'cfca_api',
    'rest_framework',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'layout',
    'datos_socioeconomicos',
    'landing',
    'catalogos',
    'usuario',
    'cuestionario',
    'panel_administrador',
    'clustering',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto.wsgi.application'

AUTH_USER_MODEL = 'usuario.UserModel'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGIN_URL = '/usuarios/login/' #redigir en caso de no estar autenticado.

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Autenticación estándar de Django
]

# EMAIL PARA RESTABLECIMIENTO DE PASS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'in-v3.mailjet.com'  # El servidor SMTP de Mailjet
EMAIL_PORT = 587  # Puerto de Mailjet para enviar correos
EMAIL_USE_TLS = True  # Usar TLS para la conexión segura
EMAIL_HOST_USER = '8a96bb0570d94c3ded9da36ab0a14ff9'  # API Key pública
EMAIL_HOST_PASSWORD = '827be7ad9f037070ac104ae50e62f4a5' # API Key Secreta
DEFAULT_FROM_EMAIL = 'mxcfca@gmail.com'  # La dirección de correo desde la que enviarás los correos
