<a id="finding_and_filtering_nodes_and_edges"> </a>
# Finding and Filtering Nodes and Edges

<a id="search_bar"> </a>
## Search Bar

You can search for nodes and edges by column value directly through
Cytoscape's tool bar. For example, to select nodes or edges with a
column value that starts with "STE", type `ste*` in the search bar. The
search is case-insensitive. The `*` is a wildcard character that matches
zero or more characters, while `?` matches exactly one character. So
`ste?` would match "STE2" but would not match "STE12". Searching for
`ste*` would match both.

![searchbar3.png](_static/images/Filters/searchbar3.png)

To search a specific column, you can prefix your search term with the
column name followed by a `:`. For example, to select nodes and edges
that have a "COMMON" column value that starts with "STE", use
`common:ste*`. If you don't specify a particular column, all columns
will be searched.

Columns with names that contain spaces, quotes, or characters other than
letters and numbers currently do not work when searching a specific
column. This will be fixed in a future release.

To search for column values that contain special characters you need to
escape those characters using a "\\". For example, to search for
"GO:1232", use the query `GO\:1232`. The complete list of special
characters is:

    + - & | ! ( ) { } [ ] ^ " ~ * ? : \

**Note:** Escaping characters only works when searching all columns. It
currently does not work for column-specific searching. This will be
fixed in a future release.

<a id="filters"> </a>
## Filters

The **Filter** tab in the **Control Panel** can be used to create selection
expressions for selecting nodes and edges.

![select-panel2.png](_static/images/Filters/select-panel2.png)

There are two tabs: 
1. On the **Filter** tab are *narrowing* filters, which can be combined into a tree. 
2. On the **Chain** tab are *chainable* transformers, which can be combined in a linear chain.

<a id="narrowing_filters"> </a>
### Narrowing Filters

Narrowing filters are applied to all the nodes and edges in the network, and are used to
select a subset of the nodes and edges based on user-specified
constraints. For example, you can find edges with a weight between 0 and
5.5, or nodes with degree less than 3 (connecting to 3 or less edges). A filter can contain an arbitrary
number of sub-filters.

To add a filter click on the "+" button. To delete a filter (and all its
sub-filters) click the "x" button. To move a filter grab the handle
![filterhandle.png](_static/images/Filters/filterhandle.png)
with the mouse and drag and drop the filter on its intended destination.
Dropping a filter on top of another filter will group the filters into a
composite filter.

<a id="interactive_filter_application_mode"> </a>
#### Interactive Filter Application Mode

Due to the nature of narrowing filters, Cytoscape can apply them to a
network efficiently and interactively. Some filters even provide slider
controls to quickly explore different thresholds. This is the default
behavior on smaller networks. For larger networks, Cytoscape
automatically disables this interactivity. You can override this by
manually checking the **Apply when filter changes** box above the **Apply**
button:

![apply-automatically2.png](_static/images/Filters/apply-automatically2.png)

The **Apply** button will re-apply the active filter. On the opposite side of the progress
bar is the cancel button, which will let you interrupt a long-running filter.

You also have the option to use the filter to show only the selected nodes by checking 
the **show** button. The **select** button is checked by default and simply selects nodes
that pass the filter.

Cytoscape comes packaged with the following narrowing filters:

<a id="column_filter"> </a>
#### Column Filter

Column filters will match nodes or edges that have particular column
values. Depending on the column data type a variety of matching options are provided:

- **Numeric Columns**
  - A slider is shown that represents the minimum and maximum values in the column.
    Drag the two handles to select a range of values.
  - The range values may also be entered manually.
  - Options:
    - **is**: Selects values that are inside the range.
    - **is not**: Selects values that are outside the range.

    ![column-numeric.png](_static/images/Filters/column-numeric.png)


- **String Columns**
  - The text entered in the text box will be matched against the column values 
    depending on the following options.
  - Options:
    - **contains**: Selects values that contain the text.
    - **doesn't contain**: Selects values that do not contain the text.
    - **is**: Selects values that match the text exactly (case-insensitive).
    - **is not**: Selects values that do not match the text exactly (case-insensitive).
    - **regex**: Selects values that match a regular expression using [Java regular expression
      syntax](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html). This allows for much more
      sophisticated matching than is provided by the above options.
  - By default string matching is case insensitive. Case sensitive matching
    requires the use of a regular expression that starts with "(?-i)". For
    example to match the text "ABC" in a case sensitive way use the
    following regular expression: "(?-i)ABC".

    ![column-string.png](_static/images/Filters/column-string.png)


