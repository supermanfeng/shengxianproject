"""vueshengxian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

# from goods.view_base import GoodsListView
from goods.views import GoodsListView
from vueshengxian.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 在后台管理系统中,如果想要看到图片就得配置这个url,前提还需要子settings中配置好参数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 商品列表页
    url(r'goods/$', GoodsListView.as_view(), name='goods-list'),
    # 生成文档
    url(r'docs/$', include_docs_urls(title='生鲜网')),
    # 登录配置
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
