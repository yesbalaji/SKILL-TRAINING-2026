template="""You are a patient Python tutor.
Explain {topic} for a beginner.
Give one example in at most {limit} words. """
prompt= template.format(topic="for loops",limit=80)
print(prompt)    