import os
from typing import Optional

class Config:
    """Configuration class for the Flask application."""

    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

    # Content settings
    CONTENT_DIR = 'content'
    PROJECTS_DIR = os.path.join(CONTENT_DIR, 'projects')
    BLOG_DIR = os.path.join(CONTENT_DIR, 'blog')
    UPLOADS_DIR = 'static/uploads'

    # Caching
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300  # 5 minutes

    # External APIs
    STRAVA_API_BASE = os.environ.get('STRAVA_API_BASE')
    CORS_ALLOWED_ORIGIN = os.environ.get('CORS_ALLOWED_ORIGIN')

    # Database (optional)
    USE_DATABASE = os.environ.get('USE_DATABASE', 'false').lower() == 'true'
    DATABASE_URL = os.environ.get('DATABASE_URL')

    # Analytics
    PLAUSIBLE_DOMAIN = os.environ.get('PLAUSIBLE_DOMAIN')

    # Markdown extensions
    MARKDOWN_EXTENSIONS = [
        'extra',
        'toc',
        'fenced_code',
        'codehilite',
        'sane_lists',
        'admonition'
    ]

    # Code highlighting style
    CODE_HIGHLIGHT_STYLE = 'monokai'

    @classmethod
    def should_enable_cors(cls) -> bool:
        """Check if CORS should be enabled based on environment."""
        return bool(cls.STRAVA_API_BASE and cls.CORS_ALLOWED_ORIGIN)

    @classmethod
    def get_cors_origins(cls) -> list:
        """Get list of allowed CORS origins."""
        if not cls.should_enable_cors():
            return []
        return [cls.CORS_ALLOWED_ORIGIN]
