from flask import Flask, request
from flask_cors import CORS
from ultralytics import YOLO
from PIL import Image
import io

app = Flask(__name__)

CORS(app)

model = YOLO("model.pt")


@app.route('/', methods=['POST'])
def index():
    try:
        if 'file' not in request.files or not request.files['file']:
            return {"message": "파일을 업로드 하세요."}, 400

        file = request.files['file']
        
        image = Image.open(io.BytesIO(file.read()))

        result = model.predict(source=image)
        items = [box.data[0].tolist() for item in result for box in item.boxes]
        return items
    except Exception as e:
        return {"message": str(e)}, 500
