
import os
import sys
sys.path.append(os.path.abspath('.'))

project = 'Tetrad Manual'
author = 'Tetrad Team'
copyright = '2025'
extensions = [
    'myst_parser',
    'sphinx.ext.autosectionlabel',
]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
]
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
# Add a top-level nav link back to the manual homepage if desired
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "sticky_navigation": True,
}
# Let raw HTML be rendered inside Markdown (MyST handles this).
myst_heading_anchors = 3
