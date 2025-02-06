from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import BasePermission
import src.core.models as models


class AdminPermission(BasePermission):
    try:
        def has_permission(self, request, view):
            if request.user and request.user.is_authenticated:
                return request.user.role == models.CONSTANTS.ROLE.admin
    except Exception as e:
        raise NotAuthenticated(e)


class StadionOwnerPermission(BasePermission):
    try:
        def has_permission(self, request, view):
            if request.user and request.user.is_authenticated:
                return request.user.role == models.CONSTANTS.ROLE.stadion_owner
    except Exception as e:
        raise NotAuthenticated(e)


class ClientPermission(BasePermission):
    try:
        def has_permission(self, request, view):
            if request.user and request.user.is_authenticated:
                return request.user.role == models.CONSTANTS.ROLE.client
    except Exception as e:
        raise NotAuthenticated(e)
