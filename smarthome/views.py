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
1
# @api_view(['GET'])
# def all_name1(request):
#     alldata = name1.objects.all()
#     serializer = nameSerializer1(alldata, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def post_name1(request):
#     if request.method == 'POST':
#         serializer = nameSerializer1(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(['PUT'])
# def update_name1(request, TID):
#     todo = name1.objects.get(id=TID)
#     if request.method == 'PUT':
#         data = {}
#         serializer = nameSerializer1(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data['status'] = 'updated'
#             return Response(data=data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def all_name2(request):
#     alldata = name2.objects.all()
#     serializer = nameSerializer2(alldata, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def post_name2(request):
#     if request.method == 'POST':
#         serializer = nameSerializer2(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(['PUT'])
# def update_name2(request, TID):
#     todo = name2.objects.get(id=TID)
#     if request.method == 'PUT':
#         data = {}
#         serializer = nameSerializer2(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data['status'] = 'updated'
#             return Response(data=data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def all_name3(request):
#     alldata = name3.objects.all()
#     serializer = nameSerializer3(alldata, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def post_name3(request):
#     if request.method == 'POST':
#         serializer = nameSerializer3(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(['PUT'])
# def update_name3(request, TID):
#     todo = name3.objects.get(id=TID)
#     if request.method == 'PUT':
#         data = {}
#         serializer = nameSerializer3(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data['status'] = 'updated'
#             return Response(data=data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def all_name4(request):
#     alldata = name4.objects.all()
#     serializer = nameSerializer4(alldata, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def post_name4(request):
#     if request.method == 'POST':
#         serializer = nameSerializer4(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(['PUT'])
# def update_name4(request, TID):
#     todo = name4.objects.get(id=TID)
#     if request.method == 'PUT':
#         data = {}
#         serializer = nameSerializer4(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data['status'] = 'updated'
#             return Response(data=data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def all_name5(request):
#     alldata = name5.objects.all()
#     serializer = nameSerializer5(alldata, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def post_name5(request):
#     if request.method == 'POST':
#         serializer = nameSerializer5(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(['PUT'])
# def update_name5(request, TID):
#     todo = name5.objects.get(id=TID)
#     if request.method == 'PUT':
#         data = {}
#         serializer =nameSerializer5(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data['status'] = 'updated'
#             return Response(data=data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def all_name6(request):
#     alldata = name6.objects.all()
#     serializer = nameSerializer6(alldata, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def post_name6(request):
#     if request.method == 'POST':
#         serializer = nameSerializer6(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(['PUT'])
# def update_name6(request, TID):
#     todo = name6.objects.get(id=TID)
#     if request.method == 'PUT':
#         data = {}
#         serializer = nameSerializer6(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data['status'] = 'updated'
#             return Response(data=data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

data = [{'message': 'hello world'}, {'message': 'wellcome'},
        {
        "title": "labtop คืออะไร?",
        "subtitle": "คอมพิวเตอร์ คือ อุปกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่นๆ?",
        "image_url": "https://raw.githubusercontent.com/Nuikittinan/BasicAPI/main/computer.jpg",
        "detail": "คอมพิวเตอร์มาจากภาษาละตินว่า Computare ซึ่งหมายถึง การนับ หรือ การคำนวณพจนานุกรม ฉบับราชบัณฑิตยสถาน พ.ศ. 2525 ให้ความหมายของคอมพิวเตอร์ไว้ว่า/n/nเครื่องอิเล็กทรอนิกส์แบบอัตโนมัติ ทำหน้าที่เหมือนสมองกล ใช้สำหรับแก้ปัญหาต่างๆ ที่ง่ายและซับซ้อนโดยวิธีทางคณิตศาสตร์\n\nคอมพิวเตอร์ จึงเป็นเครื่องจักรอิเล็กทรอนิกส์ที่ถูกสร้างขึ้นเพื่อใช้ทำงานแทนมนุษย์ ในด้านการคิดคำนวณและสามารถจำข้อมูล ทั้งตัวเลขและตัวอักษรได้เพื่อการเรียกใช้งานในครั้งต่อไป  นอกจากนี้ ยังสามารถจัดการกับสัญลักษณ์ได้ด้วยความเร็วสูง โดยปฏิบัติตามขั้นตอนของโปรแกรม คอมพิวเตอร์ยังมีความสามารถในด้านต่างๆ อีกมาก อาทิเช่น การเปรียบเทียบทางตรรกศาสตร์ การรับส่งข้อมูล การจัดเก็บข้อมูลในตัวเครื่องและสามารถประมวลผลจากข้อมูลต่างๆ ได้ การทำงานของคอมพิวเตอร์"
        }]


def Home(request):
    return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii': False})
