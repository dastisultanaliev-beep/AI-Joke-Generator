
import customtkinter as ctk
from openai import OpenAI

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://bothub.chat/api/v2/openai/v1"
MODEL = "gemini-3.1-flash-lite"

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

app = ctk.CTk()
app.title("AI Joke Generator")
app.geometry("600x500")


def generate_joke():
    topic = n.get().strip()

    if not topic:
        d.configure(text="First, enter a topic for the joke!")
        return

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Your task is to generate a very funny joke about the topic suggested by the user. Make it extremely hilarious!"
                },
                {
                    "role": "user",
                    "content": f"Generate a very funny joke about: {topic}"
                }
            ]
        )

        answer = response.choices[0].message.content

    except Exception as err:
        answer = f"Error: {err}"

    d.configure(text=answer)


n = ctk.CTkEntry(
    app,
    placeholder_text="Enter a topic for the joke",
    font=("Arial", 14),
    width=300
)
n.pack(padx=10, pady=10)

s = ctk.CTkButton(
    app,
    text="Generate Joke",
    font=("Arial", 14),
    command=generate_joke
)
s.pack(padx=10, pady=20)

d = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 14),
    wraplength=520
)
d.pack(padx=10, pady=30)

app.mainloop()
