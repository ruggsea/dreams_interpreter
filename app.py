# Importing necessary libraries
import streamlit as st
import openai
import os

# Setting up OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Creating a function to interpret dreams using OpenAI API
def interpret_dream(dream):
    # Set prompt and parameters
    prompt = "Interpret this dream: " + dream + "\n\nInterpretation:"
    params = {
        "model": "text-davinci-002",
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 200,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    # Send request to OpenAI API and get response
    response = openai.Completion.create(**params)
    # Extract interpretation from response
    interpretation = response.choices[0].text.strip()
    return interpretation

# Creating Streamlit app
def main():
    st.title("Dream Interpretation App")
    st.write("Warning: Dream interpretation is a subjective practice and should not be taken as a definitive explanation of your dream.")
    dream = st.text_input("Describe your dream:")
    
    if st.button("Interpret"):
        interpretation = interpret_dream(dream)
        st.write("Interpretation:", interpretation)

if __name__ == '__main__':
    main()
