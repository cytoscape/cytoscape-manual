# cytoscape-manual
###Cytoscape User manual

This project contains the complete user manual for Cytoscape 3. It has tags identifying the material that goes into the user manual for each version. A tag is formatted according to semantic versioning rules (e.g., 3.3).

The outstanding issues are identified as GitHub Issues. The main outstanding issues are getting document (including tables) to format properly (or at all) in PDF.

While the manual sources are maintained in GitHub, the document is actually assembled, formatted, and staged by the ReadTheDocs.org site. ReadTheDocs presents online and PDF versions, and we will use both.

ReadTheDocs can present versions of the manual for each Cytoscape release, as identified by GitHub tags. For example, given a tag of 3.3, ReadTheDocs will produce a document containing the repository files as they were for Cytoscape 3.3, and will make it available at http://manual.cytoscape.org/en/3.3. ReadTheDocs will make a "stable" version of the manual available at http://manual.cytoscape.org/en/stable ... it will resolve to the latest tagged version (ignoring beta versions such as 3.4b1). The "latest" version of the manual will be available at http://manual.cytoscape.org/en/latest, and will contain all of the latest GitHub content, irrespective of tagging.

Note that for a manual under developement, we should make "latest" non-public (configurable in ReadTheDocs) so it isn't indexed by Google.

## Editing the Manual
To edit manual text, you must first check out this repository and use a text editor on your workstation. (You can use GitHub's native Markdown editor, too, for small edits.)

All document components are in the "docs" directory. Each chapter is contained in its own file, and the files are assembled as a complete document by naming them in the "docs/index.rst" file.

Images are stored in the "docs/_static/images" directory, organized into subdirectories by chapter. For high quality images, vector graphic files produce best results (e.g., .png).

Simple tables can be represented in Markdown, but high quality formatting requires direct HTML coding. By convention, we encode tables as HTML-tagged data, but do not specify visual attributes and layout inline. Instead, we use preset table styles contained in "docs/_static/css" for formatting -- we do not use Markdown's table formatting. Note that additional CSS files can be added, but must be accounted for in "_templates/layout.html" and "conf.py". Note that while the tables appear in the HTML document, they do not appear in the PDF version -- we're working on this.

Note that the GitHub file viewer displays Markdown files reasonably well. However, it only approximates the look of tables created via HTML. For an accurate view of a table, you must look at a document rendered by ReadTheDocs.

Note that a full (browsable) link to a location has the form: "http://manual.cytoscape.org/en/stable/Launching_Cytoscape.html#mylink" where "http://manual.cytoscape.org/en/stable/" is the full URL, "Launching_Cytoscape" is the root name of the file containing the target link, and "mylink" is a named section (e.g., <a name="mylink">System requirements</a>). A link between chapters in the document has the form [My Link](Launching_Cytoscape.html#mylink), and a link within the same chapter can have the form [My Link](#mylink). For intra-document references, best to use the Launching_Cytoscape.html#mylink form, as ReadTheDocs will append the full URL appropriate for the build (e.g., "stable", "latest", "3.3", etc).

## Rebuilding the Manual
The "latest" manual is automatically rebuilt by ReadTheDocs when the GitHub repository is updated. (This is courtesy of a WebHook that I installed per http://docs.readthedocs.org/en/latest/webhooks.html). To rebuild other versions, you'll need to be in the ReadTheDocs web site on the Build page -- there should be little/no reason to ever do this.

The rebuild can be observed by logging into the ReadTheDocs account (see me for credentials) and choosing the "Cytoscape User Manual" project. To see the build log, click on the grey Builds button. You can watch the progress of the build by manually refreshing your browser window until the build status shows either Passed or Failed - a build can take anywhere from 3 minutes to 10 minutes, depending on how busy the build server is. When the build is complete, if the status shows Passed, you can view the build result by clicking on the green View Docs button. 

The document will also be available via [http://manual.cytoscape.org/en/latest](http://manual.cytoscape.org/en/latest).

Note that the "stable" version of the manual is the build for the most recent release tag (e.g., "3.3") according to semantic versioning rules. This is the version that should be reference from the cytoscape.org web site's Documentation page. Note, too, that for testing, we can set a tag (e.g., "3.4") and have ReadTheDocs build from the tagged GitHub files. It will be available at http://manual.cytoscape.org/en/3.4 ... and as we refine the document, we can use GitHub to move the tag to the appropriate latest checkin. This is useful for testing with a candidate 3.4 that will eventually stop being re-tagged.

Note that many errors (e.g., missing chapter files) fail silently. It's always best to verify recent changes by viewing them in the built document.

## Future Plan

... add info here ...

## Process for Importation
The existing Cytoscape user manual was ported from Moin Moin to Markdown/ReadTheDocs according to a formula laid out by Kozo Nishida. The original port is contained in the "originals" directory and are not part of the current document build. For posterity, the initial instructions were:

1. Export http://wiki.cytoscape.org/Cytoscape_3/UserManual to a
docbook xml. (https://github.com/kozo2/cytoscape3-usermanual/blob/master/UserManual.xml)

2. Convert UserManual.xml to UserManual.md
(https://github.com/kozo2/cytoscape3-usermanual/blob/master/UserManual.md)
with ```pandoc -f docbook -t markdown -s UserManual.xml -o UserManual.md```

3. Separate UserManual.md per chapter manually.
(https://github.com/kozo2/cytoscape3-usermanual/tree/master/docs)

4. Find all pictures used by each chapter and put them into the Images directory. Resolve all picture references in the text by hand.

5. Build and deploy #4 with mkdocs and readthedocs.
 
Additionally:

1. Create a new project in ReadTheManual, and create a WebHook from GitHub to ReadTheDocs via http://docs.readthedocs.org/en/latest/webhooks.html

1. Note that text is processed by Sphinx, which is documented here: http://www.sphinx-doc.org/en/stable/contents.html
