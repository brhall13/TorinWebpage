import os
from flask import Flask, render_template, abort
import markdown

app = Flask(__name__, static_url_path='/repository-name/static')

def load_markdown(filename):
    """Load a Markdown file from the content directory and convert it to HTML."""
    file_path = os.path.join("content", filename)
    if not os.path.exists(file_path):
        abort(404)
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return markdown.markdown(text)

@app.route('/')
def home():
    # This loads content/home.md.
    content = load_markdown("home.md")
    print(content)
    return render_template("base.html", content=content)

@app.route('/<page_name>')
def page(page_name):
    # For any other URL
    filename = f"{page_name}.md"
    content = load_markdown(filename)
    return render_template("base.html", content=content)

if __name__ == '__main__':
    app.run(debug=True)
