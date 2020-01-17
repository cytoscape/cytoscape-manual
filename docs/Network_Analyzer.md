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

![Analyzer.png](_static/images/Network_Analyzer/Analyzer.png)

Analyzer will run different statistics depending on whether the network is directed or undirected.  The app will guess which type of network it is based on the definition of a target arrow style, but since this is not 

When results are calculated, they will appear in the **Results Panel**.

![AnalyzerResults.png](_static/images/Network_Analyzer/AnalyzerResults.png)

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

### Analyze Subset of Nodes

Prior versions of this tool offered the option of analyzing all nodes or only a selected subset.   This is no longer supported directly in the program.  Instead, if you want to analyzer a subnetwork, you must first use the command **File → New Network → From Selected Nodes, All Edges** to create the desired subnetwork.
<a id="plot_parameters"> </a>
### Plot Parameters

Once the Analyzer is run, several additional columns are added to the Node Table (and EdgeBetweenness is added to the Edge Table).  To plot any of these new columns, right-click on the column header and select **Plot Histogram...** for a single parameter distribution, or **Plot Scatter...** for a bivariate plot of the data.  Within either of these charts it is possible to select a section of the data, and select the nodes (edges) in the main graph window corresponding to the region selected on the chart.
<a id="networkanalyzer_settings"> </a>

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
