from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature = 0
)

st.header('Research Helper')

paper_options = [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis",
    "Other (Custom)"
]

paper_input = st.selectbox("Select Research Paper Name",paper_options)

if paper_input == "Other (Custom)":
    paper_input = st.text_input(
        "Enter Research Paper Name"
    )

style_options = [
    "Beginner-Friendly",
    "Technical",
    "Code-Oriented",
    "Mathematical",
    "Other (Custom)"
]

style_input = st.selectbox(
    "Select Explanation Style",
    style_options
)

if style_input == "Other (Custom)":
    style_input = st.text_input(
        "Enter Custom Style"
    )


length_options = [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)",
    "Other (Custom)"
]

length_input = st.selectbox(
    "Select Explanation Length",
    length_options
)

if length_input == "Other (Custom)":
    length_input = st.text_input(
        "Enter Custom Length Requirement"
    )

    
template = load_prompt(r"C:\Users\Harishwar reddy\Desktop\LangChain\LANGCHAIN PROMPTS\template.json")
if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input' : paper_input,
        'style_input' : style_input,
        'length_input' : length_input
    })
    st.write(result.content)