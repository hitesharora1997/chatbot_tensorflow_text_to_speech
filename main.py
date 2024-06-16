from chatbot.chatbot import ChatBot

if __name__ == "__main__":
    ai = ChatBot(name="dev")
    ex = True

    try:
        while ex:
            ai.listen()
            response = ai.respond()
            if "Tata" in response or "Have a good day" in response or "Bye" in response or "Goodbye" in response or "Hope to meet soon" in response or "peace out!" in response:
                ex = False
            ai.speak(response)
    except KeyboardInterrupt:
        print("----- Closing down Dev -----")
