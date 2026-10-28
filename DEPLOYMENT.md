# Training, saving, and deployment guide

## A. Fine-tune the model in Google Colab

1. Upload `poetry_finetuning_colab.ipynb` to Google Drive and open it with Google Colab, or upload the notebook directly at [colab.research.google.com](https://colab.research.google.com/).
2. In **Runtime → Change runtime type**, choose a GPU if one is available. The notebook also works on CPU but can take longer.
3. Upload `data/poems.csv` when the notebook asks for it, or put the CSV in your Drive and set its path in the notebook.
4. Run every cell in order. The notebook first measures the base checkpoint, then runs `Trainer.train()`, evaluates the tuned checkpoint, and creates before/after samples using the same prompts.
5. The notebook saves the fine-tuned model and tokenizer in `poetry-distilgpt2-finetuned/`. It also saves measured metrics and generations under `results/`.
6. Download the model folder as a ZIP from Colab's Files panel, or use the optional Hugging Face Hub upload cell. The notebook does not silently upload anything.

## B. Upload the model to Hugging Face Hub

The model weights are too large to commit as normal files to a small GitHub app repository. Use a public Hugging Face model repository for the weights; GitHub holds the lightweight app and project files.

1. Create/sign in to a Hugging Face account and create a **new model** repository, for example `yourname/poetry-distilgpt2`.
2. In Colab, run the optional login cell and create a Hugging Face access token with write permission. Use Colab's secret manager for the token if available; do not paste a token into a notebook you plan to publish.
3. Set `MODEL_REPO_ID` in the notebook to your repository ID and run the optional `push_to_hub()` cell. Alternatively, upload the saved model folder using the Hugging Face website or CLI.
4. Check that the repository contains `config.json`, tokenizer files, and model weight files such as `model.safetensors`.
5. Copy the repository ID, e.g. `yourname/poetry-distilgpt2`.

The model repository should be public for the simplest free app setup. If you make it private, you must also configure a Hugging Face read token in Streamlit Community Cloud Secrets and add token handling to the app.

## C. Upload the project to GitHub

1. Create a new GitHub repository, e.g. `fine-tuning-poetry-mini-project`.
2. Upload the contents of this folder so that `app.py` and `requirements.txt` are in the repository root. Include the notebook, `data/poems.csv`, report, and viva file.
3. Do **not** upload a Hugging Face token, `.env`, `.streamlit/secrets.toml`, large training checkpoints, or Colab cache files. `.gitignore` covers common local secrets and checkpoints.
4. Make the repository public if you want public source code and the simplest Community Cloud deployment. Commit and push the files.

You can use GitHub's **Add file → Upload files** interface, or these commands from this project folder:

```bash
git init
git add app.py requirements.txt README.md DEPLOYMENT.md REPORT.md VIVA.md data poetry_finetuning_colab.ipynb .streamlit .gitignore
git commit -m "Add poetry fine-tuning mini project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/fine-tuning-poetry-mini-project.git
git push -u origin main
```

## D. Deploy on Streamlit Community Cloud

1. Sign in at [share.streamlit.io](https://share.streamlit.io/) and connect GitHub.
2. Select **Create app**, choose your repository and `main` branch, and set the app file path to `app.py`.
3. Deploy. Community Cloud installs dependencies from the root `requirements.txt`; the first build may take several minutes because PyTorch and Transformers are sizable.
4. Open the app once it is running. Paste your public Hugging Face model ID in the model field. Optionally set it once in the app's **Settings → Secrets** using:

   ```toml
   HF_MODEL_ID = "YOUR_USERNAME/poetry-distilgpt2"
   ```

   This is an identifier, not a secret. Don't add a Hugging Face token for a public model.

5. Generate a poem, then copy the app's `https://...streamlit.app` URL and share it with faculty.
6. To update the app, commit changes to GitHub; Community Cloud redeploys from the repository.

If the app fails to build, inspect its Community Cloud logs and check that the repository root contains `app.py` and `requirements.txt`. Confirm that the model ID is correct and the Hugging Face model repository is public.

## E. Run the app locally (optional)

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
$env:HF_MODEL_ID="YOUR_USERNAME/poetry-distilgpt2"  # PowerShell
# export HF_MODEL_ID="YOUR_USERNAME/poetry-distilgpt2"  # macOS/Linux
streamlit run app.py
```

Current deployment details are based on the official [Community Cloud deployment guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy) and [dependency guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies). Community Cloud is currently free and connects to GitHub, but service policies and resource limits can change.
