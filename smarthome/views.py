import email
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import  DeviceSerializer1, DeviceSerializer2, DeviceSerializer3, TodolistSerializer
from .models import Datalist, Device1, Device2, Device3


@api_view(['GET'])
def all_newlist(request):
    alldata = Datalist.objects.all()
    serializer = TodolistSerializer(alldata, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_newlist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_newlist(request, TID):
    todo = Datalist.objects.get(id=TID)
    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_newlist(request, TID):
    todo = Datalist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode)

@api_view(['POST', 'GET'])
def register(request):
    if request.method == 'POST':
        data = request.data.copy()
        username = data.get('username')
        password = data.get('password')
        userclass = data.get('userclass')
        phone = data.get('phone')
        email = data.get('email')
        print(data)
        print(userclass)
        if username != '' and password != ''and phone != '' and email != '':
            if userclass == 'admin':
                try:
                    user = Datalist.objects.create(username = username, password = password,email = email, phone = phone)
                    user.save()
                    return Response(status = status.HTTP_201_CREATED)
                except:
                    return Response(status = status.HTTP_400_BAD_REQUEST)


            else:
                try:
                    user = Datalist.objects.create(username = username, password = password,email = email, phone = phone)
                    user.save()
                    return Response(status = status.HTTP_201_CREATED)
                except:
                    return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def login(request):
    if request.method == 'POST':
        data = request.data.copy()
        username = data.get('username')
        password = data.get('password')
        try:
            queryset = Datalist.objects.get(username = username)
            print(queryset)
            if queryset.password == password:
                print(queryset.password)
                return Response(queryset.password == "true",status = status.HTTP_200_OK)
            else:
                return Response(status = status.HTTP_404_NOT_FOUND)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
            

@api_view(['GET'])
def all_devicelist1(request):
    alldata = Device1.objects.all()
    serializer = DeviceSerializer1(alldata, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_devicelist1(request):
    if request.method == 'POST':
        serializer = DeviceSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_devicelist1(request, TID):
    todo1 = Device1.objects.get(id=TID)
    if request.method == 'PUT':
        data = {}
        serializer = DeviceSerializer1(todo1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_devicelist1(request, TID):
    todo1 = Device1.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo1.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        return Response(data=data, status=statuscode)

@api_view(['GET'])
def all_devicelist2(request):
    alldata = Device2.objects.all()
    serializer = DeviceSerializer2(alldata, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_devicelist2(request):
    if request.method == 'POST':
        serializer = DeviceSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_devicelist2(request, TID):
    todo1 = Device2.objects.get(id=TID)
    if request.method == 'PUT':
        data = {}
        serializer = DeviceSerializer2(todo1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_devicelist2(request, TID):
    todo1 = Device2.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo1.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        return Response(data=data, status=statuscode)


@api_view(['GET'])
def all_devicelist3(request):
    alldata = Device3.objects.all()
    serializer = DeviceSerializer3(alldata, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_devicelist3(request):
    if request.method == 'POST':
        serializer = DeviceSerializer3(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_devicelist3(request, TID):
    todo1 = Device3.objects.get(id=TID)
    if request.method == 'PUT':
        data = {}
        serializer = DeviceSerializer3(todo1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_devicelist3(request, TID):
    todo1 = Device3.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo1.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        return Response(data=data, status=statuscode)

# @api_view(['POST', 'GET'])
# def readsw(request):
#     if request.method == 'POST':
#         data = request.data.copy()
#         stsw1 = data.get('stsw1')
#         # password = data.get('password')
#         try:
#             queryset = Device1.objects.get(stsw1 = stsw1)
#             print(queryset)
#             if queryset.stsw1 == "true":
#                 print(queryset.stsw1)
#                 return Response(queryset.stsw1 == "true",status = status.HTTP_200_OK)
#             else:
#                 print(queryset.stsw1)
#                 return Response(queryset.stsw1 == "false",status = status.HTTP_404_NOT_FOUND)
#         except:
#             return Response(status = status.HTTP_400_BAD_REQUEST)

def Home(request):
    return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii': False})
