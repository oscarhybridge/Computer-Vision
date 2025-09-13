from flask import Flask, render_template, request
from deepface import DeepFace
import os

app = Flask(__name__)

# Carpeta con las imágenes registradas
USER_FOLDER = "users"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            # Guardar temporalmente la imagen subida
            temp_path = os.path.join("static", uploaded_file.filename)
            uploaded_file.save(temp_path)

            # Recorrer imágenes de usuarios y verificar
            verified_user = None
            for user_image in os.listdir(USER_FOLDER):
                user_path = os.path.join(USER_FOLDER, user_image)
                try:
                    res = DeepFace.verify(
                        img1_path=temp_path,
                        img2_path=user_path,
                        model_name="ArcFace",
                        detector_backend="retinaface"
                    )
                    if res["verified"]:
                        verified_user = user_image.split(".")[0]
                        break
                except Exception as e:
                    print(f"Error verificando {user_image}: {e}")

            if verified_user:
                result = f"✅ Bienvenido, {verified_user}."
            else:
                result = "❌ Acceso denegado."

            # Borrar imagen temporal
            os.remove(temp_path)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
