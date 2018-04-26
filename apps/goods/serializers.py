from rest_framework import serializers

from goods.models import Goods, GoodsCategory, Goods_Image, IndexAd, GoodsCategoryBrand, Banner, HotSearchWords


class CategorySerializer3(serializers.ModelSerializer):
    """
    商品分类列表的三重嵌套实现，获取一级类目，二级类目，三级类目
    """

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods_Image
        fields = ['image', ]


class GoodsSerializer(serializers.ModelSerializer):
    """
    在这里设定模型的返回前端的字段对应的是views里面的view
    相当于一个映射
    这里的一个流程是url———》views———》views根据定义的serrializer的映射来 
    获取索取指定字段
    """
    # 获取外键的详细信息
    category = CategorySerializer()
    image = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        # fields = ['name', 'click_nums', 'market_price', 'add_time']
        fields = "__all__"  # 是获取所有字段


class GoodsCategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """

    class Meta:
        model = Goods
        fields = "__all__"
class HotWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = "__all__"


class IndexCategorySerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True)
    goods = serializers.SerializerMethodField()
    sub_cat = CategorySerializer2(many=True)
    ad_goods = serializers.SerializerMethodField()

    def get_ad_goods(self, obj):
        goods_json = {}
        ad_goods = IndexAd.objects.filter(category_id=obj.id, )
        if ad_goods:
            good_ins = ad_goods[0].goods
            goods_json = GoodsSerializer(good_ins, many=False, context={'request': self.context['request']}).data
        return goods_json



    def get_goods(self, obj):
        all_goods = Goods.objects.filter(Q(category_id=obj.id)|Q(category__parent_category_id=obj.id)|Q(category__parent_category__parent_category_id=obj.id))
        goods_serializer = GoodsSerializer(all_goods, many=True, context={'request': self.context['request']})
        return goods_serializer.data

    class Meta:
        model = GoodsCategory
        fields = "__all__"