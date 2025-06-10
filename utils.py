# Helpers 
from pathlib import Path
import webbrowser

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> Markdown To HMTL</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css/github-markdown.min.css">
</head>
<body class="markdown-body">
{body}
</body>
</html>
"""

def save_html(html_body, source_path, output=None):
    title = source_path.stem
    full_html = TEMPLATE.format(title=title, body=html_body)

    if output:
        output_path = Path(output)
    else:
        output_path = Path("output") / f"{title}.html"
        output_path.parent.mkdir(exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    return output_path.resolve()

def open_in_browser(html_path):
    webbrowser.open(f"file://{html_path}")