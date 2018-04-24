import django_filters

from goods.models import Goods
from django.db.models import Q


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤类
    """
    # 按照价格区间进行精确查询，学要在 settings中进行配置，也就是django.filter
    pricemin = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    # 按照名字进行模糊查询
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    # 查看商品的类目,Q对象是下面三者满足其一就可
    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'name']
