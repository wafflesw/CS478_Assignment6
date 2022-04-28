from flask import Flask, jsonify, request
import numpy as np
from keras.models import  load_model
from keras.preprocessing import image
from datetime import date

# initialize our Flask application
app= Flask(__name__)

def get_model(): #function to get model so doesn't have to reload everytime server is called from client
    global model
    model = load_model('model.h5')
    print("Model is loaded")

@app.route("/predict", methods=["POST"]) #prediction call
def predict():
    data = request.get_json()
    data = data['data']
    img = image.load_img(data, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    #this part simply reads the position in the numpy array to determine the image classificaiton to return
    if classes[0,0] == 1.0:
        return jsonify(str("What you submitted was: paper"))
    if classes[0,1] == 1.0:
        return jsonify(str("What you submitted was: rock"))
    if classes[0,2] == 1.0:
        return jsonify(str("What you submitted was: scissors"))



@app.route("/hello", methods=["GET"]) #introduction
def hello():
    today = date.today()
    return jsonify(str("Rock Paper Scissors image classification server  James Weeden  " + str(today)))

if __name__=='__main__': #keeps the server going
    print("Model is loading...")
    get_model()
    app.run(debug=True)