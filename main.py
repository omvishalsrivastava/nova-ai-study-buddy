import requests
import os

# Get API key from system environment variables
apikey = os.getenv("OPENROUTER_API_KEY")

# Stop program if API key is missing
if not apikey:
    print("ERROR: API key not found. Please add your OPENROUTER API key.")
    exit()

# Project title
print("Nova Study Buddy (SDG 3)")
print("Type 'exit' to quit\n")

# Main chat loop
while True:

    # Get user input
    user = input("You: ")

    # Exit condition
    if user.lower() == "exit":
        print("Nova: Take care! Bye 👋")
        break

    # Send request to OpenRouter AI API
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {apikey}"
        },
        json={
            "model": "gpt-4o",  # AI model used
            "messages": [
                {
                    "role": "system",
                    "content": "You are Nova, a friendly study and mental wellness assistant for students."
                },
                {
                    "role": "user",
                    "content": user
                }
            ],
            "max_tokens": 300  # limits response length
        }
    )

    # Convert API response to JSON format
    data = response.json()

    # Check if response is valid
    if "choices" in data:
        reply = data["choices"][0]["message"]["content"]
        print("Nova:", reply)
    else:
        print("Error:", data)
