import os
import re
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

from flask import Flask, render_template, abort, send_from_directory, jsonify, request
from flask_compress import Compress
from flask_caching import Cache
from flask_cors import CORS
import markdown
import frontmatter
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
compress = Compress(app)
cache = Cache(app)

# Enable CORS if configured
if Config.should_enable_cors():
    CORS(app, origins=Config.get_cors_origins())

# Database setup (optional)
if Config.USE_DATABASE:
    try:
        from flask_sqlalchemy import SQLAlchemy
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db = SQLAlchemy(app)
        # TODO: Define models here when needed
    except ImportError:
        print("Warning: SQLAlchemy not available, database features disabled")
        Config.USE_DATABASE = False

class ContentManager:
    """Manages content loading and caching."""

    def __init__(self):
        self.projects_dir = Path(Config.PROJECTS_DIR)
        self.blog_dir = Path(Config.BLOG_DIR)
        self._projects_cache = {}
        self._cache_timestamps = {}

    def _get_markdown_content(self, file_path: Path) -> Optional[Dict]:
        """Parse Markdown file with frontmatter."""
        if not file_path.exists():
            return None

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            # Extract frontmatter
            metadata = dict(post.metadata)
            content = post.content

            # Parse Markdown content
            md = markdown.Markdown(extensions=Config.MARKDOWN_EXTENSIONS)
            html_content = md.convert(content)

            # Add code highlighting
            html_content = self._highlight_code_blocks(html_content)

            # Process metadata for templates
            processed_metadata = {}
            for key, value in metadata.items():
                if key == 'date' and isinstance(value, str):
                    try:
                        # Parse date string to datetime object
                        from datetime import datetime
                        processed_metadata[key] = datetime.strptime(value, '%Y-%m-%d').date()
                    except ValueError:
                        # Keep as string if parsing fails
                        processed_metadata[key] = value
                else:
                    processed_metadata[key] = value

            return {
                'metadata': processed_metadata,
                'content': html_content,
                'toc': md.toc if hasattr(md, 'toc') else ''
            }
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None

    def _highlight_code_blocks(self, html_content: str) -> str:
        """Apply syntax highlighting to code blocks."""
        # Find code blocks and apply highlighting
        code_block_pattern = r'<pre><code class="language-(\w+)">(.*?)</code></pre>'

        def highlight_match(match):
            language = match.group(1)
            code = match.group(2)

            try:
                lexer = get_lexer_by_name(language)
                formatter = HtmlFormatter(style=Config.CODE_HIGHLIGHT_STYLE)
                highlighted = highlight(code, lexer, formatter)
                return highlighted
            except:
                # Fallback to plain code if highlighting fails
                return f'<pre><code class="language-{language}">{code}</code></pre>'

        return re.sub(code_block_pattern, highlight_match, html_content, flags=re.DOTALL)

    def get_projects(self, limit: Optional[int] = None) -> List[Dict]:
        """Get all projects, optionally limited, excluding hidden ones."""
        projects = []

        if not self.projects_dir.exists():
            return projects

        for md_file in self.projects_dir.glob('*.md'):
            project = self._get_markdown_content(md_file)
            if project:
                # Exclude hidden projects
                if str(project['metadata'].get('hidden', 'false')).lower() == 'true':
                    continue
                project['slug'] = md_file.stem
                projects.append(project)

        def get_sort_key(project):
            date_val = project['metadata'].get('date', '')
            if hasattr(date_val, 'strftime'):
                return date_val
            elif isinstance(date_val, str):
                try:
                    from datetime import datetime
                    return datetime.strptime(date_val, '%Y-%m-%d').date()
                except ValueError:
                    return date_val
            return date_val

        try:
            projects.sort(key=get_sort_key, reverse=True)
        except (TypeError, ValueError) as e:
            print(f"Warning: Could not sort projects by date: {e}")
            projects.sort(key=lambda x: x['metadata'].get('title', ''))

        if limit:
            projects = projects[:limit]

        return projects

    def get_project(self, slug: str) -> Optional[Dict]:
        """Get a specific project by slug."""
        project_file = self.projects_dir / f"{slug}.md"
        project = self._get_markdown_content(project_file)
        if project:
            project['slug'] = slug
        return project

    def get_blog_posts(self, limit: Optional[int] = None) -> List[Dict]:
        """Get blog posts if blog directory exists, excluding hidden ones."""
        if not self.blog_dir.exists():
            return []

        posts = []
        for md_file in self.blog_dir.glob('*.md'):
            post = self._get_markdown_content(md_file)
            if post:
                # Exclude hidden blogs
                if str(post['metadata'].get('hidden', 'false')).lower() == 'true':
                    continue
                post['slug'] = md_file.stem
                posts.append(post)

        def get_sort_key(post):
            date_val = post['metadata'].get('date', '')
            if hasattr(date_val, 'strftime'):
                return date_val
            elif isinstance(date_val, str):
                try:
                    from datetime import datetime
                    return datetime.strptime(date_val, '%Y-%m-%d').date()
                except Exception:
                    return date_val
            return date_val

        try:
            posts.sort(key=get_sort_key, reverse=True)
        except Exception as e:
            print(f"Warning: Could not sort blog posts by date: {e}")
            posts.sort(key=lambda x: x['metadata'].get('title', ''))

        if limit:
            posts = posts[:limit]

        return posts

    def get_blog_post(self, slug: str) -> Optional[Dict]:
        """Get a specific blog post by slug."""
        if not self.blog_dir.exists():
            return None

        post_file = self.blog_dir / f"{slug}.md"
        post = self._get_markdown_content(post_file)
        if post:
            post['slug'] = slug
        return post

