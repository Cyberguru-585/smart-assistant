def recommend_movies(user_input):
    if "action" in user_input.lower():
        return "Try: Mad Max, John Wick, Avengers"

    elif "romance" in user_input.lower():
        return "Try: Titanic, The Notebook"

    return "Tell me a genre (action, romance, etc.)"