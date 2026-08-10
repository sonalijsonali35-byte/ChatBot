while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    if "hello" in user.lower():
        print("Bot: Hi!")
    elif "how are you" in user.lower():
        print("Bot: I am fine.")
    else:
        print("Bot: I don't understand.")