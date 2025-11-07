from google import genai
from google.genai import types
import base64
import os

def generate():
  client = genai.Client(
    vertexai="true",
    project="grant-moyle-gde",
    location="us-central1"
  )

  model = "gemini-2.5-flash"
  contents = [
    types.Content(
      role="user",
      parts=[        
        types.Part.from_text(text="""give me a random fact about OSU""")
      ]
    )
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 0.5,
    top_p = 0.95,
    max_output_tokens = 65535,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    system_instruction=[types.Part.from_text(text="""This is the Oregon State University Chat Bot - please answer questions about the university""")],
    thinking_config=types.ThinkingConfig(
      thinking_budget=-1,
    ),
  )

  returnString=""
  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    returnString=returnString + chunk.text
  return returnString

print(generate())