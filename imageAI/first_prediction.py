from imageai.Classification import ImageClassification
import os

execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsInceptionV3()
prediction.setModelPath(os.path.join(
    execution_path, "imageAI\inception_v3_google-1a9a5a14.pth"))

prediction.loadModel()
predictions, probabilities = prediction.classifyImage(
    os.path.join(execution_path, "imageAI\images\\rhino.jpeg"), result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)
