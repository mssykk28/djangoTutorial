"""
djangoTutorial プロジェクト用の WSGI 設定です。

これは WSGI 呼び出しを ``application`` という名前のモジュールレベルの変数として公開します。

このファイルに関する詳細な情報は
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoTutorial.settings')

application = get_wsgi_application()
