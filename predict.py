from ultralytics import YOLO

model = YOLO("model.pt")

result = model.predict("C:/data/3.jpg", conf=0.3)
for item in result:
    for box in item.boxes:
        print(box.data[0])