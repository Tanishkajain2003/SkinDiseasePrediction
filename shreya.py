# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 04:03:06 2023

@author: TANISHKA
"""
import numpy as np
from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input

app = Flask(__name__)

dic = {'ACNE': 0, 'ECZEMA': 1, 'KELOIDALIS_ACNE_(YOU_WILL_SUFFER_FROM_HAIRLOSS)': 2, 'MELANOMA_SKIN_CANCER': 3, 'NAIL_FUNGUS': 4}

model = load_model(r"C:\Users\TANISHKA\OneDrive\Documents\Skindiseaseprediction.keras")

model.make_predict_function()

def predict_label(img_path):
       img = image.load_img(img_path, target_size=(224,224))
       img_array = image.img_to_array(img)
       expanded_img_array = np.expand_dims(img_array, axis=0)
       preprocessed_img = preprocess_input(expanded_img_array) # Preprocess the image
       prediction = model.predict(preprocessed_img)
       highest=prediction.argmax()
       result=list(dic.keys())[list(dic.values()).index(highest)]
       return result

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("tanishka.html")

@app.route("/about")
def about_page():
    return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        global p
        img_path = "static/" + img.filename    
        img.save(img_path)
        
        p = predict_label(img_path)

    return render_template("tanishka.html", prediction = p , img_path = img_path)

    

if __name__ =='__main__':
    #app.debug = True
    app.run(debug = True)
