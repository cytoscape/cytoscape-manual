extensions = [] # this gives build errors: extensions = ['recommonmark']
templates_path = ['_templates']

master_doc = 'index'

project = u'Cytoscape User Manual'
copyright = u'2021, The Cytoscape Consortium'
author = u'The Cytoscape Consortium'

version = '3.10.0'
release = '3.10.0'
language = None

exclude_patterns = ['_build']
pygments_style = 'sphinx'

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
def setup(app):
  app.add_stylesheet( "css/tables.css" )
# from http://stackoverflow.com/questions/32079200/how-do-i-set-up-custom-styles-for-restructuredtext-sphinx-readthedocs-etc/32079202#32079202

html_static_path = ['_static']
html_show_sourcelink = True
htmlhelp_basename = 'Testdoc'
html_logo = '_static/images/cytoscape3-icon-trans-128x128.png'
html_favicon = '_static/images/cytoscape3-icon.ico'

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

from recommonmark.parser import CommonMarkParser

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

source_parsers = {
	'.md': CommonMarkParser,
}


