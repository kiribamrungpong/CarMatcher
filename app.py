from flask import Flask, render_template, request
from matcher import load_vehicles, find_matches, find_cheapest

app = Flask(__name__)

VEHICLE_TYPES = ["Sedan", "Coupe", "SUV", "Truck"]

BUDGET_ERROR = "Enter your budget using numbers only, and make it greater than  $0. For example: 30000"
TYPE_ERROR = "Choose a vehicle type to continue."


# Show a number as dollar value 
@app.template_filter("money")
def money(amount):
    return "$" + format(amount, ",")


# Home page - the search form
@app.route("/")
def home():
    # If the user came back from the results page, their answers are in the url
    budget = request.args.get("budget", "")
    body_type = request.args.get("body_type", "")

    return render_template("home.html",
                           budget=budget,
                           body_type=body_type)


# Results page
@app.route("/results")
def results():

    budget = request.args.get("budget", "")
    body_type = request.args.get("body_type", "")

    budget = budget.replace(",", "").replace("$", "").strip()

    budget_error = ""
    type_error = ""

    # The budget must be all digits and more than 0
    if budget.isdecimal() and int(budget) > 0:
        budget = int(budget)  
    else:
        budget_error = BUDGET_ERROR

    # The vehicle must be one of our four types
    if body_type not in VEHICLE_TYPES:
        type_error = TYPE_ERROR

    # error handling
    if budget_error != "" or type_error != "":
        return render_template("home.html",
                               budget=budget,
                               body_type=body_type,
                               budget_error=budget_error,
                               type_error=type_error)

    # find matching cars
    vehicles = load_vehicles()
    matches = find_matches(vehicles, budget, body_type)
    cheapest = find_cheapest(vehicles, body_type)

    return render_template("results.html",
                           matches=matches,      
                           budget=budget,        
                           body_type=body_type,  
                           cheapest=cheapest)    


# Start Over page
@app.route("/start-over")
def start_over():
    budget = request.args.get("budget", "")
    body_type = request.args.get("body_type", "")

    return render_template("start_over.html",
                           budget=budget,
                           body_type=body_type)


# Useful Tips page
@app.route("/tips")
def tips():
    return render_template("tips.html")
