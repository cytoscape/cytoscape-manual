# cytoscape-manual
Markdown version of Cytoscape manual

Kozo's instructions:

1. I exported http://wiki.cytoscape.org/Cytoscape_3/UserManual to a
docbook xml. (https://github.com/kozo2/cytoscape3-usermanual/blob/master/UserManual.xml)

2. I converted UserManual.xml to UserManual.md
(https://github.com/kozo2/cytoscape3-usermanual/blob/master/UserManual.md)
with ```pandoc -f docbook -t markdown -s UserManual.xml -o UserManual.md```

3. I separated UserManual.md per chapter manually.
(https://github.com/kozo2/cytoscape3-usermanual/tree/master/docs)

4. I built and deployed 3. with mkdocs and readthedocs.
