from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resumeapi/', views.ResumeAPI.as_view())
]