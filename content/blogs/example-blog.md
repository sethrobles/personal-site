---
type: "blog"
title: "A Week of Learning Flask"
slug: "week-of-flask"
date: "2024-02-10"
tags: ["Python", "Flask", "Web Development", "Learning"]
thumbnail: "flask-week-thumb.jpg"
hero: "flask-week-hero.jpg"
summary: "Reflections on my first week diving deep into Flask, building small apps, and realizing the joys (and quirks) of web development with Python."
github_url: "https://github.com/sethrobles/flask-week"
live_url: "https://flask-week.demo.com"
show_toc: false
hidden: true
---




Links
[Camp Kesem website](https://www.campkesem.org/)


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


{{ carousel([
  {'src': '/static/uploads/blogs/gtl-italy/gtl-experiment.jpeg', 'alt': 'First', 'caption': 'First image'},
  {'src': '/static/uploads/blogs/gtl-italy/gtl-experiment.jpeg', 'alt': 'Second', 'caption': 'Second image'},
  {'src': '/static/uploads/blogs/gtl-italy/gtl-experiment.jpeg', 'alt': 'Third', 'caption': 'Third image'},
  {'src': '/static/uploads/blogs/gtl-italy/gtl-experiment.jpeg', 'alt': 'Fourth', 'caption': 'Fourth image'}
]) }}
