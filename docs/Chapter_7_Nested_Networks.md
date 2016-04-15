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
    Format](http://wiki.cytoscape.org/Cytoscape_3/UserManual/Cytoscape_3/UserManual/Network_Formats#nnf)**).

-   By manually constructing networks and assigning nested networks to
    individual nodes through the right-click node context menu. (See
    **[Nested Network Node Context
    Menu](http://wiki.cytoscape.org/Cytoscape_3/UserManual/Cytoscape_3/UserManual/Navigation_Layout#NestedNetwork)**).

<a id="visualization_of_nested_networks"> </a>	
## Visualization of Nested Networks

Nodes containing nested networks that are zoomed in sufficiently display
an image for the nested network. If no current network view exists for
the nested network the image will be a default icon, otherwise it will
be a low-resolution rendering of the nested network's current layout.

![Nested Network
visualization](_static/images/Nested_Networks/NestedNetwork.png)

![NestedNetwork2.png](_static/images/Nested_Networks/NestedNetwork2.png)

Programmatically Manipulating Nested Networks
---------------------------------------------

The giny.model.node interface defines two methods:

```
   public void setNestedNetwork(final
    [GraphPerspective](http://wiki.cytoscape.org/Cytoscape_3/UserManual/GraphPerspective#)
    graphPerspective); This will assign a "network"
    ([GraphPerspective](http://wiki.cytoscape.org/Cytoscape_3/UserManual/GraphPerspective#))
    to a Node or replace the assigned network at a node if there was a
    prior existing one. In order to remove a nested network, please pass
    null to this method.

    public
    [GraphPerspective](http://wiki.cytoscape.org/Cytoscape_3/UserManual/GraphPerspective#)
    getNestedNetwork(); If a Node has an associated nested network, it
    will be returned by this method. If no associated nested network
    exists, null will be returned instead.
```