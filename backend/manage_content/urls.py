
from django.urls import path
from manage_content import views

urlpatterns = [
    path('', views.test),
]
