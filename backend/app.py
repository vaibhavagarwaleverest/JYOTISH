# from flask import Flask, request, jsonify
# from vedastro import *
# from geopy.geocoders import Nominatim
# from flask_cors import CORS
# from astrapy import DataAPIClient
# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()
# # Set your OpenAI API key
# openai_api_key = os.getenv("OPENAI_API_KEY")
# astra_db_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
# astra_db_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
# astra_db_collection = os.getenv("ASTRA_DB_COLLECTION_NAME")
# # Initialize the Astra DB client
# client = DataAPIClient(astra_db_token)
# database = client.get_database(astra_db_endpoint)
# collection = database.get_collection(astra_db_collection)
# app = Flask(__name__)
# CORS(app,resources={r"/detail": {"origins": "*", "allow_headers": ["Content-Type", "Token"]}})
# def flatten_dict(d, parent_key='', sep=' '):
#     """
#     Flatten a nested dictionary into a single-level dictionary.
#     """

#     items = []
#     for k, v in d.items():
#         new_key = f"{parent_key}{sep}{k}" if parent_key else k
#         if isinstance(v, dict):
#             items.extend(flatten_dict(v, new_key, sep=sep).items())
#         else:
#             items.append((new_key, v))
#     return dict(items)

# def dict_to_text(data):
#     """
#     Convert a dictionary into a text string.
#     """
#     flattened = flatten_dict(data)
#     text = ". ".join([f"{k}: {v}" for k, v in flattened.items()])
#     return text
# @app.route("/detail", methods=["POST"])
# def func():
#     try:
#         # Get JSON data from the request
#         data = request.json

#         # Extract user inputs
#         name = data['name']
#         dob = data['dob']
#         time = data['time']
#         gender = data['gender']
#         state = data['state']
#         city = data['city']

#         # Get latitude and longitude using geopy
#         geolocator = Nominatim(user_agent="my_geocoding_app")
#         location_name = city + ", " + "India"
#         location = geolocator.geocode(location_name)

#         if location:
#             longitude = location.longitude
#             latitude = location.latitude
#         else:
#             return jsonify({"error": "Location not found"}), 400

#         # Create GeoLocation object
#         geolocation = GeoLocation(city + ", " + "India", longitude, latitude)

#         # Create Time object
#         time1 = time + " " + dob + " " + "+8:00"
#         birth_time = Time(time1, geolocation)

#         # Calculate planet data
#         allPlanetDataList = Calculate.AllPlanetData(PlanetName.Sun, birth_time)

