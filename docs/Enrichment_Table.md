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

Now you get the table containing enrichment results. The results are sorted according to the p-value in a increasing order by default.

<a id="filter"> </a>
## Filter Results

<a id="ring"> </a>
## Ring Charts

<a id="term"> </a>
## Term Selection

<a id="optional"> </a>
## Optional Settings

<a id="map"> </a>
## Enrichment Map Generation

<a id="export"> </a>
## Export results
