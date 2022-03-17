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
    path('api/all-devicelist1/',all_devicelist1),
    path('api/post-devicelist1/',post_devicelist1),
    path('api/update-devicelist1/<int:TID>', update_devicelist1),
    path('api/delete-devicelist1/<int:TID>', delete_devicelist1),
    path('api/all-devicelist2/',all_devicelist2),
    path('api/post-devicelist2/',post_devicelist2),
    path('api/update-devicelist2/<int:TID>', update_devicelist2),
    path('api/delete-devicelist2/<int:TID>', delete_devicelist2),
    path('api/all-devicelist3/',all_devicelist3),
    path('api/post-devicelist3/',post_devicelist3),
    path('api/update-devicelist3/<int:TID>', update_devicelist3),
    path('api/delete-devicelist3/<int:TID>', delete_devicelist3),
]
