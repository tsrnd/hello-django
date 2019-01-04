from django.urls import path, include

urlpatterns = [
    path('foo/', include('myapp.foo.urls')),
    path('event/', include('myapp.events.urls')),
    path('car/', include('myapp.cars.urls'))
]
