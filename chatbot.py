def chatbot():
    print("Welcome to ChatBot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()
# This code implements a simple chatbot that responds to user inputs.
# It recognizes greetings and a farewell, and provides default responses for unrecognized inputs.
# The chatbot runs in a loop until the user types 'bye'.
# The chatbot is case-insensitive and can be easily extended with more responses.
# The chatbot can be tested by running the script and interacting with it in the console.
# The chatbot is designed to be simple and user-friendly, making it easy to interact with.
# The chatbot can be further enhanced by adding more responses and functionalities.
# The chatbot can be used for basic conversational interactions and can serve as a foundation for more complex