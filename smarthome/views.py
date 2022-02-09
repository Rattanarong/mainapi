from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import DeviceSerializer, TodolistSerializer
from .models import Datalist, Device


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
        print(data)
        print(userclass)
        if username != '' and password != ''and phone != '':

            # Create User ระดับทั่วไป สามารถดูข้อมูลต่าง ๆ ได้แต่ไม่สามารถแก้ไขหรือ Add User คนอื่น ๆ ได้
            if userclass == 'Datalist':
                try:
                    user = Datalist.objects.create_superuser(username = username, password = password,phone = phone)
                    user.save()
                    return Response(status = status.HTTP_201_CREATED)
                except:
                    return Response(status = status.HTTP_400_BAD_REQUEST)


            else:
                try:
                    user = Datalist.objects.create_user(username = username, password = password,phone = phone)
                    user.save()
                    return Response(status = status.HTTP_201_CREATED)
                except:
                    return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def login(request):
    if request.method == 'POST':
        try:
            data = request.data.copy()
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # Check user input ว่าเป็น SuperUser หรือไม่
                alldata_get = Datalist.objects.get(username=username)
                serializer = TodolistSerializer(alldata_get)
                # เป็น SupurUser return True
                if serializer.data['is_superuser'] == True:
                    return Response(serializer.data['is_superuser'], status=status.HTTP_200_OK)
                # ไม่เป็น SupurUser return false
                else:
                    return Response(serializer.data['is_superuser'], status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def all_devicelist(request):
    alldata = Device.objects.all()
    serializer = DeviceSerializer(alldata, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_devicelist(request):
    if request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_devicelist(request, TID):
    todo1 = Device.objects.get(id=TID)
    if request.method == 'PUT':
        data = {}
        serializer = DeviceSerializer(todo1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_devicelist(request, TID):
    todo1 = Device.objects.get(id=TID)

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

data = [{'message': 'hello world'}, {'message': 'wellcome'},
        {
        "title": "labtop คืออะไร?",
        "subtitle": "คอมพิวเตอร์ คือ อุปกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่นๆ?",
        "image_url": "https://raw.githubusercontent.com/Nuikittinan/BasicAPI/main/computer.jpg",
        "detail": "คอมพิวเตอร์มาจากภาษาละตินว่า Computare ซึ่งหมายถึง การนับ หรือ การคำนวณพจนานุกรม ฉบับราชบัณฑิตยสถาน พ.ศ. 2525 ให้ความหมายของคอมพิวเตอร์ไว้ว่า/n/nเครื่องอิเล็กทรอนิกส์แบบอัตโนมัติ ทำหน้าที่เหมือนสมองกล ใช้สำหรับแก้ปัญหาต่างๆ ที่ง่ายและซับซ้อนโดยวิธีทางคณิตศาสตร์\n\nคอมพิวเตอร์ จึงเป็นเครื่องจักรอิเล็กทรอนิกส์ที่ถูกสร้างขึ้นเพื่อใช้ทำงานแทนมนุษย์ ในด้านการคิดคำนวณและสามารถจำข้อมูล ทั้งตัวเลขและตัวอักษรได้เพื่อการเรียกใช้งานในครั้งต่อไป  นอกจากนี้ ยังสามารถจัดการกับสัญลักษณ์ได้ด้วยความเร็วสูง โดยปฏิบัติตามขั้นตอนของโปรแกรม คอมพิวเตอร์ยังมีความสามารถในด้านต่างๆ อีกมาก อาทิเช่น การเปรียบเทียบทางตรรกศาสตร์ การรับส่งข้อมูล การจัดเก็บข้อมูลในตัวเครื่องและสามารถประมวลผลจากข้อมูลต่างๆ ได้ การทำงานของคอมพิวเตอร์"
        }]


def Home(request):
    return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii': False})
