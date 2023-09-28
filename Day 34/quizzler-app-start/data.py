import requests

params = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean"
}

link = "https://opentdb.com/api.php?"
question_data = {}

response = requests.get(link, params=params)

if response.ok:
    data = response.json()["results"]
    for question in data:
        question_data["question"] = question["question"]
        question_data["correct_answer"] = question["correct_answer"]

print(question_data)
