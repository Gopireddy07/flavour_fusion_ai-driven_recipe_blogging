import streamlit as st
from transformers import pipeline
import random

# Initialize pipeline
# Load model directly
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="TeichAI/Qwen3-1.7B-Gemini-2.5-Flash-Lite-Preview-Distill")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)

# ----------------------------
# Joke Generator
# ----------------------------
import random

def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
        "There are 10 types of people in the world: those who understand binary and those who don’t."
    ]
    return random.choice(jokes)
# ----------------------------
# Recipe Generator
# ----------------------------
def recipe_generation(user_input, word_count):
    try:
        joke = get_joke()
        print(f"Here’s a joke while we cook up your recipe: {joke}")

        # Call Hugging Face pipeline
        response = pipe(
            f"Write a {word_count}-word recipe blog about {user_input}.",
            max_length=word_count + 100,   # allow buffer
            do_sample=True,
            temperature=0.75,
            top_p=0.95,
            top_k=64
        )

        return response[0]["generated_text"]
    except Exception as e:
        return f"Error generating recipe: {str(e)}"
# ----------------------------
# Streamlit UI
# ----------------------------
st.title("Flavour Fusion: AI-Driven Recipe Blogging")

topic = st.text_input("Enter recipe topic:")
word_count = st.number_input("Enter desired word count:", min_value=100, max_value=3000)

if st.button("Generate Recipe Blog"):
    st.info("Generating your recipe blog... Please wait.")
    blog = recipe_generation(topic, word_count)
    st.subheader("Generated Recipe Blog")
    st.write(blog)
    st.download_button("Download Blog", blog, file_name="recipe_blog.txt")