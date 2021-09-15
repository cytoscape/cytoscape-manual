<a id="merge"> </a>
# Merge

Cytoscape allows for merging of both network and table data, through
**Tools → Merge**.

<a id="merge_networks"> </a>
## Merge Networks

The **Advanced Network Merge** interface is available from **Tools →
Merge → Networks...** and allows for merging of two or more networks.

![](_static/images/Merge/AdvancedNetworkMerge.png)

<a id="basic_operations"> </a>
### Basic Operations

-   Select either **Union**, **Intersection**
    or **Difference**.

-   Networks available for merge are listed under **Networks to merge**.
    Select a network from the list and click the right arrow to transfer
    the network to **Selected networks**. Click **Merge** to continue.
    The merged network will be displayed as a separate network.

<a id="advanced_options"> </a>
### Advanced Options

The **Advanced Network Merge** interface includes an expandable
**Advanced Network Merge** panel, where you can specify the details of
how to merge the networks. The options available here are:

-   **Matching Columns**: This specifies the network columns that should
    be used for merging. Typically, the **name** column or some other
    column containing identifier information is used here.

-   **How to merge columns**: A table lets the user specify for each of
    the individual network columns, what the corresponding column in the
    merged network should be named and its data type.

![](_static/images/Merge/AdvancedNetworkMergeOptions.png)
