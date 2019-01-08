from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .user import User
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def getUserJson(request):
    if request.method == 'GET':
        user = User.objects.all()
        result = serialize('json',user)
        return HttpResponse(result,content_type="application/json")
    else:
        return HttpResponse("fail")
    