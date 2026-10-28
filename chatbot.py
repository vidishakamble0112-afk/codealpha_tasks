def get_reply(message):
    message = message.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm a simple Python chatbot."
    elif message == "help":
        return "Try: hello, how are you, what is your name, bye"
    elif message in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def main():
    print("=== BASIC CHATBOT ===")
    print("Type 'help' to see what I understand. Type 'bye' to exit.\n")

    while True:
        user = input("You: ")
        reply = get_reply(user)
        print("Bot:", reply)
        if user.lower().strip() in ("bye", "goodbye", "exit"):
            break


if __name__ == "__main__":
    main()
