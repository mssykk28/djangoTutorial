"""
djangoTutorial プロジェクト用の Django 設定です。

Django 4.0.3 を使って 'django-admin startproject' で生成されます。

このファイルの詳細については
https://docs.djangoproject.com/en/4.0/topics/settings/

設定項目の全リストとその値については
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# プロジェクト内のビルドパスはこのようにします。BASE_DIR / 'subdir' です。
BASE_DIR = Path(__file__).resolve().parent.parent

# クイックスタート開発設定 - 製品版には適さない
# https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/ をご覧ください。

# セキュリティ警告: 実稼働環境で使用する秘密鍵は秘密にしてください!
SECRET_KEY = 'django-insecure-_po7n6g$#gue1%0e71e1pyyg$c7hxx=o_$2#xr@ze0rmmq@u)r'

# セキュリティ警告: 実稼働環境ではデバッグをオンにして実行しないでください!
DEBUG = True

ALLOWED_HOSTS = []

# アプリケーションの定義

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'djangoTutorial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'djangoTutorial.wsgi.application'

# データベース
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# パスワードの検証
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# 国際化
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# 静的ファイル（CSS、JavaScript、画像）
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# デフォルトの主キーフィールドの種類
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
