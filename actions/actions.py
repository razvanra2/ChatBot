# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import datetime as dt

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json

with open("dataset/restaurant_db.json", "r") as read_file:
    restaurants = json.load(read_file)


class RestaurantAPI:
    def search(self, tracker: Tracker):
        food = tracker.get_slot("cuisine")

        area = tracker.get_slot("location")
        all_zones = ["centre", "north", "south", "east", "west"]
        area = all_zones if area not in all_zones else [area]

        pricerange = tracker.get_slot("price")
        pricerange = "cheap" if pricerange == "lo" else "expensive" if pricerange == "hi" else "moderate" if pricerange == "mid" else pricerange

        print(food, area, pricerange)
        options = [x for x in filter(lambda x: x["food"] == food and x["area"] in area and x["pricerange"] == pricerange, restaurants)]

        return options


class ActionSearchRestaurants(Action):

    def name(self):
        return "action_search_restaurants"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="looking for restaurants")
        restaurant_api = RestaurantAPI()
        res = restaurant_api.search(tracker)
        return [SlotSet("matches", res)]


class ActionSuggest(Action):
    def name(self):
        return "action_suggest"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        res = tracker.get_slot("matches")

        buttons = [{"title": x["name"], "payload": '/affirm{"name":"' + x["name"] + '"}'} for x in res] + [{"title": "No option", "payload": "/goodbye"}]
        dispatcher.utter_message(text="here's what I found:", buttons=buttons)

        return []
