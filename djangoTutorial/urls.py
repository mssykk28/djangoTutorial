"""djangoTutorial URL の構成

urlpatterns` リストは URL をビューにルーティングします。より詳細な情報は
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
例
関数ビュー
    1. インポートの追加：from my_app import views
    2. URLをurlpatternsに追加：path('', views.home, name='home')
クラスベースのビュー
    1. インポートの追加: from other_app.views import Home
    2. URLをurlpatternsに追加：path('', Home.as_view(), name='home')
別のURLconfを含める
    1. include() 関数をインポートする： from django.urls import include, path
    2. URLをurlpatternsに追加する： path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
