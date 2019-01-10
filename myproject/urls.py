from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('blog/', include('blog.urls'))
]
