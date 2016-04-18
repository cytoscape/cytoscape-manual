<a id="publish_your_data"> </a>
# Publish Your Data

<a id="publish_your_visualizations"> </a>
## Publish Your Visualizations

When you finish your data analysis and visualization, you need to
publish your data to share the results. Cytoscape has several options to
do it, with most options suitable for Cytoscape users and other options
suitable for programmers wanting to create unusual or complex network
viewers. They're further explained below.

-   A session file

-   A static image

-   An interactive web application

    -   [CyNetShare](http://idekerlab.github.io/cy-net-share/)

    -   Full web application

    -   Simple network view (for web application developers)

<a id="as_a_session_file"> </a>
### As a Session File

The easiest way to share your results with others is simply saving
everything as a session file (which is a zipped session archive). You
can save your current session by clicking ***Save Session*** icon. You
can save to a thumb drive, a shared file system, or even a cloud drive
directory such as Dropbox -- if you save to a shared drive, beware not
to have two people work on the same session file with Cytoscape at the
same time, as unpredictable results may occur.

<a id="as_a_static_image"> </a>
### As a Static Image

Cytoscape can generate publication-quality images from network views. By
selecting ***File | Export | Network View as Graphics...***, you can
export the current network view into the following formats:

-   JPG

-   PNG

-   PS (Post Script)

-   SVG

-   PDF

We recommend using **PDF** for publications because it is a standard
vector graphics format, and it is easy to edit in other applications
such as Adobe Illustrator.

<a id="known_issues"> </a>
#### Known Issues

For PDF export, there is an option to ***Export Texts as Fonts***.
**This option does not work for two-byte characters such as Chinese or
Japanese**. To avoid corrupted texts in the exported images, please
uncheck this option when you publish networks including those
non-English characters.

<a id="as_an_interactive_web_application_new_in_3.2.0"> </a>
### As an Interactive Web Application (New in 3.2.0)

The Web is an excellent platform for data sharing and collaboration, and
Cytoscape provides a number of ways to publish your network on the web,
with each choice representing tradeoffs between ease, simplicity, and
customization options. All solutions leverage the cytoscape.js drawing
library, and so enable not only viewing but also Cytoscape-style
interactive browsing of networks and attributes.

The simplest choice is
[CyNetShare](http://cytoscape-working-copy.readthedocs.org/en/latest/Chapter_22_Publish_Your_Data.html#sharing-via-cynetshare),
where you save your network (and optionally a style) on a public file
system, then interactively view the network in a browser. Like Google
Maps, you can generate and publish a URL that allows collaborators to
also view your network.

Alternatively, Cytoscape can generate an entire web site showing a
single page containing the viewer with your network pre-loaded. You can
load this directly onto your own web server to become part of your web
site.

Finally, Cytoscape can generate the skeleton of a web site for further
customization by
[JavaScript](https://en.wikipedia.org/wiki/JavaScript)
programmers.

These features are available as Export menu items under the File menu,
and are described in sections below.

For example, here is a network in Cytoscape:

![WebExportOriginal\_v3\_3\_3.png](_static/images/Publish/WebExportOriginal_v3_3_3.png)

Here is the same network as an interactive web visualization:

![web\_export\_fullexport.png](_static/images/Publish/web_export_fullexport.png)

Note that web browsers can render small networks (e.g., 1000 nodes)
quickly and effectively, but attempting to render large ones (e.g., 5000
nodes) will take a very long time.

**A word about exporting styles styles to interactive web
applications:** Our web applications are based on the cytoscape.js
display library, which renders a subset of Cytoscape styles. For more
information, see the **Export Styles to Cytoscape.js** section below.

<a id="sharing_via_cynetshare"> </a>
#### Sharing via CyNetShare

[CyNetShare](http://idekerlab.github.io/cy-net-share/)
is a browser-based web application that renders JSON-formatted networks
and attributes saved in public directories. Optionally, you can specify
visual styles that the web application will use to draw your network as
it appears in Cytoscape.
[CyNetShare](http://idekerlab.github.io/cy-net-share/)
is similar to Google Maps in that once you have loaded your network and
have tweaked its appearance to suit, you can have
[CyNetShare](http://idekerlab.github.io/cy-net-share/)
generate a new URL that you can e-mail or post as a link on your own web
site. That URL will bring up
[CyNetShare](http://idekerlab.github.io/cy-net-share/)
preloaded with your network for anyone to see.

To use
[CyNetShare](http://idekerlab.github.io/cy-net-share/):

1.  Select ***File | Export | Network and View...*** to export your
    network to a public directory. Choose the *Cytoscape.js
    JSON (\*.cyjs)* export file format.

2.  Optionally, select ***File | Export | Style...*** to export your
    style settings. Choose the *Style for cytoscape.js (\*.json)* export
    file format.

3.  Use your public directory system to determine direct URLs for the
    files you exported.

4.  Start [CyNetShare](http://idekerlab.github.io/cy-net-share/)

5.  Enter the network's URL as the Graph URL.

6.  Optionally, enter the style's URL.

7.  Click the ***Visualize*** button.

The
[CyNetShare](http://idekerlab.github.io/cy-net-share/)
User Guide is provided on the
[CyNetShare](http://idekerlab.github.io/cy-net-share/)
web page:

-   [CyNetShare](http://idekerlab.github.io/cy-net-share/)

Note that if you specify a style URL, the style is added to the list of
styles available in
[CyNetShare](http://idekerlab.github.io/cy-net-share/)'s
Visual Style dropdown, and you can apply the style by selecting it in
the list.

Note that the mechanics of generating a URL for a file in a public
directory system is a fast moving topic. Until recently, systems like
Dropbox (and others) allowed users to create a URL that resolved
directly to a file -- a "direct" URL would be appropriate for use with
[CyNetShare](http://idekerlab.github.io/cy-net-share/).
As of this writing, some public directory systems (e.g., Dropbox)
generate "shareable" URLs instead, which resolve to a web page that
allows file download -- a "shareable" URL makes
[CyNetShare](http://idekerlab.github.io/cy-net-share/)
hang. Systems that offer "shareable" URLs may offer "direct" URLs as
part of their premium (or Pro) package. To tell if your public directory
system generates a "direct" URL, have it generate a URL for a file, then
paste the URL into the address field of a browser and observe whether
the browser displays the file itself (good!) or a download page for the
file (bad!).

A simple strategy for always getting a "direct" URL is to store your
file in a public directory served up by a web server, if you have access
to one -- a URL served by a web server might appear as:
[http://myserver.com/~mypublicdir/netstyle.json](http://myserver.com/~mypublicdir/netstyle.json).

Alternately, you can use [Gist](http://gist.github.com/) to create a
shareable document having a "direct" URL. To try this:

1.  Use Cytoscape to generate your network as a .cyjs file on your local
    disk

2.  Use an editor to open the file and copy its contents to the
    clipboard

3.  Use a web browser to surf to [Gist](http://gist.github.com/)

4.  Paste the contents into a Gist document

5.  Select ***Create public Gist***

6.  Select ***Raw*** to place the "direct" URL into your browser's
    address field

7.  Use that URL with
    [CyNetShare](http://idekerlab.github.io/cy-net-share/)

<a id="generating_a_full_web_application"> </a>
#### Generating a Full Web Application

The full page export option is designed for users who want to publish
their network as a complete [single-page
application](http://en.wikipedia.org/wiki/Single-page_application).
Cytoscape creates a zip archive containing a complete
[JavaScript](https://en.wikipedia.org/wiki/JavaScript)-based
web application that works as a basic viewer (like
[CyNetShare](http://idekerlab.github.io/cy-net-share/))
for Cytoscape-generated network visualizations. You can unzip the
archive onto a web server (or your PC) and view the network via a web
browser on PCs and tablets.

![web\_export\_full.png](_static/images/Publish/web_export_full.png)

To generate an entire web page as a zip archive, select ***File | Export
| Network View(s) as Web Page ...***.

To view the web page, unzip the archive into a folder on your PC or web
server. The folder will contain an ***index.html*** file, the network
data, and other files. You can open the ***index.html*** file in your
browser (usually from your browser's ***File | Open*** menu item.)

Depending on your browser's security settings, you may not be able to
open the ***index.html*** file directly if it is stored on your PC --
you may need to start a web server on your PC. An easy way to set up a
local web server is by running the Python simple HTTP server. If you
have Python installed on your machine, just go into the web archive
folder and type:

    python -m SimpleHTTPServer 8000

and use your browser to open:

    http://localhost:8000/

Testing the archive on your PC will serve as an easy test of the web
page, but to publish it to collaborators, you should unzip your archive
onto a web server.

Here is an example exported file from Cytoscape:

-   [Example full export deployed to web
    server](http://chianti.ucsd.edu/~kono/webapp/cytoscape-export-full/)

-   [Archive file](http://cl.ly/XjMs/cytoscape_full_export.zip)

![web\_export\_full2.png](_static/images/Publish/web_export_full2.png)

Note that because Cytoscape uses the latest HTML5-based web
technologies, it cannot support older or non-conformant web browsers
such as Internet Explorer. We strongly recommend using the latest
version of modern web browsers such as Google Chrome, Mozilla Firefox,
or Apple Safari.

<a id="generating_a_simple_network_view_for_web_application_developers"> </a>
#### Generating a Simple Network View (For Web Application Developers)

The Simple Network View export option is designed for users who want to
publish their data as a complete [single-page
application](http://en.wikipedia.org/wiki/Single-page_application), but
are interested in customizing the web viewer application themselves.
Cytoscape creates a zip archive containing a partial
[JavaScript](https://en.wikipedia.org/wiki/JavaScript)-based
web application based on the cytoscape.js library and including simple
"boilerplate" code and the current network view. The user can create a
custom viewer by customizing this code.

![web\_export\_simple.png](_static/images/Publish/web_export_simple.png)

To generate an entire web page as a zip archive, select ***File | Export
| Network View(s) as Web Page ...***, and choose the *Simple viewer for
current network only* format.

For instructions on testing the customized web application, see
*Generating a Full Web Application* above.

<a id="customize_export_template_for_web_application_developers"> </a>
#### Customize Export Template (For Web Application Developers)

The code generated by Cytoscape for the Full Web Application and the
Simple Network View web applications is minimalistic. While you can
directly modify this code yourself to create your own page design or add
new features, the modifications will apply to a single exported network.
If you are a web application developer, you can change the application
code generated for **all** exports by editing HTML5 template code
resource files in your ***\~/CytoscapeConfiguration/web*** directory:

![web\_folder.png](_static/images/Publish/web_folder.png)

In this folder, you can find ***full*** and ***simple*** sub directories
corresponding to Full Web Application and the Simple Network View
described above.

##### Requirements

To build these project, you need the following tools installed:

-   Node.js

-   gulp

-   grunt

##### Full Export Template

This is an AngularJS based web application built with grunt (at least
for now -- we have plans to migrate to gulp). Source code and more
documentations are available here:

\* [https://github.com/idekerlab/cyjs-full-export](https://github.com/idekerlab/cyjs-full-export)

To build the project into *dist* directory, type:

    grunt

##### Simple Export Template

This template is generated by a simple [gulp](http://gulpjs.com/)
project. The source code is available here:

-   [https://github.com/idekerlab/cyjs-export-simple](https://github.com/idekerlab/cyjs-export-simple)

To build the project into *dist* directory, type:

    gulp

##### Use Your Custom Templates for Export

Once you have your own builds, you can deploy your templates by
replacing the contents of *full* and *simple* with your own builds.
