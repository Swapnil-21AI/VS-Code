# Extract the objects in the provided image and out
# put them in a list in alphabetical order

"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import google.generativeai as genai

import urllib.request 

genai.configure(api_key="AIzaSyAv33lfmK3IlW0QK60Uewq_5IlNG5okoK8")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Validate that an image is present
if not (img := urllib.request.urlretrieve("https://thumbs.dreamstime.com/b/studio-photography-computers-cameras-flashes-multiple-lens-131199349.jpg")).exists():
  raise FileNotFoundError(f"Could not find image: {img}") 

image_parts = [
  {
    "mime_type": "image/jpeg",
    "data": urllib.request.urlretrieve("https://thumbs.dreamstime.com/b/studio-photography-computers-cameras-flashes-multiple-lens-131199349.jpg").read_bytes()
  },
]

prompt_parts = [
  " Extract the objects in the provided image and out<div>put them in a list in alphabetical order</div>",
  "Image: ",
  image_parts[0],
  "List of Objects: ",
]

response = model.generate_content(prompt_parts)
print(response.text)