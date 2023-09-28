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
    data = response.json()["results"][0]
    question_data[data["question"]] = data["correct_answer"]

print(question_data)
