"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

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
if not (img := Path("image0.jpeg")).exists():
  raise FileNotFoundError(f"Could not find image: {img}")

image_parts = [
  {
    "mime_type": "image/jpeg",
    "data": Path("image0.jpeg").read_bytes()
  },
  {
    "mime_type": "image/jpeg",
    "data": Path("image1.jpeg").read_bytes()
  },
  {
    "mime_type": "image/jpeg",
    "data": Path("image2.jpeg").read_bytes()
  },
]

prompt_parts = [
  " What object is this? Describe how it might be used",
  "Object: ",
  image_parts[0],
  "Description: This is a pipe organ. It is a large musical instrument that is used in churches, concert halls, and other large buildings. It is made up of a series of pipes that are arranged in different sizes and shapes. The pipes are played by pressing keys on a keyboard. When a key is pressed, air is forced through the pipe, which produces a sound. The sound of a pipe organ is very powerful and can be used to create a wide variety of music.",
  "Object: ",
  image_parts[1],
  "Description: This is a sundial. It is a device that uses the sun's position in the sky to tell the time. The sundial has a flat surface with a hole in the center. A metal rod is placed through the hole and is pointed at the North Star. The shadow of the rod falls on the flat surface and indicates the time.",
  "Object: ",
  image_parts[2],
  "Description: ",
]

response = model.generate_content(prompt_parts)
print(response.text)