import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import streamlit as st

# Load environment variable
load_dotenv()
HF_KEY = os.getenv("HF_API_KEY")
client = InferenceClient(api_key=HF_KEY)

def get_ai_response(prompt):
    try:
        response = client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",    # Or use meta-llama/Meta-Llama-3-8B-Instruct for high quality
            max_tokens=200,
            temperature=0.7
        )
        # Extract answer from the response object
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {e}"

st.set_page_config(page_title="AI Learning Buddy", page_icon="🤖")
st.title("🤖 AI Learning Buddy 📚")
st.write("Ask me anything about Data Structures, Algorithms, AI, or ML!")
user_input = st.text_area("💬 Enter your question here:")

if st.button("Get Answer"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            answer = get_ai_response(user_input)
        st.success("Here’s what I found:")
        st.write(answer)
    else:
        st.warning("Please type a question before clicking!")
