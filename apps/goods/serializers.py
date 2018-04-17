from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    """
    在这里设定模型的返回前端的字段对应的是views里面的view
    相当于一个映射
    这里的一个流程是url———》views———》views根据定义的serrializer的映射来 
    获取索取指定字段
    """
    # 获取外键的详细信息
    category = CategorySerializer()

    class Meta:
        model = Goods
        # fields = ['name', 'click_nums', 'market_price', 'add_time']
        fields = "__all__"  # 是获取所有字段
