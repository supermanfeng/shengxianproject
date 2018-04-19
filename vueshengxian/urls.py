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
from django.views.static import serve
from rest_framework.documentation import include_docs_urls

from rest_framework.routers import DefaultRouter

import xadmin
from goods.views import GoodsListViewSet, CategoryViewSet
from vueshengxian.settings import MEDIA_ROOT

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')
goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})

# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name='categorys')
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    # 生成文档
    url(r'docs/$', include_docs_urls(title='生鲜网')),
    # 登录配置
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
