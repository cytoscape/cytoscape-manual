<a id="networkanalyzer"> </a>
# Analyzer

Analyzer computes a comprehensive set of topological parameters
for undirected and directed networks, including:

-   Number of nodes, edges and connected components.

-   Network diameter, radius and clustering coefficient, as well as the
    characteristic path length.

-   Charts for topological coefficients, betweenness, and closeness.

-   Distributions of degrees, neighborhood connectiveness, average
    clustering coefficients, shortest path lengths, number of shared
    neighbors and stress centrality.


<a id="network_analysis"> </a>
## Network Analysis

<a id="analyze_network"> </a>
### Analyze Network

To run Analyzer, select **Tools → Analyze Network**.

![NetworkAnalyzer.png](_static/images/Network_Analyzer/NetworkAnalyzer.png)

Analyzer will run different statistics depending on whether the network is directed or undirected.  The app will guess which type of network it is based on the definition of a target arrow style, but since this is not 

When results are calculated, they will appear in the **Results Panel**.

![NetworkAnalyzerResults.png](_static/images/Network_Analyzer/NetworkAnalyzerResults.png)

The results have multiple tabs. Details on the network parameters can be
found
**[here](http://med.bioinf.mpi-inf.mpg.de/netanalyzer/help/2.7/index.html#complex)**.

-   **Simple Parameters**

-   **Node Degree Distribution**

-   **Avg. Clustering Coefficient Distribution**

-   **Topological Coefficients**

-   **Shortest Path Distribution**

-   **Shared Neighbors Distribution**

-   **Neighborhood Connectivity Distribution**

-   **Betweenness Centrality**

-   **Closeness Centrality**

-   **Stress Centrality Distribution**

<a id="analyze_subset_of_nodes"> </a>
### Analyze Subset of Nodes

An exhaustive topological analysis of very large networks can be a time
consuming task. The computation of local parameters for the nodes is
significantly faster than the computation of global (path-related)
parameters. Examples of local parameters are node degree, neighborhood
connectivity, topological and clustering coefficients. Betweenness and
closeness centralities, as well as stress, are global parameters.

Analyzer provides the **Analyze Subset of Nodes** option for computing local
parameters for a subset of nodes. If one or more nodes in the network
are selected before starting an analysis, only the sub-network induced
by the selected nodes is analyzed. Moreover, only local parameters are
computed. Shared neighbors distribution and shortest path lengths
distribution, among others, are not displayed in the results.

<a id="plot_parameters"> </a>
### Plot Parameters

Once the Analyzer is run, several additional columns are added to the Node Table (and EdgeBetweenness is added to the Edge Table).  To plot any of these new columns, right-click on the column header and select **Plot Histogram...** for a single parameter distribution, or **Plot Scatter...** for a bivariate plot of the data.  Within either of these charts it is possible to select a section of the data, and select the nodes (edges) in the main graph window corresponding to the region selected on the chart.
<a id="networkanalyzer_settings"> </a>
### Analyzer Settings

The following settings can be configured by the user:

-   **Store node / edge parameters in node / edge table**: For every
    node in a network, NetworkAnalyzer computes its degree (in- and
    out-degrees for directed networks), its clustering coefficient, the
    number of self-loops, and a variety of other parameters.
    NetworkAnalyzer also computes edge betweenness for each edge in
    the network. If the respective options are enabled, NetworkAnalyzer
    can stores the computed values as columns of the corresponding nodes
    and edges. This enables the users to use the values in Styles or to
    select nodes or edges based on the values. A complete list of the
    computed node and edge columns is available
    **[here](http://med.bioinf.mpi-inf.mpg.de/netanalyzer/help/2.7/index.html#attributes)**.

-   **Use expandable dialog interface for the display of network
    statistics**: If this option is enabled, analysis results are
    presented in a window in which all charts are placed below each
    other in expandable boxes. If this option is disabled, analysis
    results are presented in a window that contains tabs for the group
    of simple parameters and for every complex parameter (default).
    Users who wish to simultaneously view two or more complex parameters
    of one network, should enable this option.


-   **Location of the help documents**: URL of the original help web
    page for Analyzer. This also enables the local download and
    storage of this help page.

![NetworkAnalyzer\_ConnectedComponents.png](_static/images/Network_Analyzer/NetworkAnalyzer_ConnectedComponents.png)

<a id="networkanalyzerdemo"> </a>
## NetworkAnalyzerDemo: Computation and Visualization of Topological Parameters and Centrality Measures for Biological Networks
**Yassen Assenov<sup>1</sup>, Nadezhda Doncheva<sup>1</sup>, Thomas Lengauer<sup>1</sup>, and Mario Albrecht<sup>1</sup>**

*1 Department of Computational Biology and Applied Algorithmics, Max Planck Institute for Informatics, Campus E1.4, 66123 Saarbrücken, Germany*

NetworkAnalyzer is a versatile and highly customizable Cytoscape plugin that requires no expert knowledge 
in graph theory from the user. It computes and displays a comprehensive set of topological parameters and 
centrality measures for undirected and directed networks, which includes the number of nodes, edges, and 
connected components, the network diameter, radius, density, centralization, heterogeneity, clustering 
coefficient, and the characteristic path length. In addition, NetworkAnalyzer shows charts of the distribution 
of node degrees, neighborhood connectivities, average clustering coefficients, and shortest path lengths. 
NetworkAnalyzer also contains extra functionality, for instance, for constructing the intersection or union of two networks.

The NetworkAnalyzer plugin and a comprehensive online documentation with a tutorial are available at [http://med.bioinf.mpi-inf.mpg.de/networkanalyzer/](http://med.bioinf.mpi-inf.mpg.de/networkanalyzer/).

**Data keywords**: network, graph, topology

**Cytoscape keywords**: Network Analysis
