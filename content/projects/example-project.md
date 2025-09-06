---
type: "project"
title: "Example Project"
slug: "example-project"
date: "2024-01-15"
tags: ["Python", "Flask", "Web Development"]
thumbnail: "example-project-thumb.jpg"
hero: "example-project-hero.jpg"
summary: "A sample project to demonstrate the portfolio system's capabilities with Markdown rendering, code highlighting, and LaTeX support."
github_url: "https://github.com/sethrobles/example-project"
live_url: "https://example-project.demo.com"
show_toc: false
hidden: true
---

<h2 style="text-align:center;">What I Learned</h2>


## Features

- **Markdown Rendering**:
- **Code Highlighting**: Syntax highlighting for multiple languages
- **LaTeX Support**: Mathematical equations using MathJax
- **Responsive Design**: Mobile-first approach
- **Dark/Light Mode**: Theme switching with CSS variables

## Code Examples

Here's some Python code with syntax highlighting:

```python
from flask import Flask, render_template
import markdown

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
```

And some JavaScript:

```javascript
class PortfolioWidget {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.init();
    }

    init() {
        console.log('Widget initialized!');
    }
}
```

## Mathematical Content

The portfolio supports LaTeX equations:

Inline math: $E = mc^2$

Block math:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

## Project Structure

```
project/
├── app.py
├── config.py
├── templates/
│   ├── base.html
│   └── home.html
├── static/
│   ├── css/
│   └── js/
└── content/
    └── projects/
```

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Content**: Markdown with frontmatter
- **Styling**: CSS Grid, Flexbox, CSS Variables
- **Deployment**: Render, Gunicorn

## Future Enhancements

- [ ] Database integration
- [ ] Blog functionality
- [ ] Advanced search
- [ ] Analytics dashboard
- [ ] API endpoints

## Conclusion

This example project showcases the portfolio system's capabilities and provides a foundation for real projects to be added.


{{ carousel([
  {'src': 'suction-tank-thumb.jpg', 'alt': 'First', 'caption': 'First image'},
  {'src': '/static/uploads/projects/suction-tank/suction-tank-thumb.jpg', 'alt': 'Second', 'caption': 'Second image'},
  {'src': '/static/uploads/blogs/gtl-italy/gtl-experiment.jpeg', 'alt': 'Third', 'caption': 'Third image'},
  {'src': '/static/uploads/blogs/gtl-italy/gtl-experiment.jpeg', 'alt': 'Fourth', 'caption': 'Fourth image'}
]) }}
