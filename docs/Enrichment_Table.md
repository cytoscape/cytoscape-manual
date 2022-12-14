<a id="enrichmenttable"> </a>
# Enrichment Table

The Enrichment Table App provides the functionality of functional enrichment analysis for any network loaded into Cytoscape using [g:Profiler's web service](https://biit.cs.ut.ee/gprofiler/gost).

The app creates a new table called the `Enrichment Table` which provides an icon to perform enrichment, as well icons for settings and filters. The app also adds a menu option under ***Tools*** > ***Enrichment Table*** > ***Perform Gene Enrichment***.

By default, the enrichment analysis is performed on all nodes of the current network using the genome as background. If nodes are selected, then enrichment is performed against just those nodes using the complete network as the background. You can arrange for any background you like by loading all background nodes into Cytoscape and selecting a subset for enrichment analysis.

The enrichment analysis is supported in automation use cases as well. The basic command syntax is `enrichment analysis`.  You can optionally choose the organism associated with the query genes with the `organism` parameter. You can also optionally select the node table column containing the gene symbols with the `geneID` parameter. All parameters are listed
[here](http://localhost:1234/v1/swaggerUI/swagger-ui/index.html?url=http%3A%2F%2Flocalhost%3A1234%2Fv1%2Fcommands%2Fswagger.json#!/enrichment/enrichment_analysis).

<a id="prediction"> </a>
## Organism and Gene ID

Enrichment process requires two mandatory parameters:

- Organism: Organism associated with the query genes
- Gene ID: Node table column containing the gene symbols

![](_static/images/Enrichment_Table/species.png)

Both these parameters are predicted by enrichment table app if enough information is available.

- The application on startup predicts the possible ***organism*** by processing the data from the network in columns [`species`,`organism`,`IntAct::species`]
- The application on startup predicts the ***gene id*** column in following ways:
   1. Retrieves `NODE_LABLE` from style for any generic network
   2. Selects `display name` for `stringapp` networks
 
**If you want to manully set organism and gene ID or the prediction is incorrect, you can change options in the network specific enrichment panel settings which can be accessed by clicking the gear icon in the enrichment table panel**.
<a id="process"> </a>
## Running Enrichment Process
There are three ways you can perform enrichment analysis:

- Use the menu option under ***Tools*** > ***Enrichment Table*** > ***Perform Gene Enrichment***.
- In the command line, enter `enrichment analysis`, and click enter.
- Click the Perform Gene Enrichment button with icon of reload in the enrichment table panel.

![](_static/images/Enrichment_Table/run.png)


Now you get the table containing enrichment results. The results are sorted according to the p-value in a increasing order by default.

<a id="filter"> </a>
## Filter Results
There are couple of parameters based on which you can filter the table by categories and evidence code:

- Click the Filter Enrichment Table button with filter icon to access the filters.
- Select Gene Ontology Biological Process in the categories. Click ok. You will see a filtered table, along with number of current rows a label above table.
- Open to filter panel again and check remove redundant terms. Click ok to see terms consisting of both filters applied.

![](_static/images/Enrichment_Table/filter.png)

<a id="ring"> </a>
## Ring Charts
Ring charts provide ability visualise top-5 terms in the network using split-charts. You can change the number of terms and type of chart in chart setting panel.

- Click Draw Chart to create chart with default setting and split charts will appear in the network.
- To remove the chart, click on Reset Charts to remove charts.
- To change charts setting, go to Visit the network specific chart settings.

![](_static/images/Enrichment_Table/ring.png)


<a id="term"> </a>
## Term Selection
Enrichment Table shows results based on nodes selected in the network. If no nodes are selected, all terms are shown in the table. On multiple node selection, terms consisting of all the selected nodes are shown. Similarly, to visualize one or more enrichment term, select the rows in the table and the corresponding nodes will get highlighted.

<a id="optional"> </a>
## Optional Settings
In addition to Organism and Gene ID column, there are other parameters that can be changed to obtain a more precise enrichment results. The Options are available in the Network specific enrichment panel settings section which can be accessed by clicking the gear icon. For example, you can remove redundant terms in the table by selecting the appropriate redundancy (Jaccard) cutoff, the default is 0.5.

![](_static/images/Enrichment_Table/gear.png)


<a id="map"> </a>
## Enrichment Map Generation
We can generate [Enrichment Map](https://www.baderlab.org/Software/EnrichmentMap) from the enrichment data generated by our app. This requires [Enrichment Map](https://apps.cytoscape.org/apps/enrichmentmap) to be installed in Cytoscape. Once, enrichment map app is present, click enrichment map icon and which will provide a panel to change the file name and connectivity cutoff, and click ok to generate map.
<a id="export"> </a>
## Export results
Enrichment Table App provides functionality to export the data:

- Select the  icon that will open the export panel.
- Select appropriate location and file name and save the table.

The default file extension is .**csv**.

![](_static/images/Enrichment_Table/export.png)