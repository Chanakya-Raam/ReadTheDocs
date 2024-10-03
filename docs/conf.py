# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'FastApi Documentation'
copyright = '2024, Chanakya Terala'
author = 'Chanakya Terala'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',       # Automatically document your code
    'sphinx.ext.napoleon',      # For Google and NumPy style docstrings
    'sphinx.ext.viewcode',      # Add links to highlighted source code
    'sphinx_rtd_theme',         # Read the Docs theme
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Changing the theme to Read the Docs
html_static_path = ['_static']