# Initialize content manager
content_manager = ContentManager()

# Make content_manager available to all templates
@app.context_processor
def inject_content_manager():
    return dict(content_manager=content_manager)

@app.route('/')
def home():
    """Home page with featured projects and blogs as featured work."""
    featured_projects = content_manager.get_projects(limit=3)
    featured_blogs = content_manager.get_blog_posts(limit=3)
    # Combine and sort by date (newest first)
    featured_work = featured_projects + featured_blogs

    def get_sort_key(item):
        date_val = item['metadata'].get('date', '')
        if hasattr(date_val, 'strftime'):
            return date_val
        elif isinstance(date_val, str):
            try:
                from datetime import datetime
                return datetime.strptime(date_val, '%Y-%m-%d').date()
            except Exception:
                return date_val
        return date_val

    try:
        featured_work.sort(key=get_sort_key, reverse=True)
    except Exception as e:
        print(f"Warning: Could not sort featured work by date: {e}")
        featured_work.sort(key=lambda x: x['metadata'].get('title', ''))
    return render_template('home.html', featured_work=featured_work)

@app.route('/projects/')
def projects_index():
    """Projects index page."""
    all_projects = content_manager.get_projects()
    return render_template('projects_index.html', projects=all_projects)

@app.route('/projects/<slug>/')
def project_detail(slug):
    """Individual project detail page."""
    project = content_manager.get_project(slug)
    if not project:
        abort(404)
    # Flatten metadata for template compatibility
    if 'metadata' in project:
        for k, v in project['metadata'].items():
            project[k] = v
    project['type'] = 'project'
    return render_template('entry_detail.html', entry=project)

@app.route('/resume/')
def resume():
    """Resume page with PDF embed."""
    return render_template('resume.html')

@app.route('/portfolio/')
def portfolio():
    """Portfolio page with PDF embed."""
    return render_template('portfolio.html')

@app.route('/blog/')
def blog_index():
    """Blog index page (optional)."""
    posts = content_manager.get_blog_posts()
    return render_template('blog_index.html', posts=posts)

@app.route('/blog/<slug>/')
def blog_post(slug):
    """Individual blog post page."""
    post = content_manager.get_blog_post(slug)
    if not post:
        abort(404)
    # Flatten metadata for template compatibility
    if 'metadata' in post:
        for k, v in post['metadata'].items():
            post[k] = v
    post['type'] = 'blog'
    return render_template('entry_detail.html', entry=post)

@app.route('/api/strava/latest')
def strava_latest():
    """API endpoint for Strava activities."""
    if not Config.STRAVA_API_BASE:
        return jsonify({'error': 'Strava API not configured'}), 400

    per_page = request.args.get('per_page', 5, type=int)

    # TODO: Implement actual Strava API call
    # For now, return placeholder data
    return jsonify({
        'activities': [
            {
                'id': 1,
                'name': 'Morning Run',
                'type': 'Run',
                'distance': '5.2 km',
                'duration': '25:30',
                'date': '2024-01-15'
            }
        ]
    })

@app.route('/health')
def health_check():
    """Health check endpoint for uptime monitoring."""
    return jsonify({'ok': True, 'timestamp': datetime.utcnow().isoformat()})

@app.route('/uploads/<path:filename>')
def uploads(filename):
    """Serve uploaded files."""
    return send_from_directory(Config.UPLOADS_DIR, filename)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
