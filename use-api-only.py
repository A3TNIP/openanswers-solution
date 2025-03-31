import requests

question_json = requests.get("https://www.openanswers.co.uk/api/v1/join-us").json()
# Remove the '=' sign and strip whitespace
question = question_json['question'].replace("=", "").strip()
answer = eval(question)
payload = {
    "answer": answer,
    "key": question_json['key']
}
response = requests.post("https://www.openanswers.co.uk/api/v1/join-us", json=payload)
# Print the response
print(response.json())
