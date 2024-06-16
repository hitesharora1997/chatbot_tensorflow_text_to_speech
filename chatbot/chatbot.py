from chatbot.speech import speech_to_text
from chatbot.text_to_speech import text_to_speech
from chatbot.utilities import wake_up, action_time
import transformers
import os
import numpy as np

class ChatBot:
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name
        self.text = ""
        self.tokenizer = transformers.AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side='left')
        self.nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium", tokenizer=self.tokenizer)
        os.environ["TOKENIZERS_PARALLELISM"] = "true"

    def listen(self):
        self.text = speech_to_text()

    def respond(self):
        if wake_up(self.text, self.name):
            return "Hello I am Dave the AI, what can I do for you?"
        elif "time" in self.text:
            return action_time()
        elif any(i in self.text for i in ["thank", "thanks"]):
            return np.random.choice(["you're welcome!", "anytime!", "no problem!", "cool!", "I'm here if you need me!", "mention not"])
        elif any(i in self.text for i in ["exit", "close"]):
            return np.random.choice(["Tata", "Have a good day", "Bye", "Goodbye", "Hope to meet soon", "peace out!"])
        else:
            if self.text == "ERROR":
                return "Sorry, come again?"
            else:
                conversation = transformers.Conversation(self.text)
                chat = self.nlp(conversation)
                res = chat.generated_responses[0]
                return res

    def speak(self, response):
        text_to_speech(response)
