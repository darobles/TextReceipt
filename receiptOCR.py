import openai
from openai import OpenAI
import asyncio
from PIL import Image
import io
import base64
import requests
api_key = "sk-proj-KEY"


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "bill.jpeg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Extrae la información de los productos consumidos,la cantidad y el costo unitario de estos. Ademas incluye la propina, los descuentos y total de la siguiente boleta. Agrupa los items iguales."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 1000
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(response.json())
#purpose=''  # Esta es una representación genérica, ajusta según el modelo específico y uso
