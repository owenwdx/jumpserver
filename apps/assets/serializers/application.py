# -*- coding: utf-8 -*-
#


from rest_framework import serializers
from common.mixins import BulkSerializerMixin
from common.serializers import AdaptedBulkListSerializer
from common.fields.serializer import DictField

from ..models import Application


__all__ = [
    'ApplicationSerializer',
]


class ApplicationSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    应用(remote_app)的数据结构
    """
    # 如果不加 params(格式:{}) 校验不通过
    params = DictField()

    class Meta:
        model = Application
        list_serializer_class = AdaptedBulkListSerializer
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        return super().is_valid()
