# ==========================================
#           BASIC CHATBOT
# ==========================================

# Function for chatbot response
def chatbot_response(user_input):

    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hi! Nice to meet you."

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "My name is Python Chatbot."

    elif user_input == "what can you do":
        return "I can answer some basic questions."

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


# ==========================================
#           START CHATBOT
# ==========================================

print("=" * 45)
print("             BASIC CHATBOT")
print("=" * 45)

print("Hello! I am a simple chatbot.")
print("Type 'bye' to exit the chatbot.")
print()

# Chat loop
while True:

    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    # Stop chatbot when user says bye
    if user_input.lower() == "bye":
        break

print()
print("Chatbot session ended.")