"# Entry point" 
import click
from converter import convert_markdown_to_html
from utils import save_html, open_in_browser
from pathlib import Path

@click.group()
def cli():
    """Markdown to HTML Converter CLI"""
    pass

@cli.command()
@click.argument('markdown_file', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), help="Output HTML file path.")
@click.option('--open', 'open_browser', is_flag=True, help="Open the HTML file in browser.")
@click.option('--verbose', is_flag=True, help="Show conversion details.")
def convert(markdown_file, output, open_browser, verbose):
    """Convert a Markdown file to HTML."""
    markdown_path = Path(markdown_file)
    html_content = convert_markdown_to_html(markdown_path, verbose)

    output_path = save_html(html_content, markdown_path, output)
    
    if verbose:
        click.echo(f"✅ Saved to: {output_path}")

    if open_browser:
        open_in_browser(output_path)

if __name__ == "__main__":
    cli()