"""
djangoTutorial プロジェクト用の ASGI 設定です。

これは ASGI 呼び出しを ``application`` という名前のモジュールレベルの変数として公開します。

このファイルに関する詳細な情報は
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoTutorial.settings')

application = get_asgi_application()
