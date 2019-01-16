from django.urls import path, include

urlpatterns = [
    path('poll/', include('myapp.poll.urls'))
]
