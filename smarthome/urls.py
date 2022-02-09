from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('', Home),
    path('api/all-newlist/',all_newlist),
    path('api/login/',login),
    path('api/register/',register),
    path('api/post-newlist/',post_newlist),
    path('api/update-newlist/<int:TID>', update_newlist),
    path('api/delete-newlist/<int:TID>', delete_newlist),
    path('api/all-devicelist/',all_devicelist),
    path('api/post-devicelist/',post_devicelist),
    path('api/update-devicelist/<int:TID>', update_devicelist),
    path('api/delete-devicelist/<int:TID>', delete_devicelist),
]
