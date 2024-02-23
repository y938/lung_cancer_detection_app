# lung_detection_app/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Prediction
import cv2
from tensorflow import keras
import numpy as np


model = keras.models.load_model('model2.h5')

def predict_lung_cancer(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].read()
        nparr = np.fromstring(image, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (192, 192))  # Adjust the size based on your model's input size
        img = np.expand_dims(img, axis=0)

        # Make prediction
        prediction = model.predict(img)
        confidence = np.max(prediction)
        classes = ['Adenocarcinomas', 'Normal', 'Squamous Cell Carcinomas'] 
        result = classes[np.argmax(prediction)]

        Prediction.objects.create(result=result, confidence=confidence)

        # Render the result directly in the view
        return render(request, 'result.html', {'result': result, 'confidence': confidence})

    return render(request, 'index.html')
