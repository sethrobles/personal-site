---
type: "project"
title: "LED Array"
slug: "led-array"
date: "2025-08-22"
tags: ["KiCAD", "PCB Design", "STM32 Design"]
thumbnail: "led-array-thumb.png"
# hero: "example-project-hero.jpg"
summary: "A 4-layer PCB with an STM32 microcontroller using shift-registers and MOSFETs with a 1/8 scan."
github_url: "https://github.com/sethrobles/led-array"
# live_url: "https://example-project.demo.com"
show_toc: false
hidden: false
---

This is a sample project that demonstrates the portfolio system's capabilities.

## Features

- **Markdown Rendering**: Full Markdown support with extensions
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




August 23rd.

I'm working on setting up the PCB-layout in KiCAD, which I have nver done. There are 32x32 LEDs, so there's a lot of components to lay out and I don't want to do it on my own. Thankfully i have hiearchical sheets set up and am not trying ot use replicate layout.


https://github.com/MitjaNemec/ReplicateLayout?tab=readme-ov-file

I downloaded the zip file from there and in KiCAD went to tools -> external plugs -> "Reval plugin folder in Finder"


I was getting an issue when i ran it so I did htis:


Edit one line in the plugin to make it KiCad-8 safe.

Open this file in a text editor:
~/Library/Preferences/kicad/8.0/scripting/plugins/replicate_layout/replicate_layout.py
(If you installed under ~/Documents/KiCad/8.0/..., use that path instead.)

Go to ~line 930 (near where it says Replicating footprints). Find the line:

dst_fp.fp.SetLocalZoneConnection(src_fp.fp.GetLocalZoneConnection())


Replace it with a safe fallback that works across KiCad 6/7/8:

# KiCad 7 had SetLocalZoneConnection/GetLocalZoneConnection.
# KiCad 8 changed/removed those; try both, fall back quietly.
try:
    dst_fp.fp.SetLocalZoneConnection(src_fp.fp.GetLocalZoneConnection())
except AttributeError:
    try:
        dst_fp.fp.SetZoneConnection(src_fp.fp.GetZoneConnection())
    except AttributeError:
        pass  # No per-footprint zone connection API in this build
