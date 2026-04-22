
from modules.chatbot.bot import get_bot_response
from modules.recommender.movies import recommend_movies
from modules.chatbot.intent_model import predict_intent


last_intent = None 

def route(user_input):
    global last_intent

    intent, confidence = predict_intent(user_input)

    if user_input.lower() in ["action", "romance", "comedy"]:
        return recommend_movies(user_input)

    if confidence < 0.5:
        return "I'm not sure what you mean. Can you rephrase?"

    if intent == "greeting":
        last_intent = "greeting"
        return get_bot_response(user_input)

    elif intent == "movie_recommend":
        last_intent = "movie_recommend"
        return "Tell me a genre (action, romance, etc.)"

    return "Sorry, I don't support that yet."