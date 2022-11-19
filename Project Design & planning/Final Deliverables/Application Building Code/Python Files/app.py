# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
 
app = Flask(_name_)  # initializing the app
model = pickle.load(open('CKD.pkl','wb')) #loading the model

@app.route('/') # route to display the home page
def home():
    return render_template('Home.html') # rendering the home page

@app.route('/prediction',methods=['POSt','GET'])
def prediction(): # route to display prediction page
    return render_template('indexnew.html')

@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('Home.html') # rendering the home page

@app.route('/predict',methods=['POST']) # route to show the prediction in web UI     
def predict():
    # reading the inputs given by the user
    inputs_features = [float(x) for x in request.form.values()] 
    features_value = [np.array(inputs_features)]

    features_name = ['age','pc','bu','rbc','dm','cad','pe','ane']
     
    df = pd.DataFrame(features_value, columns=features_name)

    output = model.predict(df) # prediction using the loaded model file
    b=[1]
    # showing the prediction results in a UI
    if(output==b):
        return render_template("Result.html")
    else:
        return render_template("Resultf.html")

    # showing the prediction results in a UI
    

if _name_ == "_main_":
    app.run(debug=True) # running the app