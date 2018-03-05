from flask import Flask, request, jsonify  # Flask Framework - Handles main GET and POST requests
import requests
from config import Config

app = Flask(__name__)
configs = Config()
api_key = configs.places_api_key #Put your Google Places API Key Here



@app.route("/api/search",methods=['GET', 'POST'])
def handle_fbrequests():
    placeTypes = {"Restaurant": "restaurant",
                  "Laundry": "laundry",
                  "ATM": "atm",
                  "Bank":"bank",
                  "Bus Station": "bus_station",
                  "Cafe": "cafe"}
    if request.method == "GET":
        index=1
        placeType = placeTypes[request.args.get("PlaceType")]
        longitude = request.args.get("longitude")
        latitude = request.args.get("latitude")
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/" \
              "json?location={0},{1}&radius=500&type={2}&key={3}".format(latitude, longitude, placeType, api_key)
        places = requests.get(url).json()
        elements = []
        if places['status'] == "ZERO_RESULTS":
            payload = {"messages":[
                {"text": "I can't find any places for your location. :("},
                {"text": "Do you want to try again?",
             "quick_replies": [{"title": "Yeah! :D","block_names": ["Search"]},
                               {"title": "Not now :(", "block_names": ["Thank You Msg"]}]}]}
        else:
            payload = {"messages": [
                {"text": "Here are the near by " + request.args.get("PlaceType") + " in your area. :)"},
                {"attachment": {"type": "template", "payload": {"template_type": "generic", "elements": []}}},
                {"text": "Do you want to search another place? ;)",
                 "quick_replies": [{"title": "Yeah! :D", "block_names": ["Search"]},
                                   {"title": "Not now :(", "block_names": ["Thank You Msg"]}]}]}
            for place in places['results']:
                if (len(places['results']) > 10) and (index == 11):
                    break
                elements.append({"title": place['name'],
                                 "image_url":"http://via.placeholder.com/1000x500/536DFE/ffffff?text={0}".format(place['name']),
                                 "subtitle":place['vicinity'],
                                 "buttons":[{"type":"element_share"}]})
                index += 1

            payload['messages'][1]['attachment']['payload']['elements'] = elements

        return jsonify(payload)
