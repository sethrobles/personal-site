---
type: "blog"
title: "Camp Kesem 2025"
slug: "camp-kesem-2025"
date: "2025-08-17"
tags: ["Mentoring"]
thumbnail: "camp-kesem-2025-thumb.jpg"
hero: "flask-week-hero.jpg"
summary: "A week-long summer camp to help support children whose parents have been affected by cancer"
# github_url: "https://github.com/sethrobles/flask-week"
# live_url: "https://flask-week.demo.com"
show_toc: false
hidden: false
---

# A Week of Learning Flask

This past week, I decided to take Flask seriously. I'd tinkered with it before, but never really built something that felt *usable*. By the end of the week, I had a simple blog running locally, a newfound respect for routing, and a list of mistakes I’ll probably laugh at later.

## What Clicked

There were a few moments that made everything feel less intimidating:

- **Routes are just functions**: The idea that `@app.route("/")` is just mapping a URL to a Python function made things *click*.I'm
- **Jinja Templates**: At first, mixing HTML and curly braces felt strange, but then I realized how powerful templating is.
- **Server Reloads**: Flask reloading on save was both a blessing (fast feedback) and a curse (when I broke everything five times in a row).

## Code That Made Me Smile

Here’s the first “real” route I wrote that didn’t feel like just a toy example:

```python
from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"title": "First Post", "content": "This is where it all began."},
    {"title": "Second Post", "content": "Now it feels like a blog."}
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)
