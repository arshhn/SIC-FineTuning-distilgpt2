# Short Project Report

## Title

**Fine-Tuning a Small Language Model for AI Poem Generation**

## Abstract

This mini project adapts the pretrained DistilGPT-2 causal language model to a small collection of short poems. A Google Colab notebook tokenizes the poems, measures a pretrained baseline, fine-tunes the model with Hugging Face Transformers, and records validation loss/perplexity and generated examples. A Streamlit web app accepts a user prompt and generates a poem with the saved fine-tuned model. The notebook writes the measured results; insert those values below after completing a run.

## Problem statement

General-purpose language models are not specifically adapted to the style and format of this project's small poetry collection. The goal is to demonstrate whether a small amount of domain-specific fine-tuning changes continuation style and held-out language-model loss, then make the result accessible through a simple web interface.

## Objectives

1. Load the pretrained `distilbert/distilgpt2` checkpoint.
2. Fine-tune it as a causal language model on the included starter poetry dataset.
3. Compare baseline and fine-tuned validation loss/perplexity on the same held-out poems.
4. Compare generations for identical prompts.
5. Provide a Streamlit interface and a reproducible free deployment path.

## Tools and dataset

- Python and Google Colab; GPU runtime is recommended when available.
- Hugging Face Transformers `Trainer` and the pretrained `distilbert/distilgpt2` checkpoint.
- A 20-poem starter dataset in `data/poems.csv`. The short sample poems are original educational text, and the dataset is intentionally small.
- Streamlit for the user interface; Hugging Face Hub stores the model weights; GitHub stores the source; Streamlit Community Cloud hosts the app.

## Method

1. Shuffle the dataset with a fixed seed and keep a small validation split aside.
2. Tokenize each poem using the checkpoint's tokenizer and use causal language-model labels (the input tokens are the next-token prediction targets, shifted internally by the model).
3. Measure the untouched pretrained checkpoint on the held-out poems.
4. Fine-tune the same model checkpoint with the training poems using the Transformers `Trainer`.
5. Measure the tuned model on the same held-out split and compute perplexity as `exp(eval_loss)`.
6. Generate samples before and after fine-tuning with identical prompts and decoding settings. Review both the numerical measure and the actual text; the notebook saves these outputs.

## Results (fill only after running the notebook)

Copy the exact values from `results/metrics.json`. Do not estimate or invent missing results.

| Measure | Pretrained baseline | Fine-tuned model |
| --- | ---: | ---: |
| Held-out evaluation loss | **[insert]** | **[insert]** |
| Held-out perplexity | **[insert]** | **[insert]** |

**Training details:** run date: [insert]; epochs: [insert]; train/validation poems: [insert]; runtime/device: [insert].

**Generation comparison:** paste at least two prompt/output pairs from `results/generation_comparison.json`. Briefly describe observed differences, such as line structure or vocabulary, without claiming that style improvement is objectively proven by only a few examples.

## Discussion and limitations

This is an educational demonstration, not a robust creative-writing system. A 20-poem corpus is too small to represent poetry broadly; train/validation loss can be noisy; the model may memorize phrases, repeat itself, or generate incoherent text. Perplexity measures next-token fit and does not measure literary quality, originality, fairness, or factuality. Generated text should be reviewed and attributed as AI-assisted. Results depend on the dataset, split, hardware, package versions, random seeds, and training settings.

## Conclusion

The project demonstrates the full pipeline from a pretrained language model through causal-language-model fine-tuning to a small hosted generation app. Complete this paragraph after running the notebook: state the observed validation-loss/perplexity change, describe what you observed in the paired generations, and mention one limitation. Avoid claiming improvement unless your measured and qualitative results support it.

## References

- Hugging Face, [DistilGPT-2 model card](https://huggingface.co/distilbert/distilgpt2).
- Hugging Face Transformers, [Causal language modeling guide](https://huggingface.co/docs/transformers/tasks/language_modeling).
- Streamlit, [Community Cloud deployment guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).
