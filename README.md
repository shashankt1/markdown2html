# 📝 Markdown2HTML — Streamlit App with ML-Powered Enhancements

This is an advanced **Markdown to HTML** converter with built-in **machine learning capabilities** for:

- **Heading classification** (e.g., Heading1, Heading2, Paragraph)
- **Style classification** (Formal, Informal, Instructional, Neutral)
- **Auto-summarization** using NLP
- Live **Streamlit** web interface
- Command-line utility support

---

## 🚀 Features

- 🧠 **ML Model Integration**
  - BERT-based style classification
  - LightGBM for heading classification
  - Extractive summarization using `transformers`

- 🧩 **CLI + Streamlit**
  - CLI (`cli.py`) for quick local conversion
  - Streamlit app (`app.py`) for interactive UI

- 💡 **Customization**
  - Style and heading ML models trained on custom datasets
  - Output HTML using Jinja2 templates
  - Convert `.md` to rich HTML with classified sections

---

## 📂 Project Structure

markdown2html/
│
├── app.py # Streamlit Web App
├── cli.py # Command-Line Interface
├── converter.py # Core conversion logic
├── utils.py # Helpers
│
├── ml/
│ ├── classify_headings.py # Heading classifier
│ ├── style_predictor.py # Style classifier
│ ├── summarize.py # Summarization
│ └── datasets/ # Custom datasets
│
├── models/ # Trained ML models
│
├── templates/
│ └── base.html # HTML template for rendering
├── tests/
│ └── test_converter.py # Unit tests
│
├── sample.md # Example Markdown file
├── output/sample.html # Generated HTML
├── requirements.txt # Python dependencies
└── README.md # You are here

yaml
Copy
Edit

---

## 🧪 Quick Start

### ⚙️ Installation

```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate    # On Windows

# Install dependencies
pip install -r requirements.txt
🖥️ Run Streamlit App
bash
Copy
Edit
streamlit run app.py
🧵 Run CLI
bash
Copy
Edit
python cli.py sample.md
🧠 Training the Models
Use ml/datasets/styles.csv and ml/datasets/headings.csv to train or update models.

Models stored in models/

Style classification uses HuggingFace BERT (AutoModelForSequenceClassification)

Heading classification uses LightGBM

🛠️ Challenges Faced
1. SSH Key Setup for GitHub
Faced "Permission denied (publickey)"

Solution: Generated SSH keys and added them to GitHub → Guide

2. GitHub LFS Limitation
model.safetensors was 417MB, exceeding GitHub's 100MB limit

Git LFS also failed due to free bandwidth quota

Solution:

Removed the model from Git tracking

Ignored it via .gitignore

Suggested: Host model on Hugging Face or Google Drive and auto-download it

3. Rebase Conflicts
Initial push failed due to conflict with the remote repo

Resolved merge conflicts and used git rebase --continue after manual resolution

📌 TODOs
 Auto-download large models from Hugging Face

 Improve summarization quality (use Pegasus or LLaMA 3)

 Dark mode toggle in UI

 Unit test coverage > 90%

🙌 Credits
Streamlit

Hugging Face Transformers

LightGBM

Python-Markdown

📃 License
MIT License — free to use, modify, and distribute

💡 Author
Shashank Tiwari
GitHub: @shashankt1
Email: shashankt16@gmail.com
