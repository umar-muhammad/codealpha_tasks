import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using patterns & responses
chatbot_pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]],
    [r"how are you?", ["I'm a bot, but I'm doing great!", "I'm fine! How about you?"]],
    [r"what is your name?", ["I'm a chatbot!", "I don't have a name, but you can call me ChatBot."]],
    [r"who made you?", ["I was created by Umar!", "A human programmer built me."]],
    [r"what can you do?", ["I can chat with you! Try asking me simple questions."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Talk to you later!"]],
    [r"(.*)", ["I'm not sure how to respond to that.", "Could you rephrase that?", "That's interesting!"]]
]

# Create chatbot instance
chatbot = Chat(chatbot_pairs, reflections)

# Start chat function
def start_chat():
    print("=" * 40)
    print("🤖 Welcome to the Simple ChatBot!")
    print("📌 Type simple messages like:")
    print("   - 'hi', 'hello', 'hey'")
    print("   - 'how are you?'")
    print("   - 'what is your name?'")
    print("   - 'who made you?'")
    print("   - 'bye' to exit the chat")
    print("=" * 40)
    
    while True:
        user_input = input("\nYou: ").lower()
        if user_input == "bye":
            print("🤖 ChatBot: Goodbye! Have a great day! 👋")
            break
        response = chatbot.respond(user_input)
        print(f"🤖 ChatBot: {response}")

# Run chatbot
if __name__ == "__main__":
    start_chat()
