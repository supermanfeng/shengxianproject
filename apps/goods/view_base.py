from django.views.generic.base import View

from goods.models import Goods
from django.forms.models import model_to_dict
import json
from django.http import JsonResponse
from django.core import serializers


class GoodsListView(View):
    """
    将数据转换成json格式返回前端
    """

    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:10]

        for good in goods:
            # 获取所有字段并转换成字典
            json_dict = model_to_dict(good)
            json_list.append(json_dict)
        #序列化
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
