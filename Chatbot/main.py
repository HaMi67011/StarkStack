from utils import load_api_key
from chatbot import SupportChatbot

def main():
    print("Welcome to the Technical Support Chatbot!")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    api_key = load_api_key()
    chatbot = SupportChatbot(api_key)

    while True:
        user = input("User : ")
        if user.lower() in ['exit', 'quit']:
            print("Ending the conversation. Goodbye!")
            break
        try:
            response = chatbot.send_message(user)
            print("Chatbot:", response)
        except Exception as e:
            print("Error:", str(e))
            break
if __name__ == "__main__":
    main()