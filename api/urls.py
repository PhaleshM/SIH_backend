from django.urls import path
from .views import predict_image_view

urlpatterns = [
    path('predict/', predict_image_view, name='predict_image'),
]
