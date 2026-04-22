from core.router import route

print("🤖 Smart Assistant Running... (type 'quit' to exit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Bot: Goodbye 👋")
        break

    response = route(user_input)
    print("Bot:", response)