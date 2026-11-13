import json


# Read the cars from vehicles.json and return them as a list
def load_vehicles():
    with open("vehicles.json") as file:
        vehicles = json.load(file)
    return vehicles


# use sort to put the cars in order by price
def get_price(vehicle):
    return vehicle["price"]


# Return the cars of this type that cost the budget or less - cheapest first
def find_matches(vehicles, budget, body_type):
    matches = []
    for vehicle in vehicles:
        if vehicle["body_type"] == body_type and vehicle["price"] <= budget:
            matches.append(vehicle)

    matches.sort(key=get_price)
    return matches


# Return the cheapest car of this type when nothing matches
def find_cheapest(vehicles, body_type):
    cheapest = None
    for vehicle in vehicles:
        if vehicle["body_type"] == body_type:
            if cheapest is None or vehicle["price"] < cheapest["price"]:
                cheapest = vehicle
    return cheapest
