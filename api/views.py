from django.shortcuts import render,HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import io
def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data,safe=True)

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many =True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')

    # using jsonresponse
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res= {'msg':'Data created'}
            return JsonResponse(res)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type ='application/json')
@csrf_exempt
def student_update(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        print(pythondata)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id= id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type ='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type ='application/json')

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res= {'msg':'Data created'}
            return JsonResponse(res)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type ='application/json')

    if request.method == "PUT":
        json_data  = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = pythondata, partial =True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type ='application/json')