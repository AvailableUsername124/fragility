from flask import Flask, url_for, render_template, request
from markupsafe import Markup

import random
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('fragile.html')

@app.route("/p1")
def render_page1():
    
    State_Fragility_Indexs = fragility_index()
    countries = get_country_options()
    years = get_year_options()
    return render_template('page1.html', country_options=countries, year_options=years)

@app.route("/p2")
def render_page2():
    return render_template('page2.html')

@app.route('/showFragility')
def render_fact():
    countries = get_country_options()
    country = request.args.get('country','')
    years = get_year_options()
    year = request.args.get('year', '')
    State_Fragility_Indexs = fragility_index()
    State_Fragility_Index = request.args.get('State Fragility Index', '')
    #county = county_most_under_18(state)
    #county1 = white(state)
    Fragile1 = "In " + country + ", " + "The fragility is " + year + "."
    Fragile2 = "In " + country + ", " "the fragility is " + year + "."
    return render_template('page1.html', country_options=countries, Fragility1=Fragile1, Fragility2 = Fragile2)

def get_country_options():
    with open('state_fragility.json') as fragility_data:
        years = json.load(fragility_data)
    countries=[]
    for c in years:
        if c["Country"] not in countries:
            countries.append(c["Country"])
    options=""
    for s in countries:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options

def get_year_options():
    with open('state_fragility.json') as fragility_data:
        countries = json.load(fragility_data)
    years=[]
    for c in countries:
        if c["Year"] not in years:
            years.append(c["Year"])
    options=""
    for s in years:
        options += Markup("<option value=\"" + str(s) + "\">" + str(s) + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options

def fragility_index():
    with open('state_fragility.json') as fragility_data:
        countries = json.load(fragility_data)
    State_Fragility_Indexs=[]
    for c in countries:
        if c["Metrics"]["State Fragility Index"] not in State_Fragility_Indexs:
            State_Fragility_Indexs.append(c["Metrics"]["State Fragility Index"])
    options=""
    for s in State_Fragility_Indexs:
        options += Markup("<option value=\"" + str(s) + "\">" + str(s) + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options



if __name__=="__main__":
    app.run(debug=True)