from django.urls import path
from .views import gender_view

urlpatterns = [
    path('api/classify', gender_view, name='gender-classify'),
]
