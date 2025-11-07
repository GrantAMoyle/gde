# Generate me an image based on the prompt provided by the parameter image
# use Google Gemini to create the image
from google import genai
from google.genai import types
import base64
import os

def generate_image(prompt):
  client = genai.Client(
    vertexai="true",
    project="grant-moyle-gde",
    location="us-central1"
  )

  model = "image-generation@006" # Use the appropriate image generation model

  response = client.models.generate_content(
    model=model,
    contents=[
      types.Content(
        role="user",
        parts=[
          types.Part.from_text(text=prompt)
        ]
      )
    ]
  )
  
  # Assuming the response contains an image in base64 format
  # You might need to adjust this based on the actual API response structure
  if response.candidates and response.candidates[0].content.parts:
      for part in response.candidates[0].content.parts:
          if part.image:
              # The image data is likely in part.image.data or similar
              # For demonstration, let's assume it's a base64 encoded string
              return part.image.data
  return None

if __name__ == "__main__":
  # Example usage:
  image_prompt = "A futuristic city at sunset"
  generated_image_data = generate_image(image_prompt)
  if generated_image_data:
    # You can save the image or display it
    with open("generated_image.png", "wb") as f:
      f.write(base64.b64decode(generated_image_data))
    print("Image generated and saved as generated_image.png")
  else:
    print("Failed to generate image.")
    