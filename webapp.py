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
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')

@app.route('/showFragility')
def render_fact():
    states = get_state_options()
    state = request.args.get('country')
    #county = county_most_under_18(state)
    county1 = white(state)
    fact = "In " + state + ", the county with the highest percentage of under 18 year olds is " + county + "."
    fact1 = "in" + state + ", the country with the lowest percentage of white people is " + county1 + "."
    return render_template('home.html', state_options=states, funFact=fact, funFact1 = fact1)

def get_state_options():
    with open('state_fragility.json') as geographics_data:
        country = json.load(geographics_data)
    country=[]
    for c in country:
        if c["country"] not in country:
            country.append(c["country"])
    options=""
    for s in country:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options

if __name__=="__main__":
    app.run(debug=False)