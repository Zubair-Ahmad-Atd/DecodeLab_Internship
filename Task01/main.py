responses = {
    "hello": "Hi there!",
    "how are you": "I'm fine.",
    "name": "I am a chatbot build by Zubair Ahmad.",
    "stack": "Artificial Intelligence",
    "project" : "Rule Based AI Chatbot",
    "recruiter" : "Decode Labs",
    "bye": "Goodbye!"
}
print(f""" You can ask these  questions fron chatbot:
          1.    hello
          2.    how are you 
          3.    name
          4.    stack
          5.    project
          6.    recruiter
          7.    bye
          
      For quit write exit

""")
while True:
    
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    reply = responses.get(
        user_input,
        "Bot: I do not understand. please ask within the given questions bank"
    )

    print(reply)