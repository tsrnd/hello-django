from django.urls import path, include
from django.urls import path, include
app_name = 'myapp1'
urlpatterns = [
    path('question_choice/', include('myapp1.question_choice.urls'))
]