- **Boolean Columns**
  - Boolean colums can only contain three values: true, false or blank.
  - Options:
    - **true**: Selects values that are true.
    - **false**: Selects values that are false.

    ![column-boolean.png](_static/images/Filters/column-boolean.png)


- **List Columns**
  - Column filters for list columns are similar to their non-list counterparts, however
    there is one additional option...
    - **any element**: Matches if any value in the list matches the filter.
    - **each element**: Matches only if all of the values in the list match the filter.

    ![column-list.png](_static/images/Filters/column-list.png)


<a id="degree_filter"> </a>
#### Degree Filter

The degree filter matches nodes with a degree that falls within the
given minimum and maximum values, inclusive. You can choose whether the
filter operates on the in-degree, out-degree or overall (in + out)
degree.

<a id="topology_filter"> </a>
#### Topology Filter

The topology filter matches nodes having a certain number of neighbors
which are within a fixed distance away, and which match a sub-filter.
The thresholds for the neighborhood size and distance can be set
independently, and the sub-filter is applied to each such neighbor node.

The topology filter will successfully match a node if the sub-filter
matches against the required number of neighbor nodes.

<a id="grouping_and_organizing_filters"> </a>
#### Grouping and Organizing Filters

By default, nodes and edges need to satisfy the constraints of all your
filters. You can change this so that instead, only the constraints of at
least one filter needs to be met in order to match a node or edge. This
behavior is controlled by the **Match all/any** drop-down box. This
appears once your filter has more than one sub-filter. For example,
suppose you wanted to match nodes with column **COMMON** containing `ste`
or `cdc`, but you only want nodes with degree 5 or more, you'd first
construct a filter that looks like this:

![group1.png](_static/images/Filters/group1.png)

This filter will match nodes where **COMMON** contains `ste` **and**
`cdc`. To change this to a logical **or** operation, drag either of the
column filters by its handle
![filterhandle.png](_static/images/Filters/filterhandle.png)
onto the other column filter to create a new group. Now change the
group's matching behavior to **Match any**:

![group2.png](_static/images/Filters/group2.png)

You can also reorder filters by dropping them in-between existing
filters.

<a id="chainable_filters"> </a>
### Chainable Transformers

The input to a chainable transformer is a set of nodes and edges, either the nodes and edges
that are currently selected in the network, or the output of a narrowing filter. Chainable
transformers can filter out nodes/edges, or include more nodes/edges. For example a chainable
transformer can add nodes that are neighbours of the nodes in the input. 

Chainable filters are combined in an ordered list. The nodes and edges
in the output of a transformer become the input of the next transformer in the
chain. The first transformer in the chain gets its input from the current
selection or from a filter on the **Filter** tab. The output of the last
transformer becomes the new selection.

You can specify the input to the first transformer in the chain by selecting
a **Start with**, where **Current selection** refers to the nodes and
edges currently selected. You can also choose a narrowing filter, which
produces a different set of selected nodes and edges.

![chain-filter1.png](_static/images/Filters/chain-filter1.png)

Chainable transformer can be reordered by dragging one by the handle and
dropping it between existing transformer.

Cytoscape currently bundles the following chainable transformers:

<a id="edge_interaction_transformer"> </a>
#### Edge Interaction Transformer

This transformer will go through all the input edges and selectively add
their source nodes, target nodes, or both, to the output. This is useful
for adding nodes that are connected to edges that match a particular
filter.

Output options:

-   Add (default): Automatically includes all input nodes and edges in
    the output, and adds source or target nodes from input edges to
    the output.

-   Replace with: Does not automatically include input nodes and edges
    in the output. Only outputs nodes that match the filter.

A sub-filter may be added as well. When a sub-filter is present the
source/target nodes must match the filter to be included in the output.

<a id="node_adjacency_transformer"> </a>
#### Node Adjacency Transformer

This transformer is used to add nodes and edges that are adjacent to the
input nodes. A sub-filter may be specified as well.