#         # Define the keys for planet data
#         planet_keys = [
#             "BouncBackInputPlanet",
#             "HousePlanetOccupies",
#             "HousePlanetOccupiesBasedOnSign",
#             "HousesInAspect",
#             "HousesOwnedByPlanet",
#             "IsPlanetAspectedByBeneficPlanets",
#             "IsPlanetAspectedByEnemyPlanets",
#             "IsPlanetAspectedByFriendPlanets",
#             "IsPlanetAspectedByMaleficPlanets",
#             "IsPlanetBenefic",
#             "IsPlanetConjunctWithEnemyPlanets",
#             "IsPlanetConjunctWithFriendPlanets",
#             "IsPlanetConjunctWithMaleficPlanets",
#             "IsPlanetDebilitated",
#             "IsPlanetExalted",
#             "IsPlanetInEnemyHouse",
#             "IsPlanetInFriendHouse",
#             "IsPlanetInGarvitaAvasta",
#             "IsPlanetInKendra",
#             "IsPlanetInKshobhitaAvasta",
#             "IsPlanetInKshuditaAvasta",
#             "IsPlanetInLajjitaAvasta",
#             "IsPlanetInMoolatrikona",
#             "IsPlanetInMuditaAvasta",
#             "IsPlanetInOwnHouse",
#             "IsPlanetInTrashitaAvasta",
#             "IsPlanetInTrikona",
#             "IsPlanetInUpachaya",
#             "IsPlanetInWaterySign",
#             "IsPlanetMalefic",
#             "IsPlanetRetrograde",
#             "IsPlanetStrongInShadbala",
#             "PlanetAbdaBala",
#             "PlanetAkshavedamshaD45Sign",
#             "PlanetAvasta",
#             "PlanetAyanaBala",
#             "PlanetBhamshaD27Sign",
#             "PlanetChaturthamshaD4Sign",
#             "PlanetChaturvimshamshaD24Sign",
#             "PlanetConstellation",
#             "PlanetDashamamshaD10Sign",
#             "PlanetDeclination",
#             "PlanetDigBala",
#             "PlanetDrekkanaBala",
#             "PlanetDrekkanaD3Sign",
#             "PlanetDrikBala",
#             "PlanetDwadashamshaD12Sign",
#             "PlanetDwadashamshaSignOLD",
#             "PlanetEphemerisLongitude",
#             "PlanetHoraBala",
#             "PlanetHoraD2Signs",
#             "PlanetIshtaKashtaScore",
#             "PlanetIshtaKashtaScoreDegree",
#             "PlanetIshtaScore",
#             "PlanetKalaBala",
#             "PlanetKashtaScore",
#             "PlanetKendraBala",
#             "PlanetKhavedamshaD40Sign",
#             "PlanetLordOfConstellation",
#             "PlanetLordOfZodiacSign",
#             "PlanetMasaBala",
#             "PlanetMotionName",
#             "PlanetNaisargikaBala",
#             "PlanetNathonnathaBala",
#             "PlanetNatureScore",
#             "PlanetNatureScoreMK4",
#             "PlanetNavamshaD9Sign",
#             "PlanetNirayanaLongitude",
#             "PlanetOchchaBala",
#             "PlanetOjayugmarasyamsaBala",
#             "PlanetPakshaBala",
#             "PlanetPowerPercentage",
#             "PlanetSaptamshaD7Sign",
#             "PlanetSaptamshaSignOLD",
#             "PlanetSaptavargajaBala",
#             "PlanetsAspectingPlanet",
#             "PlanetSayanaLatitude",
#             "PlanetSayanaLongitude",
#             "PlanetShadbalaPinda",
#             "PlanetShashtyamshaD60Sign",
#             "PlanetShodashamshaD16Sign",
#             "PlanetsInAspect",
#             "PlanetsInConjuction",
#             "PlanetSpeed",
#             "PlanetSthanaBala",
#             "PlanetStrength",
#             "PlanetTemporaryFriendList",
#             "PlanetTribhagaBala",
#             "PlanetTrimshamshaD30Sign",
#             "PlanetVaraBala",
#             "PlanetVimshamshaD20Sign",
#             "PlanetZodiacSign",
#             "ResidentialStrength",
#             "SignsPlanetIsAspecting",
#             "SwissEphemeris"
#         ]

#         # Convert planet data to key-value pairs
#         planet_data = {}
#         for i, value in enumerate(allPlanetDataList):
#             if i < len(planet_keys):
#                 planet_data[planet_keys[i]] = str(value)

#         # Calculate house data
#         allHouseDataList = Calculate.AllHouseData(HouseName.House1, birth_time)

#         # Define the keys for house data
#         house_keys = [
#             "HouseAkshavedamshaD45Sign",
#             "HouseBhamshaD27Sign",
#             "HouseChaturthamshaD4Sign",
#             "HouseChaturvimshamshaD24Sign",
#             "HouseConstellation",
#             "HouseConstellationLord",
#             "HouseDashamamshaD10Sign",
#             "HouseDrekkanaD3Sign",
#             "HouseDwadashamshaD12Sign",
#             "HouseHoraD2Sign",
#             "HouseKhavedamshaD40Sign",
#             "HouseLongitude",
#             "HouseNatureScore",
#             "HouseNatureScoreMK4",
#             "HouseNavamshaD9Sign",
#             "HouseSaptamshaD7Sign",
#             "HouseShashtyamshaD60Sign",
#             "HouseShodashamshaD16Sign",
#             "HouseSignName",
#             "HouseStrength",
#             "HouseTrimshamshaD30Sign",
#             "HouseVimshamshaD20Sign",
#             "HouseZodiacSign",
#             "IsBeneficPlanetAspectHouse",
#             "IsBeneficPlanetInHouse",
#             "IsMaleficPlanetAspectHouse",
#             "IsMaleficPlanetInHouse",
#             "LordOfHouse",
#             "PlanetsAspectingHouse",
#             "PlanetsInHouse",
#             "PlanetsInHouseBasedOnSign"
#         ]

