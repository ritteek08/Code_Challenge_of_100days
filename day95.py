#Simple Text Editor Program in Python
def text_editor():  
    print("Welcome to the Simple Text Editor!")
    print("Type 'exit' to quit the editor.")
    
    text = ""
    
    while True:
        user_input = input("Enter text (or 'exit' to finish): ")
        
        if user_input.lower() == "exit":
            print("Exiting the text editor. Here's your final text:")
            print(text)
            break
        else:
            text += user_input + "\n"
if __name__ == "__main__":
    text_editor()