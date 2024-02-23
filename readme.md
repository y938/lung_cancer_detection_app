# Lung Cancer Detection App

This Django web application utilizes a pre-trained deep learning model to predict lung cancer from chest X-ray images. The model has been trained to classify images into three classes: Adenocarcinomas, Normal, and Squamous Cell Carcinomas.

## Getting Started
you can get the trained model at my google drive https://drive.google.com/file/d/1srqILxGZqxfPYeJHVJcpIb2QCq8AIDb-/view?usp=sharing
- then add it in your project folder

### Prerequisites

- Python 3.x
- Django
- OpenCV
- TensorFlow
- numpy

### Usage

1. Clone the repository:

```bash
git clone https://github.com/y938/lung_detection_app.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Django development server:

```bash
python manage.py runserver
```

4. Visit http://localhost:8000/ in your web browser.

### Predicting Lung Cancer

1. Upload a chest X-ray image on the web interface.
2. The model will make a prediction and store the result and confidence in the database.
3. View the prediction result on the web page.

### Training the Model for Better Accuracy

To improve the model accuracy(i used free version of colab), you can train your own model using Google Colab. Follow these steps:

1. Open `lung.ipynb` in Google Colab.
2. Increase the image size and batch size for better accuracy.
3. Train the model and save it as `model2.h5`.
4. Replace the existing `model2.h5` with your newly trained model.

