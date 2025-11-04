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
    country = request.args.get('country')
    year = request.args.get('year')
    State_Fragility_Indexs = fragility_index(country, year)
    countries = get_country_options()
    years = get_year_options()
    return render_template('page1.html', country_options=countries, year_options=years)

@app.route("/p2")
def render_page2():
    country = request.args.get('country')
    year = request.args.get('year')
    effectiveness = effectiveness_index(country, year)
    countries = get_country_options()
    years = get_year_options()
    return render_template('page2.html', country_options=countries, year_options=years)

@app.route("/p3")
def render_page3():
    return render_template('page3.html')


@app.route('/showFragility')
def render_fact():
    countries = get_country_options()
    country = request.args.get('country')
    years = get_year_options()
    year = request.args.get('year')
    State_Fragility_Indexs = fragility_index(country, year)
    effectiveness = effectiveness_index(country, year)
    Fragile1 = "In " + str(country) + ", " + "in the year " + str(year) + " The fragility is " + str(State_Fragility_Indexs) + "." #used ai to add str cause I was actin like a dingleberry and forgot how to fix it ai: https://www.perplexity.ai/search/i-got-the-error-can-only-conca-lwcYFVcxQXKBZE9JvUG90w 
    Fragile2 = "In " + str(country) + ", " + "in the year " + str(year) + " The effectiveness of the government us is " + str(effectiveness) + "."
    return render_template('page1.html', year_options=years, country_options=countries, Fragility1=Fragile1, Fragility2=Fragile2)
    
    
@app.route('/showEffectiveness')
def render_fact1():
    countries = get_country_options()
    country = request.args.get('country')
    years = get_year_options()
    year = request.args.get('year')
    State_Fragility_Indexs = fragility_index(country, year)
    effectiveness = effectiveness_index(country, year)
    Fragile1 = "In " + str(country) + ", " + "in the year " + str(year) + " The fragility is " + str(State_Fragility_Indexs) + "." #used ai to add str cause I was actin like a dingleberry and forgot how to fix it ai: https://www.perplexity.ai/search/i-got-the-error-can-only-conca-lwcYFVcxQXKBZE9JvUG90w 
    Fragile2 = "In " + str(country) + ", " + "in the year " + str(year) + " The effectiveness of the government us is " + str(effectiveness) + "."
    return render_template('page2.html', year_options=years, country_options=countries, Fragility1=Fragile1, Fragility2=Fragile2)

def get_country_options():
    with open('state_fragility.json') as fragility_data:
        years = json.load(fragility_data)
    countries=[]
    for c in years:
        if c["Country"] not in countries:
            countries.append(c["Country"])
    options=""
    for s in countries:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>")
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
        options += Markup("<option value=\"" + str(s) + "\">" + str(s) + "</option>")
    return options

def fragility_index(country, year):
    with open('state_fragility.json') as fragility_data:
        countries = json.load(fragility_data)
    metric = ""
    for c in countries: 
        if c["Country"] == country and str(c["Year"]) == str(year):
            return c["Metrics"]["State Fragility Index"]
    return None
    
def effectiveness_index(country, year):
    with open('state_fragility.json') as fragility_data:
        countries = json.load(fragility_data)
    metric = ""
    for c in countries: 
        if c["Country"] == country and str(c["Year"]) == str(year):
            return c["Metrics"]["Effectiveness"]["Effectiveness Score"]
    return None
    

if __name__=="__main__":
    app.run(debug=False)