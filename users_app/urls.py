from django.urls import path
from users_app import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

]