#         # Convert house data to key-value pairs
#         house_data = {}
#         for i, value in enumerate(allHouseDataList):
#             if i < len(house_keys):
#                 house_data[house_keys[i]] = str(value)
#         allZodiacDataList = Calculate.AllZodiacSignData(ZodiacName.Gemini, birth_time)

#         # Define the keys for zodiac data
#         zodiac_keys = [
#             "BeneficPlanetListInSign",
#             "DestinyPoint",
#             "FortunaPoint",
#             "HouseFromSignName",
#             "IsBeneficPlanetInSign",
#             "IsMaleficPlanetInSign",
#             "MaleficPlanetListInSign",
#             "PlanetInSign",
#             "PlanetsInSign"
#         ]

#         # Convert zodiac data to key-value pairs
#         zodiac_data = {}
#         for i, value in enumerate(allZodiacDataList):
#             if i < len(zodiac_keys):
#                 zodiac_data[zodiac_keys[i]] = str(value)

#         # Prepare the response in JSON format
#         response = {
#             "name": name,
#             "dob": dob,
#             "time": time,
#             "gender": gender,
#             "state": state,
#             "city": city,
#             "latitude": latitude,
#             "longitude": longitude,
#             "planet_data": planet_data,
#             "house_data": house_data,
#             "zodiac_data":zodiac_data
#         }
#         text_to_vectorize = dict_to_text(response)
#         client = OpenAI(api_key=openai_api_key)
#         response = client.embeddings.create(
#             input=text_to_vectorize,
#             model="text-embedding-3-large"
#         )
#         vector_embedding = response.data[0].embedding

#     # Insert the document with the vector embedding
#         # result = collection.insert_one(
#         #     {
#         #         "name": name,
#         #         "city": city,
#         #         "dob": dob,
#         #         "gender": gender,
#         #         "house_data": house_data,
#         #         "planet_data": planet_data,
#         #         "zodiac_data": zodiac_data,
#         #         "$vector": vector_embedding  # Add the vector embedding
#         #     }
#         # )
#         metadata = {
#     "timestamp": "2023-10-15T12:34:56Z",  # Timestamp of insertion
#     "source": "user_input",  # Source of the data
#     "version": "1.0"  # Version of the data
# }
#         result = collection.insert_one(
#             {
#                 "content":str([{"name": name,
#                 "city": city,
#                 "dob": dob,
#                 "gender": gender,
#                 "house_data": house_data,
#                 "planet_data": planet_data,
#                 "zodiac_data": zodiac_data,
#                 }])
#                ,
#                 "$vector": vector_embedding,
#                   "metadata": metadata  # Add the vector embedding
#             }
#         )
    

#         # Return the response as JSON
#         return jsonify(result)

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__== "__main__":
#     app.run(debug=True, port=5001)

