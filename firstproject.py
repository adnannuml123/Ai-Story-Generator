import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# API key
api_key = os.getenv("AIzaSyClT9PFhCGwYnFL80X9sshg0lTuz0e1ThM")

# Gemini client
client = genai.Client(api_key=api_key)

# UI
st.set_page_config(page_title="AI Story Generator", page_icon="📖")
st.title(" AI Story Generator for Kids")
st.write("Simple AI app jo bachon ke liye kahani banata hai ")

topic = st.text_input("Story ka topic likho:")
length = st.selectbox("Story length select karo:", ["Short", "Medium"])

if st.button("Generate Story"):
    if topic == "":
        st.warning("Please topic likho!")
    else:
        with st.spinner("Story ban rahi hai..."):
            try:
                prompt = f"Write a {length.lower()} and simple story for a 5 year old kid about {topic}."

                response = client.models.generate_content(
                    model="models/gemini-2.5-flash",
                    contents=prompt
                )

                st.success("Story ready ✅")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {e}")
