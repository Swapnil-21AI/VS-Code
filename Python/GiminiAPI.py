"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyAv33lfmK3IlW0QK60Uewq_5IlNG5okoK8")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
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

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "Tech trends"
  },
  {
    "role": "model",
    "parts": "1. **Artificial Intelligence (AI) and Machine Learning (ML)**: AI and ML technologies continue to advance rapidly, enabling automation, data analysis, and decision-making across various industries.\n\n2. **5G Networks**: The deployment of 5G networks is expected to accelerate, offering faster internet speeds, lower latency, and increased connectivity.\n\n3. **Edge Computing**: Edge computing brings computation and data storage closer to the end devices, reducing latency and improving performance for real-time applications.\n\n4. **Blockchain**: Blockchain technology is gaining traction beyond cryptocurrencies, with applications in areas such as supply chain management, digital identity, and voting.\n\n5. **Internet of Things (IoT)**: IoT devices are becoming increasingly prevalent, enabling connectivity and data collection from a wide range of physical objects.\n\n6. **Cybersecurity**: With the increasing reliance on technology and data, cybersecurity measures become critical to protect against threats such as hacking, data breaches, and cyberattacks.\n\n7. **Virtual and Augmented Reality (VR/AR)**: VR and AR technologies are finding applications in gaming, education, training, and entertainment.\n\n8. **Robotics and Automation**: Robotics and automation technologies are advancing, leading to increased efficiency and productivity in manufacturing, healthcare, and other industries.\n\n9. **Cloud Computing**: Cloud computing continues to grow as businesses and organizations adopt cloud-based services for data storage, application deployment, and infrastructure management.\n\n10. **Data Analytics and Business Intelligence**: Advanced analytics and business intelligence tools enable businesses to extract insights from data, make informed decisions, and improve operational efficiency.\n\n11. **3D Printing**: 3D printing technology is becoming more accessible and affordable, allowing for rapid prototyping, customization, and small-scale manufacturing.\n\n12. **Quantum Computing**: Quantum computing research and development progress, holding the potential for significant advancements in computation speed and problem-solving capabilities.\n\n13. **Digital Twin Technology**: Digital twin technology creates virtual representations of physical assets or processes, enabling monitoring, simulation, and optimization in various domains.\n\n14. **Green Technology**: Technology solutions that promote sustainability, such as renewable energy sources, energy-efficient devices, and carbon capture and storage systems, are gaining attention.\n\n15. **Low-/No-Code Development**: Low-/no-code development platforms simplify software development, allowing non-programmers to create applications with drag-and-drop interfaces and pre-built components."
  },
  {
    "role": "user",
    "parts": "Tech trends"
  },
  {
    "role": "model",
    "parts": "1. **Generative AI**: Generative AI technologies, such as large language models (LLMs) and generative adversarial networks (GANs), are advancing rapidly, enabling the creation of realistic text, images, audio, and even code.\n\n2. **Metaverse**: The concept of the metaverse, a shared virtual world where people can interact and engage in various activities, is gaining traction and investment.\n\n3. **Web3**: Web3 refers to the next generation of the internet, characterized by decentralization, blockchain technology, and token-based economies.\n\n4. **Quantum Computing**: While still in its early stages, quantum computing is attracting significant research and investment due to its potential to revolutionize computation and problem-solving.\n\n5. **Digital Health**: Technology-driven solutions for healthcare, including telemedicine, wearable health devices, and AI-powered diagnostics, are transforming healthcare delivery and patient experiences.\n\n6. **Sustainable Tech**: Technologies that promote sustainability and combat climate change, such as renewable energy sources, energy-efficient solutions, and carbon capture technologies, are gaining importance.\n\n7. **Edge AI**: Edge AI involves running AI algorithms and models on devices or local servers, rather than relying solely on cloud-based processing, enabling faster response times and improved privacy.\n\n8. **Autonomous Systems**: Autonomous systems, including self-driving cars, drones, and robots, are becoming more sophisticated and are being deployed in various industries for tasks such as transportation, delivery, and security.\n\n9. **Vertical Farming**: Vertical farming utilizes controlled environments and technology to grow crops vertically in stacked layers, offering solutions for sustainable food production in urban areas.\n\n10. **Digital Twins**: Digital twins, virtual representations of physical assets or processes, are increasingly used for monitoring, simulation, and predictive maintenance in industries such as manufacturing, healthcare, and transportation.\n\n11. **Space Tech**: Advances in space technology, including reusable rockets, satellite constellations, and space tourism, are driving innovation and expanding our understanding of the universe.\n\n12. **Blockchain Beyond Crypto**: While cryptocurrencies have gained attention, blockchain technology is also being explored for applications in supply chain management, digital identity, voting systems, and more.\n\n13. **Synthetic Biology**: Synthetic biology involves designing and engineering biological systems to perform specific functions, with applications in medicine, agriculture, and biofuels.\n\n14. **Brain-Computer Interfaces (BCIs)**: BCIs enable communication between the brain and external devices, offering potential for applications in assistive technologies, prosthetics, and neurological research.\n\n15. **Personalized Medicine**: Advances in genomics, AI, and data analytics are leading to the development of personalized medicine approaches, tailoring treatments and therapies to individual patient characteristics."
  }
])

prompt = input("enter prompt:")
convo.send_message(prompt)
print(convo.last.text)