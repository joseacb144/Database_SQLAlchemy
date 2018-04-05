from flask import Flask, jsonify
import os
import pandas as pd
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Call SQLite
engine = create_engine('sqlite:///hawaii.sqlite')

# Create Base
Base = automap_base()
Base.prepare(engine, reflect = True)

# Read Measurement and Station Tables 
Measurement = Base.classes.measurement
Station = Base.classes.station

# Connect
session = Session(engine)

# Define App
app = Flask(__name__)

# Opne Saved Dic Files
with open('temp_dates_dict.json', 'r') as fp:
    precipitation_data = json.load(fp)

with open('stations_info_dict.json', 'r') as st:
    stations_data = json.load(st)

# Create Routes
@app.route("/")

# Welcoming Page
def welcome():
    return(

        f"Climate Analysis and Exploration of Hawaii! <br/>"

        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<start>/<end> <br/>"

        
    )

@app.route("/api/v1.0/precipitation")

def precipitation():
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")

def stations():
    return jsonify(stations_data)

@app.route("/api/v1.0/tobs")

def tobs():
    return jsonify(tobs_data)

if __name__=="__main__":
    app.run(debug=True)