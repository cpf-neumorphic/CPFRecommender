import csv
from faker import Faker
from pprint import pprint
from pymongo import MongoClient
from time import sleep

faker = Faker()
formatted_data = {}

with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row[0] == "NRIC":
            continue

        NRIC, page_id, time_spent = row
        usage = {"page_id": page_id, "time_spent": time_spent}

        if NRIC not in formatted_data:
            formatted_data[NRIC] = {"NRIC": NRIC, "Name": "", "Usage": [usage]}
        else:
            formatted_data[NRIC]["Usage"].append(usage)

with open("user_features.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row[0] == "NRIC":
            continue

        NRIC, age, gender, job_industry, income = row

        if gender == "male":
            formatted_data[NRIC]["Name"] = faker.name_male()
        else:
            formatted_data[NRIC]["Name"] = faker.name_female()

        formatted_data[NRIC]["Feature"] = {
            "age": age,
            "gender": gender,
            "job_industry": job_industry,
            "income": income,
        }

with open("user_recommendations.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row[0] == "NRIC":
            continue

        (
            NRIC,
            recommended_page_1,
            predicted_time_spent_1,
            recommended_page_2,
            predicted_time_spent_2,
            recommended_page_3,
            predicted_time_spent_3,
        ) = row

        formatted_data[NRIC]["Recommendation"] = [
            recommended_page_1, recommended_page_2, recommended_page_3
        ]


# client = MongoClient(mongoDBUrl, retrywrites=False)
# db = client["cpf-neumorphic"]
# users = db["users"]
# 
# count = 0
# 
# for user in formatted_data:
#     count += 1
#     if count % 10 == 0:
#         sleep(5)
#     users.insert_one(formatted_data[user])

# Initiate DB Connection
client = MongoClient(mongoDBUrl)
db = client['neumorphic']
users = db.users
for user in formatted_data:
    pprint(formatted_data[user])
    users.insert_one(formatted_data[user])
