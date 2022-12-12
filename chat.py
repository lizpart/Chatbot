import json
import random
from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()
stopword = set(stopwords.words("english"))

# load the chatbot's brain from a JSON file
with open("brain.json") as f:
    brain = json.load(f)



# define a function to process a user's input and return a response
def chatbot_response(message):
    # tokenize the user's input, remove stop words, and stem the remaining words
    words = [stemmer.stem(w) for w in message.split() if w not in stopword]

    # initialize the response to be empty
    response: str = ""
    chatbot = Chat(chatbot_response)

    # iterate through each category in the chatbot's brain
    for category, triggers in brain.items():
        # iterate through each trigger within the category
        for trigger, responses in triggers.items():
            # if the trigger is in the user's input, choose a random response
            # and concatenate it to the chatbot's response
            if trigger in words:
                response += random.choice(responses) + " "

    # return the chatbot's response
            return response

# pass the reflections dictionary to the Chat instance
    chatbot.set_reflections(brain)

# start the conversation
    chatbot.converse()

# test the chatbot
message = input("User: ")
response = chatbot_response(message)
print("Bot: ", response)

