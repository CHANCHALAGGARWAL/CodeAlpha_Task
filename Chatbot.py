def chatbot():
    print("🤖🤖🤖🤖 Chatbot: Hello! Type something to start chatting (type 'bye' to exit).")
    
    while True:
        user = input("👤 You: ").lower()

        if user == "hello" or user == "hi":
            print("🤖🤖 Chatbot: Hi!")
        elif user == "how are you":
            print("🤖🤖 Chatbot: I'm fine, thanks!")
        elif user == "bye":
            print("🤖🤖 Chatbot: Goodbye!")
            break
        else:
            print("🤖🤖 Chatbot: Sorry, I don't understand that.")

chatbot()
