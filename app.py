from flask import Flask, request, jsonify, send_file
from transparent_background import Remover
from PIL import Image
import os
from datetime import datetime
from io import BytesIO

app = Flask(__name__)
remover = Remover()  # Use default model

def generate_filename():
    os.makedirs("done", exist_ok=True)
    return "done/" + datetime.now().strftime("output_%Y%m%d_%H%M%S_%f")[:-3] + ".png"

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = Image.open(request.files["image"]).convert("RGB")
    if image.width > 1500:
        image = image.resize((image.width // 2, image.height // 2))

    result = remover.process(image)
    filename = generate_filename()
    result.save(filename)

    return send_file(filename, mimetype="image/png")

@app.route("/")
def home():
    return "🎉 Background Remover API is running!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
