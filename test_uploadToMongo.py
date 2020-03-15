from pymongo import MongoClient
from credentials import mongoDBUrl
from pprint import pprint

client = MongoClient(mongoDBUrl, retrywrites=False)

db = client["cpf-neumorphic"]

users = db["users"]

user_data = {
    "Feature": {
        "age": "22",
        "gender": "female",
        "income": "4212",
        "job_industry": "real_estate_services",
    },
    "NRIC": "S9899697V",
    "Name": "Elizabeth Meyer",
    "Recommendation": [
        {"duration": "13.9828727120516", "page_id": "4"},
        {"duration": "12.6312804019084", "page_id": "8"},
        {"duration": "12.3197395613409", "page_id": "5"},
    ],
    "Usage": [
        {"page_id": "7", "time_spent": "4"},
        {"page_id": "0", "time_spent": "12"},
        {"page_id": "5", "time_spent": "15"},
        {"page_id": "4", "time_spent": "19"},
    ],
}

users.insert_one(user_data)
