import numpy as np
from tensorflow.keras.preprocessing import image
import os

def predict_images(model, img_path, classes, target_size=(64,64)):

    if not os.path.exists(img_path):
        raise FileNotFoundError(f"File Tidak Ditemukan: {img_path}")
    
    img=image.load_img(img_path, target_size=target_size)
    img_array=image.img_to_array(img)
    img_array=np.expand_dims(img_array, axis=0)
    img_array=img_array/ 255.0

    prediction=model.predict(img_array)
    class_index=np.argmax(prediction)
    confidence=np.max(prediction)
    result=classes[class_index]

    return result ,confidence