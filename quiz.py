import json
quiz=(
    "Question:" "What does len() return?",
    "Answer:""The number of items"
)
text=json.dumps(quiz)
print(text)
parsed= json.loads(text)
print(["Answer"])
