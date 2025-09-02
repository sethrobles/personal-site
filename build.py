
import os
import json
import frontmatter
import markdown
from pathlib import Path
from staticjinja import Site

# Load socials
SOCIALS_PATH = "private/socials.json"
def load_socials():
    if os.path.exists(SOCIALS_PATH):
        with open(SOCIALS_PATH) as f:
            return json.load(f)
    return {}

# Markdown and content helpers
def parse_markdown(md_path):
    post = frontmatter.load(md_path)
    content = markdown.markdown(post.content, extensions=[
        'extra', 'toc', 'fenced_code', 'codehilite', 'sane_lists', 'admonition'
    ])
    return {
        'metadata': dict(post.metadata),
        'content': content,
        'slug': md_path.stem
    }

def get_projects():
    projects_dir = Path('content/projects')
    projects = []
    for md_file in projects_dir.glob('*.md'):
        proj = parse_markdown(md_file)
        if str(proj['metadata'].get('hidden', 'false')).lower() != 'true':
            projects.append(proj)
    projects.sort(key=lambda x: x['metadata'].get('date', ''), reverse=True)
    return projects

def get_blogs():
    blogs_dir = Path('content/blogs')
    blogs = []
    for md_file in blogs_dir.glob('*.md'):
        blog = parse_markdown(md_file)
        if str(blog['metadata'].get('hidden', 'false')).lower() != 'true':
            blogs.append(blog)
    blogs.sort(key=lambda x: x['metadata'].get('date', ''), reverse=True)
    return blogs

socials = load_socials()
print("DEBUG socials", socials)
projects = get_projects()
blogs = get_blogs()

# Context functions for each template
def home_context(template):
    featured_projects = projects[:3]
    featured_blogs = blogs[:3]
    featured_work = sorted(featured_projects + featured_blogs, key=lambda x: x['metadata'].get('date', ''), reverse=True)
    return {'featured_work': featured_work, 'socials': socials}

def projects_index_context(template):
    return {'projects': projects, 'socials': socials}

def blog_index_context(template):
    return {'posts': blogs, 'socials': socials}

def entry_detail_context(template):
    # This will be set per-render below
    return {}



site = Site.make_site(
    searchpath='templates',
    outpath='output',
    contexts=[
        ('home.html', home_context),
        ('projects_index.html', projects_index_context),
        ('blog_index.html', blog_index_context),
        ('.*', lambda template: {'socials': socials})
    ]
)

# Debug: print outpath type and value
print(f"site.outpath type: {type(site.outpath)}, value: {site.outpath}")



# Render index pages using Jinja2's stream().dump() to avoid staticjinja rule errors
site.get_template('home.html').stream(home_context(None)).dump(os.path.join(site.outpath, 'index.html'))
site.get_template('projects_index.html').stream(projects_index_context(None)).dump(os.path.join(site.outpath, 'projects_index.html'))
site.get_template('blog_index.html').stream(blog_index_context(None)).dump(os.path.join(site.outpath, 'blog_index.html'))

# Render detail pages for projects and blogs
def render_detail_pages(site, items, template_name, outdir):
    for item in items:
        context = {'entry': item, 'socials': socials}
        outpath = os.path.join(site.outpath, outdir, f"{item['slug']}.html")
        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        site.get_template(template_name).stream(context).dump(outpath)

render_detail_pages(site, projects, 'entry_detail.html', 'projects')
render_detail_pages(site, blogs, 'entry_detail.html', 'blogs')

# Render static pages
site.get_template('resume.html').stream({'socials': socials}).dump(os.path.join(site.outpath, 'resume.html'))
site.get_template('portfolio.html').stream({'socials': socials}).dump(os.path.join(site.outpath, 'portfolio.html'))
site.get_template('404.html').stream({'socials': socials}).dump(os.path.join(site.outpath, '404.html'))
site.get_template('500.html').stream({'socials': socials}).dump(os.path.join(site.outpath, '500.html'))



import shutil

src_static = "static"
dst_static = os.path.join(site.outpath, "static")
if os.path.exists(dst_static):
    shutil.rmtree(dst_static)
shutil.copytree(src_static, dst_static)