from flask import Flask, request, jsonify
from vedastro import *
from geopy.geocoders import Nominatim
from flask_cors import CORS
from astrapy import DataAPIClient
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Set your OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
astra_db_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
astra_db_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
astra_db_collection = os.getenv("ASTRA_DB_COLLECTION_NAME")
# Initialize the Astra DB client
client = DataAPIClient(astra_db_token)
database = client.get_database(astra_db_endpoint)
collection = database.get_collection(astra_db_collection)
app = Flask(__name__)
CORS(app, resources={r"/detail": {"origins": "*", "allow_headers": ["Content-Type", "Token"]}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

def flatten_dict(d, parent_key='', sep=' '):
    """
    Flatten a nested dictionary into a single-level dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def dict_to_text(data):
    """
    Convert a dictionary into a text string.
    """
    flattened = flatten_dict(data)
    text = ". ".join([f"{k}: {v}" for k, v in flattened.items()])
    return text

@app.route("/detail", methods=["POST", "OPTIONS"])
def func():
    if request.method == "OPTIONS":
        # Handle preflight request
        response = jsonify({"status": "success"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Token')
        response.headers.add('Access-Control-Allow-Methods', 'POST,OPTIONS')
        return response
    else:
        try:
            # Get JSON data from the request
            data = request.json

            # Extract user inputs
            name = data['name']
            dob = data['dob']
            time = data['time']
            gender = data['gender']
            state = data['state']
            city = data['city']

            # Get latitude and longitude using geopy
            geolocator = Nominatim(user_agent="my_geocoding_app")
            location_name = city + ", " + "India"
            location = geolocator.geocode(location_name)

            if location:
                longitude = location.longitude
                latitude = location.latitude
            else:
                return jsonify({"error": "Location not found"}), 400

            # Create GeoLocation object
            geolocation = GeoLocation(city + ", " + "India", longitude, latitude)

            # Create Time object
            time1 = time + " " + dob + " " + "+8:00"
            birth_time = Time(time1, geolocation)

            # Calculate planet data
            allPlanetDataList = Calculate.AllPlanetData(PlanetName.Sun, birth_time)

            # Define the keys for planet data
            planet_keys = [
                "BouncBackInputPlanet",
                "HousePlanetOccupies",
                "HousePlanetOccupiesBasedOnSign",
                "HousesInAspect",
                "HousesOwnedByPlanet",
                "IsPlanetAspectedByBeneficPlanets",
                "IsPlanetAspectedByEnemyPlanets",
                "IsPlanetAspectedByFriendPlanets",
                "IsPlanetAspectedByMaleficPlanets",
                "IsPlanetBenefic",
                "IsPlanetConjunctWithEnemyPlanets",
                "IsPlanetConjunctWithFriendPlanets",
                "IsPlanetConjunctWithMaleficPlanets",
                "IsPlanetDebilitated",
                "IsPlanetExalted",
                "IsPlanetInEnemyHouse",
                "IsPlanetInFriendHouse",
                "IsPlanetInGarvitaAvasta",
                "IsPlanetInKendra",
                "IsPlanetInKshobhitaAvasta",
                "IsPlanetInKshuditaAvasta",
                "IsPlanetInLajjitaAvasta",
                "IsPlanetInMoolatrikona",
                "IsPlanetInMuditaAvasta",
                "IsPlanetInOwnHouse",
                "IsPlanetInTrashitaAvasta",
                "IsPlanetInTrikona",
                "IsPlanetInUpachaya",
                "IsPlanetInWaterySign",
                "IsPlanetMalefic",
                "IsPlanetRetrograde",
                "IsPlanetStrongInShadbala",
                "PlanetAbdaBala",
                "PlanetAkshavedamshaD45Sign",
                "PlanetAvasta",
                "PlanetAyanaBala",
                "PlanetBhamshaD27Sign",
                "PlanetChaturthamshaD4Sign",
                "PlanetChaturvimshamshaD24Sign",
                "PlanetConstellation",
                "PlanetDashamamshaD10Sign",
                "PlanetDeclination",
                "PlanetDigBala",
                "PlanetDrekkanaBala",
                "PlanetDrekkanaD3Sign",
                "PlanetDrikBala",
                "PlanetDwadashamshaD12Sign",
                "PlanetDwadashamshaSignOLD",
                "PlanetEphemerisLongitude",
                "PlanetHoraBala",
                "PlanetHoraD2Signs",
                "PlanetIshtaKashtaScore",
                "PlanetIshtaKashtaScoreDegree",
                "PlanetIshtaScore",
                "PlanetKalaBala",
                "PlanetKashtaScore",
                "PlanetKendraBala",
                "PlanetKhavedamshaD40Sign",
                "PlanetLordOfConstellation",
                "PlanetLordOfZodiacSign",
                "PlanetMasaBala",
                "PlanetMotionName",
                "PlanetNaisargikaBala",
                "PlanetNathonnathaBala",
                "PlanetNatureScore",
                "PlanetNatureScoreMK4",
                "PlanetNavamshaD9Sign",
                "PlanetNirayanaLongitude",
                "PlanetOchchaBala",
                "PlanetOjayugmarasyamsaBala",
                "PlanetPakshaBala",
                "PlanetPowerPercentage",
                "PlanetSaptamshaD7Sign",
                "PlanetSaptamshaSignOLD",
                "PlanetSaptavargajaBala",
                "PlanetsAspectingPlanet",
                "PlanetSayanaLatitude",
                "PlanetSayanaLongitude",
                "PlanetShadbalaPinda",
                "PlanetShashtyamshaD60Sign",
                "PlanetShodashamshaD16Sign",
                "PlanetsInAspect",
                "PlanetsInConjuction",
                "PlanetSpeed",
                "PlanetSthanaBala",
                "PlanetStrength",
                "PlanetTemporaryFriendList",
                "PlanetTribhagaBala",
                "PlanetTrimshamshaD30Sign",
                "PlanetVaraBala",
                "PlanetVimshamshaD20Sign",
                "PlanetZodiacSign",
                "ResidentialStrength",
                "SignsPlanetIsAspecting",
                "SwissEphemeris"
            ]

            # Convert planet data to key-value pairs
            planet_data = {}
            for i, value in enumerate(allPlanetDataList):
                if i < len(planet_keys):
                    planet_data[planet_keys[i]] = str(value)

            # Calculate house data
            allHouseDataList = Calculate.AllHouseData(HouseName.House1, birth_time)

            # Define the keys for house data
            house_keys = [
                "HouseAkshavedamshaD45Sign",
                "HouseBhamshaD27Sign",
                "HouseChaturthamshaD4Sign",
                "HouseChaturvimshamshaD24Sign",
                "HouseConstellation",
                "HouseConstellationLord",
                "HouseDashamamshaD10Sign",
                "HouseDrekkanaD3Sign",
                "HouseDwadashamshaD12Sign",
                "HouseHoraD2Sign",
                "HouseKhavedamshaD40Sign",
                "HouseLongitude",
                "HouseNatureScore",
                "HouseNatureScoreMK4",
                "HouseNavamshaD9Sign",
                "HouseSaptamshaD7Sign",
                "HouseShashtyamshaD60Sign",
                "HouseShodashamshaD16Sign",
                "HouseSignName",
                "HouseStrength",
                "HouseTrimshamshaD30Sign",
                "HouseVimshamshaD20Sign",
                "HouseZodiacSign",
                "IsBeneficPlanetAspectHouse",
                "IsBeneficPlanetInHouse",
                "IsMaleficPlanetAspectHouse",
                "IsMaleficPlanetInHouse",
                "LordOfHouse",
                "PlanetsAspectingHouse",
                "PlanetsInHouse",
                "PlanetsInHouseBasedOnSign"
            ]

            # Convert house data to key-value pairs
            house_data = {}
            for i, value in enumerate(allHouseDataList):
                if i < len(house_keys):
                    house_data[house_keys[i]] = str(value)

            allZodiacDataList = Calculate.AllZodiacSignData(ZodiacName.Gemini, birth_time)

            # Define the keys for zodiac data
            zodiac_keys = [
                "BeneficPlanetListInSign",
                "DestinyPoint",
                "FortunaPoint",
                "HouseFromSignName",
                "IsBeneficPlanetInSign",
                "IsMaleficPlanetInSign",
                "MaleficPlanetListInSign",
                "PlanetInSign",
                "PlanetsInSign"
            ]

            # Convert zodiac data to key-value pairs
            zodiac_data = {}
            for i, value in enumerate(allZodiacDataList):
                if i < len(zodiac_keys):
                    zodiac_data[zodiac_keys[i]] = str(value)

            # Prepare the response in JSON format
            response = {
                "name": name,
                "dob": dob,
                "time": time,
                "gender": gender,
                "state": state,
                "city": city,
                "latitude": latitude,
                "longitude": longitude,
                "planet_data": planet_data,
                "house_data": house_data,
                "zodiac_data": zodiac_data
            }
            text_to_vectorize = dict_to_text(response)
            client = OpenAI(api_key=openai_api_key)
            response = client.embeddings.create(
                input=text_to_vectorize,
                model="text-embedding-3-large"
            )
            vector_embedding = response.data[0].embedding

            # Insert the document with the vector embedding
            metadata = {
                "timestamp": "2023-10-15T12:34:56Z",  # Timestamp of insertion
                "source": "user_input",  # Source of the data
                "version": "1.0"  # Version of the data
            }
            result = collection.insert_one(
                {
                    "content": str([{"name": name,
                                    "city": city,
                                    "dob": dob,
                                    "gender": gender,
                                    "house_data": house_data,
                                    "planet_data": planet_data,
                                    "zodiac_data": zodiac_data,
                                    }]),
                    "$vector": vector_embedding,
                    "metadata": metadata  # Add the vector embedding
                }
            )

            # Return the response as JSON
            return jsonify(result)

        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)