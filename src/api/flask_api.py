import flask 
import pickle
import joblib
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

<<<<<<< HEAD
clf = pickle.load(open('../machine_learning/pickles/binary_extra_trees_2.sav', "rb"))
=======
clf_classifier = pickle.load(open('src/machine_learning/pickles/binary_extra_trees_2.sav', "rb"))
scaler_classifier = joblib.load("src/machine_learning/pickles/binary_extra_trees_scaler.sav")

clf_reg = pickle.load(open('src/machine_learning/pickles/gradient_regressor.sav', "rb"))
scaler_reg = joblib.load("src/machine_learning/pickles/gradient_regressor_scaler.sav")

>>>>>>> 37c24d1a2619c84d0c9a5e32d991259238c32f5a

@app.route("/getFireConfidence", methods=["GET"])
def getFireConfidence():
    AvgTemp = None
    Rainfall = None
    Windspeed = None
    Humidity = None
    Pressure = None
    lat = None
    lon = None
    regress = None
    
    # classifier arguments
    if "AvgTemp" in flask.request.args:
        AvgTemp = float(flask.request.args["AvgTemp"])
    if "Rainfall" in flask.request.args:
        Rainfall = float(flask.request.args["Rainfall"])
    if 'Windspeed' in flask.request.args:
        Windspeed = float(flask.request.args["Windspeed"])
    if 'Humidity' in flask.request.args:
        Humidity = float(flask.request.args["Humidity"])
    if 'Pressure' in flask.request.args:
        Pressure = float(flask.request.args["Pressure"])
    if 'lat' in flask.request.args:
        lat = float(flask.request.args["lat"])
    if 'long' in flask.request.args:
        lon = float(flask.request.args["long"])
    if 'regress' in flask.request.args:
        regress = float(flask.request.args["regress"])

    classifier_input = np.array([[AvgTemp, Rainfall, Windspeed, Humidity, Pressure, lat, lon]])
    classifier_input = scaler_classifier.transform(classifier_input)
    classifier_result = clf_classifier.predict(classifier_input)

    if (regress and classifier_result):
        brightness = None
        bright_t31 = None
        month = None

        if 'brightness' in flask.request.args:
            brightness = float(flask.request.args["brightness"])
        if 'bright_t31' in flask.request.args:
            bright_t31 = float(flask.request.args["bright_t31"])
        if 'month' in flask.request.args:
            month = float(flask.request.args["month"])

<<<<<<< HEAD
=======
        regressor_input = np.array([[lat, lon, month, brightness, bright_t31]])
        regressor_input = scaler_reg.transform(regressor_input)
        regressor_result = clf_reg.predict(regressor_input)

        return str(regressor_result[0])

    return str(classifier_result[0]) 
    
>>>>>>> 37c24d1a2619c84d0c9a5e32d991259238c32f5a
app.run()
