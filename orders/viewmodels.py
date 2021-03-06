#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence 
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: viewmodels.py
@time: 2018/6/9 上午1:28
"""
from rest_framework import serializers
from accounts.models import UserModel, WxUserModel
from orders.models import OrderModel, BlessingModel
from xiaobiaobai.utils import get_systemconfigs, convert_to_uuid, check_words_spam

from django.core.exceptions import ObjectDoesNotExist

from accounts.viewmodels import UserModelSerializer
import logging

logger = logging.getLogger(__name__)


class BlessingSerializer(serializers.Serializer):
    usermodel = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(),
                                                   pk_field=serializers.UUIDField())
    ordermodel = serializers.PrimaryKeyRelatedField(queryset=OrderModel.objects.all(),
                                                    pk_field=serializers.UUIDField())


class PostLoveSerializer(serializers.Serializer):
    usermodel = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(),
                                                   pk_field=serializers.UUIDField()
                                                   )
    username = serializers.CharField(required=True)
    target_username = serializers.CharField(required=True)
    background_img = serializers.CharField(required=False, allow_blank=True)
    candies_count = serializers.IntegerField(required=True, min_value=0)
    order_content = serializers.CharField(required=True, max_length=200)
    city = serializers.CharField(required=True, max_length=100)

    # def validate(self, attrs):
    #     order_content = attrs['order_content']
    #     if not check_words_spam(order_content):
    #         raise serializers.ValidationError("order_content", "订单内容非法")
    #     return super(PostLoveSerializer, self).validate(attrs)


class OrderSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex')
    usermodel = UserModelSerializer(read_only=True)

    username = serializers.CharField()
    target_username = serializers.CharField(required=True)
    background_img = serializers.CharField(required=False, allow_blank=True)

    candies_count = serializers.IntegerField(required=True, min_value=0)
    order_content = serializers.CharField(required=True, max_length=200)
    city = serializers.CharField(required=True, max_length=100)
    wx_prepayid = serializers.CharField(required=True, max_length=100)
    # blessings = BlessingSerializer(read_only=True, many=True, source='blessingmodel_set')
    confirmations = serializers.IntegerField(required=False)
    block_height = serializers.IntegerField(required=False)
    txid = serializers.CharField(required=False)
    block_chain_url = serializers.CharField(required=False)
    blessing_count = serializers.IntegerField(required=False, default=0)
    show_confession_wall = serializers.BooleanField(default=True)
    created_time = serializers.DateTimeField(required=False)
    pay_time = serializers.DateTimeField(required=False)


class ConfessionWallSerializer(serializers.Serializer):
    usermodel = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(),
                                                   pk_field=serializers.UUIDField()
                                                   )
    ordermodel = serializers.PrimaryKeyRelatedField(queryset=OrderModel.objects.all(),
                                                    pk_field=serializers.UUIDField())
    status = serializers.BooleanField(required=True)
