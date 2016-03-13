Skip to content
This repository  
Search
Pull requests
Issues
Gist
 @bdemchak
 Watch 2
  Star 0
 Fork 1 kozo2/cytoscape3-usermanual
 Code  Issues 2  Pull requests 0  Wiki  Pulse  Graphs
Branch: master Find file Copy pathcytoscape3-usermanual/conf.py
b8d8569  on Nov 18, 2015
@kozo2 kozo2 prepare to move from mkdocs to sphinx
1 contributor
RawBlameHistory     62 lines (46 sloc)  1.19 KB
extensions = []
templates_path = ['_templates']

master_doc = 'index'

project = u'Test'
copyright = u'2015, Test'
author = u'Test'

version = 'test'
release = 'test'
language = None

exclude_patterns = ['_build']
pygments_style = 'sphinx'

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']
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
  (master_doc, 'Test.tex', u'Test Documentation',
   u'Test', 'manual'),
]

man_pages = [
    (master_doc, 'test', u'Test Documentation',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'Test', u'Test Documentation',
   author, 'Test', 'One line description of project.',
   'Miscellaneous'),
]

from recommonmark.parser import CommonMarkParser

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

source_parsers = {
	'.md': CommonMarkParser,
}
Status API Training Shop Blog About Pricing
© 2016 GitHub, Inc. Terms Privacy Security Contact Help
