from django.urls import path
from cms.views import index

urlpatterns = [
    path('', index),
]
