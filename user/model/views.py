from django.shortcuts import render
from django.http import HttpResponse
from .user import User


def create(request,name):
    result = User.objects.all()
    res = HttpResponse()
    if result is None:
        user = User(1,name)
        user.save()
    else:
        user = User(len(result)+1 ,name)
        user.save()
    result = User.objects.all()
    for us in result:
        res.write(us.name)
    return HttpResponse(res)

def getUser(request):
    user = User.objects.all()
    # res = HttpResponse()
    # res.write("<h1>id - user</h1>")
    # for us in user:
    #     res.write("<h1>%d - %s</h1>" %(us.id,us.name))
    # return HttpResponse(res)
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
    result = User.objects.get(id = id)
    result.delete()
    return HttpResponse("ok")
