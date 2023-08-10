# AI Assistant - ChatGPT-3.5-Turbo
import openai
print("\nAI Assistant - ChatGPT-3.5-Turbo")
# Set your OpenAI API key here
api_key = ""

# Initialize the OpenAI API client
openai.api_key = api_key

def get_chat_response(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        response = get_chat_response(user_input)
        
        # Print header and response with separator line
        print("ChatGPT-3.5-Turbo:", response)
        print("_" * 100)  # Creating a line separator

if __name__ == "__main__":
    main()
