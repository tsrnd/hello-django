from django.urls import path
from . import views

urlpatterns = [
    path('create/<str:name>', views.create, name='create'),
    path('get', views.getUser, name='getUser'),
    path('getname/<str:name>', views.getName, name='getName'),
    path('update/<int:id>/<str:newname>',views.update,name ='update'),
    path('delete/<int:id>',views.delete,name = "delete"),
    path('json',views.getUserJson,name = "getUserJson")
]
