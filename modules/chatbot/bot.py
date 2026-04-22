def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hello! How can I help you?"

    elif "bye" in user_input:
        return "Goodbye!"

    return "I didn't understand that."