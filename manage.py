#!/usr/bin/env python
"""Django の管理作業用コマンドラインユーティリティです。"""
import os
import sys


def main():
    """管理タスクを実行する。"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoTutorial.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Django がインストールされていることは確認しましたか？"
            "環境変数 PYTHONPATH で利用可能ですか？もしかして"
            "仮想環境を有効にするのを忘れたのか？"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
