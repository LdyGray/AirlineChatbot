import streamlit as st
from openai import OpenAI
import os
from langchain.output_parsers import StrOutputParser

# Show title and description.
st.title("💬 Airline Chatbot")
st.write(
    "Homework Week 3 3.1 "
)
API_KEY = st.secrets["openai"]["OPENAI_API_KEY"]
### OpenAI stuff: Creative: High temperature
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  temperature = 1.8,
  max_tokens=20
)

### Display
st.write(
    "Creative: " + response.choices[0].message.content
)


### OpenAI stuff: Predictable: Low temperature
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  temperature = 0.2,
  max_tokens=20
)

### Display
st.write(
    "Predictable: " + response.choices[0].message.content
)