from api import OPENAI_API_KEY
from openai import OpenAI

# Passando a chave ao inicializar o cliente
client = OpenAI(api_key=OPENAI_API_KEY)

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "cute girl"},
        {
            "role": "user",
            "content": "talk in a cute and charismatic way."
        }
    ]
)

print(completion.choices[0].message)
