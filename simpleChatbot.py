import nltk
from nltk.chat.util import Chat, reflections

pairs = [
  [
    r"my name is (.*)", 
    ["Hello %1, How can I help you today?"]
  ],
  [
    r"what is your name?",
    ["I am a chatbot. You can call me a bot."]
  ],
  [
    r"how are you?",
    ["I am doing good. How about  you?"]
  ],
  [
    r"sorry (.*)", 
    ["Its alright"]
  ],
  [
    r"what is the weather in (.*)?",
    ["Weather in %1 is sunny"]
  ],
  [
    r"what is the time?",
    r"the time is %s" % time.strftime("%H:%M:%S")],
[
  r"(.*)",
  ["I don't understand"]
]
]

def chatbot():
  print("Hi! I'm a chatbot. Let's talk!")
  chat = Chat(pairs, reflections)
  chat.converse()

if __name__ == "__main__":
  chatbot()

