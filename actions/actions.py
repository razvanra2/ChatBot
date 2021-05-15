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

class RestaurantAPI:
    def search(self, info):
        return "papi's pizza place"


class ActionSearchRestaurants(Action):
    def name(self):
        return "action_search_restaurants"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="looking for restaurants")
        restaurant_api = RestaurantAPI()
        restaurants = restaurant_api.search(tracker.get_slot("cuisine"))
        return [SlotSet("matches", restaurants)]


class ActionSuggest(Action):
    def name(self):
        return "action_suggest"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="here's what I found:")
        dispatcher.utter_message(text=tracker.get_slot("matches"))
        dispatcher.utter_message(
            text="is it ok for you? hint: I'm not going to find anything else :)"
        )
        return []
