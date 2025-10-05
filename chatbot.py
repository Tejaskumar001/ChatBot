
import json

def load_faq_data(filepath='faq_data.json'):
    with open(filepath, 'r') as file:
        return json.load(file)

def chatbot_response(user_input, faq_data):
    user_input = user_input.lower()
    for question in faq_data:
        if question in user_input:
            return faq_data[question]
    return "Sorry, I don't understand that question."

def main():
    faq_data = load_faq_data()
    print("Welcome to Sri Vasavi Engineering College FAQ Chatbot! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input, faq_data))

if __name__ == "__main__":
    main()
