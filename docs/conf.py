extensions = ["myst_parser", "sphinxcontrib.jquery"] ## recommonmark is deprecated, switch to myST. sphinxcontrib.jquery is necessary to fix a buggy version selector (KH). 
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md'] 

master_doc = 'index'

project = u'Cytoscape User Manual'
copyright = u'2024, The Cytoscape Consortium'
author = u'The Cytoscape Consortium'

version = '3.10.2'
release = '3.10.2'
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path. Added _templates based on py4cytoscape conf.py (KH)
exclude_patterns = ['_build', '_templates']

pygments_style = 'sphinx'

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

## app.add_stylesheet() method is deprecated, switch to using html_css_files = [] below (KH)
#def setup(app):
  #app.add_stylesheet( "css/tables.css" ) ##deprecated method
# from http://stackoverflow.com/questions/32079200/how-do-i-set-up-custom-styles-for-restructuredtext-sphinx-readthedocs-etc/32079202#32079202
html_logo = '_static/images/cytoscape3-icon-trans-128x128.png'
html_favicon = '_static/images/cytoscape3-icon.ico'

## Set theme options (theme-specific) (KH)
html_theme_options = {
    'prev_next_buttons_location': 'both',
    'navigation_depth': 4,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/tables.css']

html_show_sourcelink = True
htmlhelp_basename = 'Testdoc'

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

latex_documents = [
  (master_doc, 'Test.tex', u'Cytoscape User Manual',
   u'The Cytoscape Consortium', 'manual'),
]

man_pages = [
    (master_doc, 'test', u'Cytoscape User Manual',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'Test', u'Cytoscape User Manual',
   author, 'Test', 'Cytoscape User Manual',
   'Miscellaneous'),
]


