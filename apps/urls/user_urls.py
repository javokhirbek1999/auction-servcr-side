from django.urls import path, include

from ..views import user_views


app_name = 'user'


urlpatterns = [
    path('create/', user_views.UserAPIView.as_view(), name='create-user'),
    path('create-superuser/', user_views.CreateSuperuserAPIView.as_view(), name='create-superuser'),
    path('user/<str:pk>', user_views.UpdateDeleteUserAPIView.as_view(), name='user'),
    path('admin/<str:pk>', user_views.UpdateDeleteAdminUserAPIView.as_view(), name='admin-user'),
    path('all/', user_views.AllUsers.as_view(), name='all-users'),
    path('token/', user_views.AuthTokenAPIView.as_view(), name='token'),
]