# converter.py

from markdown2 import markdown
from ml.style_predictor import predict_style
from ml.classify_headings import predict_heading
from ml.summarize import summarize_text

def convert_markdown(text: str, verbose: bool = False) -> str:
    """
    Convert markdown text into HTML string with ML-powered:
     - Heading classification (`heading1`, `heading2`, default markdown)
     - Paragraph styling (BERT tone prediction)
     - Section summarization (optional)
    """
    lines = text.splitlines()
    html_lines = []

    for line in lines:
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            html_lines.append("")
            continue

        # Heading detection via ML
        heading_type = predict_heading(stripped)
        if heading_type == "heading1":
            html_lines.append(f"<h1>{stripped}</h1>")
            continue
        elif heading_type == "heading2":
            html_lines.append(f"<h2>{stripped}</h2>")
            continue

        # Summarization if the line is long
        if len(stripped) > 200:
            summary = summarize_text(stripped)
            html_lines.append(f'<div class="summary-block"><strong>Summary:</strong> {summary}</div>')
        
        # Style prediction for paragraph
        style = predict_style(stripped)
        html_lines.append(f'<p class="style-{style}">{markdown(stripped)}</p>')

    return "\n".join(html_lines)
