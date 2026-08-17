import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Say hello and confirm you're working."}
    ]
)

print(response["message"]["content"])
