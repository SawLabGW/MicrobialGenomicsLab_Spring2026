# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Microbial Genomics Lab Spring 2026'
copyright = '2026, Jimmy H. Saw'
author = 'Jimmy H. Saw'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']

## cloud_sptheme (options: cloud, greencloud, magenta_cloud, redcloud, solarcloud)
from cloud_sptheme import themes
#html_theme = 'cloud'
html_theme = 'greencloud'
#html_theme = 'redcloud'

## set pygments styles
#pygments_style = 'arduino'
pygments_style = 'tango'
#pygments_style = 'trac'
#pygments_style = 'friendly'
#pygments_style = 'autumn'
#pygments_style = 'solarized-light'
#pygments_style = 'xcode'
#pygments_style = 'paraiso-light'
#pygments_style = 'lovelace'
#pygments_style = 'stata'
#pygments_style = 'vs'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']
html_logo = 'phylo.png'
