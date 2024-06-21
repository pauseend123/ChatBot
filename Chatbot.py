import openai
import json
from dotenv import load_dotenv

# Load environment variables (including your OpenAI API key)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Chat history for context
conversation_history = []

def get_chatbot_response(user_message):
    """Gets a response from the chatbot based on user input and conversation history."""
    global conversation_history

    conversation_history.append({"role": "user", "content": user_message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or gpt-4 if available
        messages=conversation_history,
        temperature=0.7,  # Adjust for creativity (0.0 - 1.0)
    )
    
    # Update conversation history
    conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})
    
    return response.choices[0].message.content


def main():
    """Main loop for interactive chat with the user."""

    print("IT Help Desk Chatbot (type 'exit' to quit)")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        response = get_chatbot_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()
