import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time
from PIL import ImageTk, Image


# Train Image
def TrainImage(haarcasecade_path, trainimage_path, trainimagelabel_path, message,text_to_speech):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(haarcasecade_path)
    faces, Id = getImagesAndLables(trainimage_path)
    recognizer.train(faces, np.array(Id))
    recognizer.save(trainimagelabel_path)
    res = "Image Trained successfully"  # +",".join(str(f) for f in Id)
    message.configure(text=res)
    text_to_speech(res)


def getImagesAndLables(path):
    faces = []
    Ids = []
    if not os.path.exists(path):
        return faces, Ids
    
    for d in os.listdir(path):
        dir_path = os.path.join(path, d)
        if os.path.isdir(dir_path):
            for f in os.listdir(dir_path):
                if f.lower().endswith((".jpg", ".jpeg", ".png")):
                    image_file_path = os.path.join(dir_path, f)
                    try:
                        filename = os.path.basename(image_file_path)
                        # Expect format: Name_Enrollment_sampleNum.jpg
                        parts = filename.split("_")
                        if len(parts) >= 2:
                            Id = int(parts[1])
                            pilImage = Image.open(image_file_path).convert("L")
                            imageNp = np.array(pilImage, "uint8")
                            faces.append(imageNp)
                            Ids.append(Id)
                    except Exception as e:
                        print(f"Skipping file {f} due to error: {e}")
    return faces, Ids
