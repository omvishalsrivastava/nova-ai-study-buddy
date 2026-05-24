import requests
import os

apikey = os.getenv("OPENROUTER_API_KEY")
if not apikey:
    print("ERROR: API key not found. Set OPENROUTER_API_KEY in environment variables.")
    exit()
print("Nova Study Buddy (SDG 3)")
print("Type 'exit' to quit\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Nova: Take care! Bye 👋")
        break

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {apikey}"
        },
        json={
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "system",
                    "content": "You are Nova, a friendly study and mental wellness buddy for students."
                },
                {
                    "role": "user",
                    "content": user
                }
            ],
            "max_tokens": 300
        }
    )

    data = response.json()

    if "choices" in data:
        reply = data["choices"][0]["message"]["content"]
        print("Nova:", reply)
    else:
        print("Error:", data)
