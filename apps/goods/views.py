from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins, generics, viewsets, filters
from rest_framework.pagination import PageNumberPagination

from goods.filter import GoodsFilter
from .serializers import GoodsSerializer
from .models import Goods


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_limit = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    # 商品列表页
    # 如果需要分页就需要对rest_framework里面的settings里面的
    #  'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    # 进行重写，将其配置到我们自己的settings里面
    # 我们甚至可以自己定义分页的设置，也就是重写rest_framework里面的分页设置pagination.py
    # 下面的Limitpaginations类，
    # 就像上面这样GoodsPagination
    # 还需要在下面声明一下

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    #分页
    pagination_class = GoodsPagination
    # 过滤语句，过滤的类我们在filter文件中自定义
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    # 搜索框的模糊搜索，是rest_framework里面的
    search_fields = ['name', 'goods_brief', 'goods_desc']
    # 按照制定字段排序
    ordering_fields = ['sold_nums', 'add_time']
