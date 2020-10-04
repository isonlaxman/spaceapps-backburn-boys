import flask 
import pickle

app = flask.Flask(__name__)
app.config["DEBUG"] = True

clf = pickle.load(open('../machine_learning/pickles/binary_extra_trees_2.sav', "rb"))

@app.route("/getFireConfidence", methods=["GET"])
def getFireConfidence():
    AvgTemp = None
    Rainfall = None
    Windspeed = None
    Humidity = None
    Pressure = None
    lat = None
    lon = None
    
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

    result = clf.predict([[AvgTemp, Rainfall, Windspeed, Humidity, Pressure, lat, lon]])
    
    return str(result[0]) 

app.run()
