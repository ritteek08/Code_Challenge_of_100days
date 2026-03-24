# Simple Chatbot Program in Python
def chatbot():
    print("Hello! I'm a simple chatbot. What's your name?")
    name = input("You: ")
    print(f"Chatbot: Nice to meet you, {name}!")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif "what's your name" in user_input.lower() or "who are you" in user_input.lower():
            print("Chatbot: I'm a simple chatbot created to chat with you!")
        else:
            print(f"Chatbot: You said '{user_input}'. That's interesting!")

if __name__ == "__main__":
    chatbot()