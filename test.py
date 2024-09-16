import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'  # Replace with your actual API key

# Define the chat messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Provide a brief summary of the French Revolution, focusing on the key causes, major events, and significant outcomes."}
]

# Request completion from the chat model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use "gpt-4" if available
    messages=messages,
    max_tokens=150,  # Adjust as needed
    temperature=0.7  # Adjust creativity
)

# Print the model's response
print(response.choices[0].message['content'].strip())
