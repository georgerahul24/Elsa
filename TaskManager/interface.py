import ollama
from task import *

context = """
You are talking with a user and then simplifying the query to python program
You can output only three responses
'time' if the user wants to know about the current time.
'web','<keyword>' if the user wants to search something in the internet
'youtube','<keyword>' if the user wants to search some videos or series
'others',<the response> for the some other responses that does not fit the above categories
Use the appropriate one
Give bare minimum response since a python program has to parse it using regex
Make sure to follow to the current output syntax"""

response = ollama.generate(model='llama3', prompt=context + 'I want to watch some videos about cat')['response']
print(response)

response = ollama.generate(model='llama3', prompt=context + 'Where is Taj Mahal located?')['response']
print(response)

response = ollama.generate(model='llama3', prompt=context + 'What is the time now?')['response']
print(response)

response = ollama.generate(model='llama3', prompt=context + 'Why is the sky blue?')['response']
print(response)

response = ollama.generate(model='llama3', prompt=context + 'What is latest election results?')['response']
print(response)
