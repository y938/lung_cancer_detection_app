# lung_cancer_detection/urls.py
from django.urls import path, include

urlpatterns = [
    path('lung_detection/', include('lung_detection_app.urls')),
]
