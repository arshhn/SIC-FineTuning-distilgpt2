"""Streamlit demo for a fine-tuned DistilGPT-2 poetry model."""

import os

import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


st.set_page_config(page_title="AI Poem Studio", page_icon="🪶", layout="centered")
st.title("🪶 AI Poem Studio")
st.caption("A small DistilGPT-2 model fine-tuned on a starter collection of original poems.")


def configured_model_id():
    """Read a public Hugging Face model ID from Streamlit Secrets or an env var."""
    try:
        return st.secrets.get("HF_MODEL_ID", os.getenv("HF_MODEL_ID", ""))
    except Exception:
        return os.getenv("HF_MODEL_ID", "")


@st.cache_resource(show_spinner="Loading the poetry model…")
def load_model(model_id):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = tokenizer.pad_token_id
    model.eval()
    return tokenizer, model


default_model_id = configured_model_id()
model_id = st.text_input(
    "Hugging Face model repository",
    value=default_model_id,
    placeholder="your-username/poetry-distilgpt2",
    help="Upload your fine-tuned model to a public Hugging Face repository, then paste its ID here.",
)

prompt = st.text_area(
    "Poem prompt",
    value="Under the old tree,",
    height=100,
    max_chars=300,
    help="A short starting phrase gives the model a direction.",
)
col1, col2 = st.columns(2)
with col1:
    max_new_tokens = st.slider("Length", min_value=30, max_value=120, value=70, step=10)
with col2:
    temperature = st.slider("Creativity", min_value=0.5, max_value=1.2, value=0.85, step=0.05)

if st.button("Generate poem", type="primary", use_container_width=True):
    if not model_id.strip():
        st.error("Add your Hugging Face model ID above. See DEPLOYMENT.md for the upload steps.")
    elif not prompt.strip():
        st.warning("Enter a short prompt first.")
    else:
        try:
            tokenizer, model = load_model(model_id.strip())
            inputs = tokenizer(prompt.strip(), return_tensors="pt")
            with torch.inference_mode():
                output = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    do_sample=True,
                    temperature=temperature,
                    top_k=50,
                    top_p=0.92,
                    repetition_penalty=1.15,
                    no_repeat_ngram_size=3,
                    pad_token_id=tokenizer.eos_token_id,
                    eos_token_id=tokenizer.eos_token_id,
                )
            poem = tokenizer.decode(output[0], skip_special_tokens=True)
            st.subheader("Your poem")
            st.write(poem)
        except Exception as error:
            st.error(f"Could not load or run this model: {error}")

with st.expander("About this mini project"):
    st.write(
        "The project compares the pretrained model with the same model after causal-language-model "
        "fine-tuning. The training notebook saves actual validation loss, perplexity, and generated "
        "examples to a results file; no scores are hard-coded in this app."
    )
