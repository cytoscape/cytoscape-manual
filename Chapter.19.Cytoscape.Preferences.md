[Cytoscape Preferences](http://wiki.cytoscape.org/Cytoscape_3/UserManual/Cytoscape_3/UserManual/Preferences)
============================================================================================================

Managing Properties
-------------------

The Cytoscape properties editor, accessed via **Edit ? Preferences ?
Properties...**, is used to specify default properties. Any changes made
to these properties will be saved in .props files under the
`CytoscapeConfiguration` subdirectory of the user's home directory.

Cytoscape properties are configurable using the Add, Modify and Delete
buttons as seen below.

-   ![Preferences\_cy3.png](http://wiki.cytoscape.org//Cytoscape_3/UserManual/Preferences?action=AttachFile&do=get&target=Preferences_cy3.png)

App properties may also be edited in the same way as editing Cytoscape
properties. For example, to edit the properties of Linkout, select
'linkout' from the combobox of the Preferences Editor. Some apps may
store properties inside session files in addition to (or instead of)
storing them in the `CytoscapeConfiguration` directory.

-   ![Preferences\_linkout.png](http://wiki.cytoscape.org//Cytoscape_3/UserManual/Preferences?action=AttachFile&do=get&target=Preferences_linkout.png)

Managing Bookmarks
------------------

Cytoscape contains a pre-defined list of bookmarks, which point to
sample network files located on the Cytoscape web server. Users may add,
modify, and delete bookmarks through the Bookmark manager, accessed by
going to **Edit ? Preferences ? Bookmarks...**.

-   ![Preferences\_bookmarks.png](http://wiki.cytoscape.org//Cytoscape_3/UserManual/Preferences?action=AttachFile&do=get&target=Preferences_bookmarks.png)

There are currently several types of bookmarks (based on data
categories), including network and table. Network bookmarks are URLs
pointing to Cytoscape network files. These are normal networks that can
be loaded into Cytoscape. Table bookmarks are URLs pointing to data
table files.

Managing Proxy Servers
----------------------

You can define and configure a proxy server for Cytoscape by going to
**Edit ? Preferences ? Proxy Settings...**.

-   ![Preferences\_proxy.png](http://wiki.cytoscape.org//Cytoscape_3/UserManual/Preferences?action=AttachFile&do=get&target=Preferences_proxy.png)

After the proxy server is set, all network traffic related to loading a
network from URL will pass through the proxy server. Cytoscape apps use
this capability as well. The proxy settings are saved in
`cytoscape3.props`. Each time you click the OK button after making a
change to the proxy settings, an attempt is made to connect to a well
known site on the Internet (e.g., google.com) using your settings. For
both success and failure you are notified and for failure you are given
an opportunity to change your proxy settings.

If you no longer need to use a proxy to connect to the Internet, simply
set the Proxy type to "direct" and click the OK button.

Managing Group View
-------------------

The configuration of Cytoscape group view may also be edited through
**Edit ? Preferences ? Group Preferences...**.

-   ![Preferences\_groups.png](http://wiki.cytoscape.org//Cytoscape_3/UserManual/Preferences?action=AttachFile&do=get&target=Preferences_groups.png)
