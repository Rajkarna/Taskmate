from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.home, name="home"),
    path('todolist/' , include('todolist_app.urls')),
    path('account/' , include('users_app.urls')),
    path('contact', todolist_views.contactV, name="contact"),
    path('about', todolist_views.aboutV, name="about"),
]
