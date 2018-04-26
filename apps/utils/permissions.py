# -*- coding: utf-8 -*-
__author__ = 'bobby'
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
 对象等级权限仅允许拥有者区编辑
 比如说用户的收藏,仅允许该收藏的用户自己区修改
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user