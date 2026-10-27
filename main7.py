def chatbot():
    print("=== Welcome to the Enhanced AI Chatbot! ===")
    
    # 1. Greet the user and ask for their name
    name = input("AI: Hello there! What is your name? ").strip()
    print(f"AI: Nice to meet you, {name}!")
    
    # 2. Loop for continuous conversation
    while True:
        # Ask about mood / feelings
        mood = input(f"\nAI: How are you feeling today, {name}? (good, bad, neutral): ").strip().lower()
        
        if mood in ["good", "great", "happy", "awesome"]:
            print(f"AI: That's wonderful to hear! I'm glad you're having a good day.")
        elif mood in ["bad", "sad", "not good", "rough"]:
            print(f"AI: I'm sorry to hear that. I hope things turn around for you soon.")
        elif mood in ["neutral", "okay", "fine"]:
            print(f"AI: Got it. Sometimes an okay day is just what we need.")
        else:
            print(f"AI: Thanks for sharing! Emotions can be complex.")
            
        # 3. Follow-up questions about hobbies / interests
        hobby = input(f"\nAI: What do you like to do in your free time, {name}? ").strip()
        print(f"AI: {hobby.capitalize()} sounds like a lot of fun! That's a great interest to have.")
        
        # 4. Option to continue or exit
        choice = input(f"\nAI: Would you like to keep chatting? (yes/no): ").strip().lower()
        if choice not in ["yes", "y"]:
            # 5. Personalized farewell message
            print(f"\nAI: Goodbye, {name}! Have a wonderful rest of your day. Take care!")
            break

if __name__ == "__main__":
    chatbot()