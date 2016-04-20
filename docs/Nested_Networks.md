<a id="nested_networks"> </a>
# Nested Networks

Cytoscape has the ability to associate a **Nested Network** with any
node. A nested network is any other network currently defined in
Cytoscape. This capability allows for creation of network hierarchies as
well as circular relationships. For example, various module-finding
plugins make use of nested networks in the overview network that they
generate. There each node representing a module contains a nested
network.

<a id="creating_nested_networks"> </a>
## Creating Nested Networks

There are currently two ways in which a user can create nested networks.

-   By importing a Nested Network Format (NNF) file. (See: **[NNF
    Network
    Format](http://cytoscape-working-copy.readthedocs.org/en/latest/Supported_Network_File_Formats.html#nnf)**).
	
-   By manually constructing networks and assigning nested networks to
    individual nodes through the right-click node context menu. (See
    **[Nested Network Node Context
    Menu](http://cytoscape-working-copy.readthedocs.org/en/latest/Navigation_and_Layout.html#nested-network-node-context-menu)**).

<a id="visualization_of_nested_networks"> </a>	
## Visualization of Nested Networks

Nodes containing nested networks that are zoomed in sufficiently display
an image for the nested network. If no current network view exists for
the nested network the image will be a default icon, otherwise it will
be a low-resolution rendering of the nested network's current layout.

![NestedNetwork2.png](_static/images/Nested_Networks/NestedNetwork2.png)
