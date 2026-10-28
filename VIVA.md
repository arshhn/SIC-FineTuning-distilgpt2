# Viva Questions and Answers

### 1. What is fine-tuning?

Fine-tuning continues training an already pretrained model on a smaller, task-related dataset so its behavior adapts to that data.

### 2. What does GPT-2 learn during causal language modeling?

It learns to predict the next token from the tokens that came before it. At generation time, it repeatedly samples or selects a next token and appends it to the prompt.

### 3. Why use DistilGPT-2?

It is a smaller distilled GPT-2 checkpoint, so it is easier to demonstrate and deploy than a larger language model while retaining the same basic autoregressive generation approach.

### 4. What is a tokenizer?

A tokenizer converts text into token IDs the model can process, and converts generated token IDs back into text. Tokens may be word pieces rather than whole words.

### 5. What is the purpose of a validation split?

It holds back examples from training so we can estimate how well the model predicts poems it did not train on. It is not a guarantee of real-world quality, especially with a tiny dataset.

### 6. What does perplexity mean?

Perplexity is `exp(loss)` for the language-model cross-entropy loss. Lower values mean the model assigned higher probability to the observed held-out token sequence, but do not necessarily mean better poems.

### 7. Why compare before and after using the same prompts?

Holding prompts and generation settings constant makes the sample comparison more informative because the model checkpoint is the main changing factor.

### 8. What does temperature control?

Temperature adjusts how sharply token probabilities are sampled. Lower values tend to be more predictable; higher values tend to add variation and risk less coherent output.

### 9. What is overfitting, and why is it a risk here?

Overfitting occurs when the model adapts too closely to training examples and performs worse on unseen examples. A tiny poetry dataset makes this especially likely.

### 10. Why does the app need the Hugging Face model ID?

The lightweight app code is stored on GitHub, while the larger trained weights are stored in the Hugging Face model repository. The ID tells Transformers where to download the model and tokenizer.

### 11. What is the role of Streamlit?

Streamlit turns a Python script into an interactive web app. Here it collects a prompt and settings, loads the model, runs generation, and displays the result.

### 12. What are the main limitations of the project?

The dataset and evaluation set are very small; perplexity is not a measure of literary quality; output may repeat or be incoherent; and the model can memorize training phrases. The measured run and examples should be reported honestly.
