from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .user import User
from django.views.decorators.csrf import csrf_exempt
from user.model.userSerializer import UserSerializer
# from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

def create(request,name):
    result = User.objects.all()
    res = HttpResponse()
    # if result is None:
    #     user = User(1,name)
    #     user.save()
    # else:
    #     user = User(len(result)+1 ,name)
    #     user.save()
    user = User(name = name)
    user.save()
    result = User.objects.all()
    for us in result:
        res.write(us.name)
    return HttpResponse(res)

def getUser(request):
    user = User.objects.all()
    return render(request,'user.html',{'users':user})


def getName(request,name):
    result = User.objects.filter(name = name)
    res = HttpResponse()
    for us in result:
        res.write(us.name)
    return HttpResponse(res)

def update(reqest,id,newname):
    result = User.objects.get(id = id)
    result.name = newname
    result.save()
    return HttpResponse("ok")

def delete(reqest,id):
    # result = User.objects.get(id = id)
    result = User.objects.all()
    result.delete()
    return HttpResponse("ok")

# @csrf_exempt
@api_view()
def getUserJson(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializers = UserSerializer(user,many=True)
        # user = User.objects.get(pk=1)
        # serializers = UserSerializer(user)
        return Response(serializers.data)
    else:
        return HttpResponse("fail")
    