# Nova AI Study Buddy (`nova-ai-study-buddy`)

## Overview
**Nova Study Buddy** is a simple command-line chat client that helps you study by conversing with an AI model through the **OpenRouter API**. The app runs in an interactive terminal session and sends each of your messages to OpenRouter, then prints Nova’s response.

The entry point is `main.py`, which:
- Reads your `OPENROUTER_API_KEY` from environment variables
- Starts an interactive loop for user input
- Sends messages to `https://openrouter.ai/api/v1/chat/completions` using the **`gpt-4o`** model
- Uses a fixed **system prompt** to define Nova’s role
- Displays the AI reply (or the API error payload if a valid response is not returned)

## Key Features
- **Interactive CLI chat loop**: type messages continuously until you enter `exit`
- **Environment-based configuration**: requires `OPENROUTER_API_KEY`
- **OpenRouter-backed responses**: sends chat requests to the OpenRouter `chat/completions` endpoint
- **Fixed Nova persona/system prompt**: ensures consistent study-buddy behavior
- **Basic error handling**: prints the API error payload when the expected response shape is missing

## Tech Stack
- **Python** (command-line application)
- **Requests**: HTTP client library pinned to **`requests==2.32.3`**
- **OpenRouter API**: `https://openrouter.ai/api/v1/chat/completions`
- **Model used**: `gpt-4o`

## Project Architecture
This repository is intentionally minimal and centers around a single runtime script:

### `main.py` — Command-line client
**Responsibilities:**
1. **Configuration loading**
   - Loads `OPENROUTER_API_KEY` from environment variables
   - Exits with an error if the key is missing

2. **Interactive loop**
   - Prompts for user input repeatedly
   - Terminates when the user types `exit`

3. **API request**
   - Sends each message to the OpenRouter chat completions endpoint:
     - `https://openrouter.ai/api/v1/chat/completions`
   - Uses:
     - **Model**: `gpt-4o`
     - **System prompt**: a fixed prompt defining Nova’s role
     - **User message**: the latest input from the terminal

4. **Response handling**
   - Prints Nova’s reply when a `choices` field is present in the API response
   - Otherwise, prints the API error payload (or raw error details)

### `requirements.txt` — Dependencies
- Declares a single primary dependency:
  - `requests==2.32.3`

## Installation (Placeholder)
> Install prerequisites and dependencies (exact steps may vary by environment).

1. Ensure you have Python installed (version not specified in this repository summary).
2. Install dependencies:
   bash
   pip install -r requirements.txt
   

## Usage (Placeholder)
1. Set your OpenRouter API key as an environment variable:
   bash
   export OPENROUTER_API_KEY="your_api_key_here"
   
2. Run the application:
   bash
   python main.py
   
3. Start chatting in the terminal.
   - Type `exit` to end the session.

--- 
If you want, I can also provide a small “developer quickstart” checklist (env vars, request/response expectations, and common failure modes) based on the current behavior described in `main.py`.

---
*This README was generated with [PresentMe](https://www.presentmeapp.xyz/). View the full presentation [here](https://www.presentmeapp.xyzhttp://localhost:5000/p/220c528a-1ccd-479c-a2fb-c5f1757ad7c1).*
