# Seth Robles - Portfolio Website

A modern, responsive portfolio website built with Flask, featuring Markdown content management, dark/light mode, and interactive widgets.

## Features

- 🎨 **Modern Design**: Clean, professional design with dark/light mode toggle
- 📱 **Responsive**: Mobile-first approach with CSS Grid and Flexbox
- 📝 **Markdown Content**: Projects and blog posts written in Markdown with frontmatter
- 🎯 **Code Highlighting**: Syntax highlighting for code blocks using Pygments
- 📊 **LaTeX Support**: Mathematical equations rendered with MathJax
- 🏃‍♂️ **Strava Widget**: Integration with Strava API for fitness activities
- 📚 **Goodreads Widget**: Placeholder for reading progress integration
- 🚀 **Performance**: Flask-Compress and caching for optimal performance
- 🔒 **Security**: Environment-based configuration with no hardcoded secrets

## Tech Stack

- **Backend**: Python 3 + Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Content**: Markdown with python-frontmatter
- **Styling**: CSS Grid, Flexbox, CSS Variables
- **Code Highlighting**: Pygments
- **Math Rendering**: MathJax
- **Deployment**: Render (with Gunicorn)

## Project Structure

```
personal-site-2/
├── app.py                 # Main Flask application
├── config.py             # Configuration and environment variables
├── requirements.txt      # Python dependencies
├── Procfile             # Deployment configuration
├── render.yaml          # Render deployment config
├── README.md            # This file
├── content/             # Content directory
│   ├── projects/        # Project Markdown files
│   └── blog/           # Blog post Markdown files
├── static/              # Static assets
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   └── uploads/        # Images, PDFs, and other files
└── templates/           # Jinja2 templates
    ├── base.html        # Base template
    ├── home.html        # Home page
    ├── projects_index.html  # Projects listing
    ├── project_detail.html  # Individual project page
    ├── resume.html      # Resume page
    ├── portfolio.html   # Portfolio page
    ├── 404.html         # 404 error page
    ├── 500.html         # 500 error page
    └── _components/     # Reusable components
        ├── navbar.html   # Navigation component
        ├── footer.html   # Footer component
        └── card.html     # Project/blog card component
```

## Local Development

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd personal-site-2
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables** (optional)
   ```bash
   export STRAVA_API_BASE="https://your-api.onrender.com"
   export CORS_ALLOWED_ORIGIN="https://yourdomain.com"
   export USE_DATABASE="false"
   export DATABASE_URL="postgresql://..."
   export PLAUSIBLE_DOMAIN="yourdomain.com"
   ```

5. **Run the development server**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `STRAVA_API_BASE` | Base URL for Strava API integration | `None` | No |
| `CORS_ALLOWED_ORIGIN` | Allowed CORS origin for external API calls | `None` | No |
| `USE_DATABASE` | Enable database features (SQLAlchemy) | `"false"` | No |
| `DATABASE_URL` | PostgreSQL connection string | `None` | No |
| `PLAUSIBLE_DOMAIN` | Domain for Plausible Analytics | `None` | No |
| `SECRET_KEY` | Flask secret key for sessions | Auto-generated | No |

## Content Management

### Adding Projects

1. Create a new Markdown file in `content/projects/`
2. Use the following frontmatter structure:

```yaml
---
title: "Project Title"
slug: "project-slug"
date: "2024-01-15"
tags: ["Python", "Flask", "Web Development"]
thumbnail: "project-thumb.jpg"
hero: "project-hero.jpg"
summary: "Brief project description"
github_url: "https://github.com/username/project"
live_url: "https://project.demo.com"
---
```

3. Add your project content below the frontmatter
4. Place images in `static/uploads/`

### Adding Blog Posts

1. Create a new Markdown file in `content/blog/`
2. Use similar frontmatter structure as projects
3. Write your blog content in Markdown

### Supported Markdown Features

- **Code Blocks**: Use triple backticks with language specification
- **LaTeX**: Inline math with `$...$`, block math with `$$...$$`
- **Images**: Standard Markdown image syntax
- **Tables**: Standard Markdown table syntax
- **Lists**: Ordered, unordered, and task lists

## Deployment

### Render (Recommended)

1. **Connect your repository** to Render
2. **Create a new Web Service**
3. **Configure environment variables** as needed
4. **Deploy automatically** on git push

The `render.yaml` file is pre-configured for easy deployment.

### Other Platforms

- **Heroku**: Use the `Procfile` and `requirements.txt`
- **Vercel**: Configure as a Python application
- **Railway**: Use the existing configuration files

## Customization

### Styling

- Modify `static/css/base.css` for design changes
- CSS variables control the color scheme and theming
- Dark/light mode colors are defined in `:root` and `[data-theme="dark"]`

### Components

- Edit templates in `templates/_components/` for reusable elements
- Modify `static/js/widgets.js` for JavaScript functionality
- Add new routes in `app.py` for additional pages

### Widgets

- **Strava**: Configure `STRAVA_API_BASE` and implement API calls
- **Goodreads**: Extend the existing placeholder widget
- **Custom**: Add new widgets following the existing pattern

## Performance Optimization

- **Flask-Compress**: Automatic gzip compression
- **Flask-Caching**: In-memory caching for parsed Markdown
- **Image Optimization**: Optimize images before uploading
- **CDN**: Consider using a CDN for static assets in production

## Security Considerations

- **Environment Variables**: Never commit secrets to version control
- **CORS**: Only enable when necessary for external API integration
- **File Uploads**: The uploads directory is public - only upload safe files
- **HTTPS**: Always use HTTPS in production

## Browser Support

- **Modern Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **Mobile**: iOS Safari, Chrome Mobile
- **Features**: CSS Grid, CSS Variables, ES6+ JavaScript

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues:
- Create an issue on GitHub
- Contact: seth@example.com
- Portfolio: [sethrobles.com](https://sethrobles.com)

## Roadmap

- [ ] Database integration with SQLAlchemy
- [ ] Advanced search and filtering
- [ ] Blog comments system
- [ ] Admin panel for content management
- [ ] Analytics dashboard
- [ ] Newsletter integration
- [ ] Social media sharing
- [ ] SEO optimization tools
