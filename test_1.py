import new.test_1 as test_1

# Set your OpenAI API key
test_1.api_key = 'your-api-key-here'

def generate_response(prompt):
    response = test_1.Completion.create(
        engine="text-davinci-003",  # You can use different engines
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Define prompts to test
prompts = [
    "Write a short story about a dragon and a knight.",
    "Explain the theory of relativity in simple terms.",
    "List 5 tips for improving productivity."
]

# Generate and print responses
for prompt in prompts:
    print(f"Prompt: {prompt}")
    print(f"Response: {generate_response(prompt)}")
    print("="*40)
