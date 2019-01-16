from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import BlogpostView, BlogpostDetailView, BlogpostCreateView, BlogpostEditView, SignupView


urlpatterns = [
    path('posts/', BlogpostView.as_view(), name='posts'),
    path('posts/<int:id>/', BlogpostDetailView.as_view(), name='posts-detail'),
    path('posts/create/', BlogpostCreateView.as_view(), name='posts-create'),
    path('posts/<int:id>/edit/', BlogpostEditView.as_view(), name='posts-edit'),

    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='blog/login.html', next_page='/accounts/login/'), name='logout'),
]