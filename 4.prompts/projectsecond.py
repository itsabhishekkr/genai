import streamlit as st
from project_static import get_researcher_info
from langchain_core.prompts import PromptTemplate, load_prompt

st.title("Research Paper Summary Generator")
template = load_prompt("./4.prompts/template.json")

# Research Paper List
papers = [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "LLaMA: Open and Efficient Foundation Language Models",
    "ResNet: Deep Residual Learning for Image Recognition",
    "AlexNet: ImageNet Classification with Deep CNN",
    "YOLO: You Only Look Once",
    "GANs: Generative Adversarial Networks",
    "Diffusion Models Beat GANs",
    "NeRF: Neural Radiance Fields",
    "Transformer XL",
    "Vision Transformer (ViT)",
    "CLIP by OpenAI",
    "RAG: Retrieval-Augmented Generation",
    "Chain of Thought Prompting",
    "LoRA: Low-Rank Adaptation",
    "Stable Diffusion",
    "DeepSeek-R1",
    "Mixtral of Experts",
    "AlphaGo"
]

# Form
with st.form("summary_form"):

    paper_input = st.selectbox(
        "Select Research Paper",
        papers
    )

    style_input = st.selectbox(
        "Select Explanation Style",
        ["Beginner Friendly", "Technical", "Mathematical", "Code-Oriented"]
    )

    length_input = st.selectbox(
        "Select Explanation Length",
        ["Short", "Medium", "Detailed"]
    )

    submit_button = st.form_submit_button(
        label="Generate Summary"
    )

# After Submit
if submit_button:

    with st.spinner("Generating Summary..."):

        answer = get_researcher_info(template.format(
            paper_input=paper_input,
            style_input=style_input,
            length_input=length_input
        ))

        st.subheader("Summary")
        st.write(answer)