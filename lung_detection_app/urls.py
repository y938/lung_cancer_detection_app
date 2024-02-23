# lung_detection_app/urls.py

from django.urls import path
from .views import predict_lung_cancer

urlpatterns = [
    path('predict/', predict_lung_cancer, name='predict_lung_cancer'),
]
