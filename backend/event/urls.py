from django.urls import path
from .views import register, success

urlpatterns = [
     path('', register, name="register"),
     path('success/<int:participant_id>', success, name="success"),
     
]