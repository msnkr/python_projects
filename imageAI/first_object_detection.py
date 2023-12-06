from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(os.path.join(
    execution_path, "imageAI/tiny-yolov3.pt"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(
    execution_path, "imageAI/images/unsplash-3.jpg"), output_image_path=os.path.join(execution_path, "imageAI/images/image2new.jpg"), minimum_percentage_probability=10)

for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"],
          " : ", eachObject["box_points"])
    print("--------------------------------")
