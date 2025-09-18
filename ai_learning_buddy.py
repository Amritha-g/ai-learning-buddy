
#openai.api_key = "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"  




import openai
import streamlit as st

from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to explain concept like a 5-year-old
def explain_like_im5(concept):
    prompt = f"Explain '{concept}' like I'm 5 years old in simple words."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",   # Use GPT-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful teacher who explains concepts simply."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

#  Function to generate simple quiz
def generate_quiz(concept):
    prompt = f"Create 3 very simple multiple-choice questions for a 5-year-old about '{concept}'. Each question should have 4 options and mark the correct one clearly."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a teacher who makes fun quizzes for kids."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()
