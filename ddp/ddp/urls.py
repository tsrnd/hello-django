from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Post API',
                                     description='RESTful API for Post')),
    #url(r'^', include(('posts.urls', 'posts'), namespace='posts')),
    #url(r'^', include(('topics.urls', 'topics'), namespace='topics')),
]