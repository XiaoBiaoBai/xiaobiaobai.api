#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence 
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: urls.py
@time: 2018/6/10 下午12:16
"""

from django.urls import path
from orders.views import OrderList, OrderDetail, BlessingDetail, update_show_confession_wall

app_name = "orders"

urlpatterns = [
    path(r'order', OrderList.as_view(), name='orderlist'),
    path(r'orderdetail/<str:pk>', OrderDetail.as_view(), name='orderdetail'),
    path('blessing', BlessingDetail.as_view(), name='blessing'),
    path('updatewall', update_show_confession_wall, name='updatewall')
]
