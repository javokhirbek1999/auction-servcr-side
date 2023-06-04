from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsAdminOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        
        return request.method in SAFE_METHODS or request.user.is_superuser


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        
        return request.user.id == obj.auctioneer.id