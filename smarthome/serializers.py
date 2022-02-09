from rest_framework import serializers
from .models import Datalist, Device


class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datalist
        fields = ('id', 'username', 'password', 'email', 'phone')

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id','qrname1','qrname2','qrname3')
