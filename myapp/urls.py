from django.urls import path, include

urlpatterns = [
    path('products/', include('myapp.products.urls'))
]