Note that pressing the **Apply** button repeatedly may cause the
selection to continuously expand. This allows adjacent nodes that are at
greater distances to be added.

Output options:

-   Add (default): Automatically includes all input nodes and edges in
    the output, and adds selected adjacent nodes and edges.

-   Replace with: Only outputs the adjacent nodes/edges.

Select options:

-   Adjacent nodes: Output nodes that are adjacent to the input nodes.

-   Adjacent edges: Output edges that are adjacent (incident) to the
    input nodes.

-   Adjacent nodes and edges (default): Output both nodes and edges that
    are adjacent to the input nodes.

Edge direction options. (Hidden by default, click the small arrow icon
to reveal.):

-   Incoming: Only include adjacent nodes/edges when the adjacent edge
    is incoming.

-   Outgoing: Only include adjacent nodes/edges when the adjacent edge
    is outgoing.

-   Incoming and Outgoing (default): Ignore the directionality of
    adjacent edges.

Sub-filter options. (Available when a sub-filter has been added.):

-   Adjacent nodes (default): The sub-filter is only applied to
    adjacent nodes. (Edges to the adjacent nodes are still included in
    the output.)

-   Adjacent edges: The sub-filter is only applied to adjacent edges.
    (Nodes connected to the adjacent edges are still included in
    the output.)

-   Adjacent nodes and edges: Both the adjacent edge and its connected
    node must match the filter. Note that for a filter to match an edge
    and a node at the same time it should be a compound filter that is
    set to "Match any (OR)".

<a id="working_with_narrowing_and_chainable_filters"> </a>
### Working with Narrowing and Chainable Filters

The name of active filter appears in the drop-down box at the top of
**Select** panel. Beside this is the options button which will allow you
to rename, remove or export the active filter. It also lets you create a
new filter, or import filters.

![select-panel-options2.png](_static/images/Filters/select-panel-options2.png)


<a id="diffusion"> </a>
## Diffusion

Cytoscape's Diffusion algorithm attempts to use a set of nodes and an entire interaction network to find the nodes most relevant to the original set.
Conceptually, Diffusion applies heat to each node in the set, and lets the heat flow through connecting edges to adjacent nodes. 
It then produces a list of nodes ranked by the heat they accumulated. A node with many connections will tend to have a higher
ranking, and an isolated node will tend to have low rank (and thus be excluded from the resulting node set).

By default, Diffusion uses the set of selected nodes as the heat sources, with each node having the same initial heat. At the end of a Diffusion, Cytoscape leaves the top 90th percentile of hot nodes selected. It allows you to use the Results panel to select a higher or 
lower percentile dynamically. It also stores the node's initial heat as a node attribute in the "diffusion_input" column, and returns the heat and ranking values in the "diffusion_output_heat" and "diffusion_output_rank" columns.

An advanced Diffusion option allows you to specify initial heat values for each node via its "diffusion_input" attribute.

This figure shows the result of selecting the PHO4, GCR1 and ICL1 genes (via the [search bar](Finding_and_Filtering_Nodes_and_Edges.html#search_bar)) and performing a Diffusion by either selecting **Tools → Diffuse → Selected Nodes** or right-clicking to **Diffuse → Selected Nodes**. Diffusion calculated the heat ranking of all 331 nodes in the network, and then selected the top 33. 

![after_diffusion.png](_static/images/Filters/after_diffusion.png)

To select more than 33 nodes, move the **Node Rank** slider in the Diffusion Output Results Panel to the right or enter a number greater than 33 in the **Current Rank** field. You can also select nodes using a heat value cutoff by using the **Range Column** to select a column containing heat values. Finally, you can use the **Visual Style** chooser and **Create** button to extract the selected nodes into a new network.

You can execute Diffusion multiple times on a network, thereby creating multiple heat, output_heat and output_rank columns.

<a id="the_select_menu"> </a>
## The Select Menu

The **Select → Nodes** and **Select → Edges** menus provide several
mechanisms for selecting nodes and edges. Most options are fairly
straightforward; however, some need extra explanation.

**Select → Nodes → From ID List File...** selects nodes based on node
identifiers found in a specified file. The file format is simply one
node id per line:

    Node1
    Node2
    Node3
    ...
