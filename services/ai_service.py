from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
def frage_ki(aufgabe):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "Du bist NovaAI, ein professioneller KI-Mitarbeiter für Unternehmen."
            },
            {
                "role": "user",
                "content": aufgabe
            }
        ]
    )

    return response.output_text
