# Proyecto 6: Computer Vision

*Escribe aquí una breve descripción de tu proyecto*

*Escribe un instructivo de cómo podemos utilizar tu software (incluye instrucciones para crear entorno virtual)*


requirements.txt
Flask
deepface
opencv-python
tensorflow
tf-keras


Carpeta users/

Coloca ahí imágenes de los usuarios permitidos para acceder.
Por ejemplo:

users/oscar.jpg
users/ana.jpg




---------Cómo ejecutar

Crear y activar entorno virtual:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Instalar dependencias:

pip install -r requirements.txt


Ejecutar la app:

python app.py


Abrir navegador:
http://127.0.0.1:5000

Sube una foto de tu cara para probar login, previamente registrada o subida en la carpeta users/
o bien te puedes tomar una foto desde la webcam y probar login.
