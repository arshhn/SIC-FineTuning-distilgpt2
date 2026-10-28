# Fine-Tuning a Small Language Model for AI Poem Generation

Beginner-friendly college mini project using Python in Google Colab, Hugging Face Transformers, `distilgpt2`, an original 20-poem starter dataset, and Streamlit.

## Project files

- `poetry_finetuning_colab.ipynb` — step-by-step Colab notebook. It actually fine-tunes DistilGPT-2 and writes measured results; it does not contain made-up scores.
- `data/poems.csv` — small starter dataset of original short poems.
- `app.py` — Streamlit poem-generation interface.
- `requirements.txt` — app dependencies for Streamlit Community Cloud.
- `REPORT.md` — short report template with a results table to fill from the notebook.
- `VIVA.md` — viva questions and answers.
- `DEPLOYMENT.md` — model upload, GitHub, and free Community Cloud steps.

## Fast start

1. Open `poetry_finetuning_colab.ipynb` in Google Colab and select a GPU runtime if available.
2. Run the notebook from top to bottom. It fine-tunes `distilbert/distilgpt2`, compares the pretrained and fine-tuned checkpoints, saves a model folder, and writes `results/metrics.json` plus generated examples.
3. Upload the fine-tuned model folder to a public Hugging Face model repository (instructions in `DEPLOYMENT.md`).
4. Push this project folder to a GitHub repository and deploy `app.py` from Streamlit Community Cloud.
5. In the app, paste your Hugging Face model ID, for example `yourname/poetry-distilgpt2`.

## Important result policy

The dataset is intentionally tiny for a 2–4 week class project. The notebook produces the actual validation loss/perplexity and before/after generations when you run it. Small-corpus fine-tuning can overfit and does not guarantee that every generated poem is coherent or original. Fill the report's results section from your own run.

## Suggested 2–4 week plan

| Week | Work |
| --- | --- |
| 1 | Read about causal language modeling, inspect the dataset, and run the pretrained baseline. |
| 2 | Fine-tune in Colab, save the checkpoint, and compare held-out loss and sample generations. |
| 3 | Upload the model, run the Streamlit app locally, and deploy it from GitHub. |
| 4 | Improve the report, document limitations, and prepare the viva demonstration. |

## Model and data notes

The base model is the public `distilbert/distilgpt2` checkpoint. The CSV poems are short original educational examples included for this project. This tiny dataset is a demonstration corpus, not a representative poetry collection or a benchmark.
