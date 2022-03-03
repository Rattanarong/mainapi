from rest_framework import serializers
from .models import Datalist, Device1, Device2, Device3


class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datalist
        fields = ('id', 'username', 'password', 'email', 'phone')

class DeviceSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Device1
        fields = ('id','qrname1','namesw1')

class DeviceSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Device2
        fields = ('id','qrname2','namesw21','namesw22')

class DeviceSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Device3
        fields = ('id','qrname3','namesw31','namesw32','namesw33')

