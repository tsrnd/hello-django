from django.urls import path, include
app_name = 'myapp'
urlpatterns = [
    path('foo/', include('myapp.foo.urls')),
    path('categories/', include('myapp.category.urls'))
]
