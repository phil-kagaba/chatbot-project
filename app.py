from model import get_response

print("Chatbot is ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = get_response(user_input)
    print("Bot:", response)
    