<a id="rendering_engine"> </a>
# Rendering Engine

<a id="what_is_level_of_detail_lod"> </a>
## What is Level of Detail (LOD)?

Cytoscape is able to display large networks (> 10,000 nodes) while 
maintaining interactive speed. To accomplish this goal the 
**level of detail (LOD)** used to display the network is 
chosen based on the number of nodes and edges currently being displayed. 
For example, by default, node labels (if present) are only
rendered when less than 200 nodes are visible because drawing text is a
relatively expensive operation. This can create some unusual behavior.
If the screen currently contains 198 nodes, node labels will be
displayed. If you pan across the network, such that now 201 nodes are
displayed, the node labels will disappear. As another example, if the
sum of rendered edges and rendered nodes is greater than or equal to a
default value of 4000, a very coarse level of detail is chosen, where
edges are always straight lines, nodes are always rectangles, and no
anti-aliasing is done. 

Additionally Cytoscape may temporarily lower the **level of detail** even
more while the network is being interacted with (eg. panning, 
zooming, moving a node). For example edges and charts may not be displayed
during interaction. When the network is no longer being interacted 
with it will be displayed again in higher detail. 


**Low LOD vs High LOD**

<table cellspacing="0">
<caption>Levels of Detail</caption>
<tbody>
<tr> <th class="center">Network with <b>Low</b> LOD</th>                                                            <th class="center">Network with <b>High</b> LOD</th>                                                       </tr>
<tr> <td class="center left"><img src="_static/images/Rendering_Engine/LowLOD.png" height="589" width="336" /></td> <td class="center"><img src="_static/images/Rendering_Engine/HighLOD.png" height="589" width="336" /></td> </tr>
</tbody>
</table>
<br>

With low LOD values, all nodes are displayed as square and anti-aliasing
is turned off. With high LOD values, anti-aliasing is turned on and
nodes are displayed as actual shape user specified in the Style.


<a id="force_to_display_detail"> </a>
### Force to Display Detail

If you want to display every detail of the network at all times regardless of LOD
values, you can toggle to full details mode by **View → Always Show Graphics
Details** (or CTR+SHIFT+D on Windows/Linux, Command+SHIFT+D for Mac), or click the 
**Always Show Graphics
Details** button ![](_static/images/Rendering_Engine/lod-button.png) in the **Network View Tools**.
This option forces the display of all graphics details. If the network
is large, this option slows down rendering speed. To hide details,
unselect the menu item (**View → Always Show Graphics Details**).


<a id="parameters_for_controlling_lod"> </a>
### Parameters for Controlling LOD

The default values used to determine level of detail
can be changed by setting properties under **Edit → Preferences → Properties...**.

**NOTE:** *The greater these thresholds become, the slower performance
will become.* If you work with small networks (a few hundred nodes),
this shouldn't be a problem, but for large networks it will produce
noticeable slowing. The various thresholds are described below.

**NOTE:** Since Cytoscape 3.9 interactivity will always be maintained
even when a high level of detail is chosen. It is generally safe
to increase the level of detail or to force full graphics details even
for very large networks.

<table cellspacing="0">
<caption>LOD Thresholds</caption>
<tr> <th class="">Parameter</th>                          <th class="">Description</th>                                                                                                                                  </tr>
<tr> <th class="spec">render.coarseDetailThreshold</th>  <td class="">If the sum of <i>rendered</i> nodes and <i>rendered</i> edges equals to or exceeds this number, a very coarse level of detail will be chosen and all other detail parameters will be ignored. If the total number of nodes and edges is below this threshold, anti-alias will be turned on; this value defaults to 4000.</td> </tr>
<tr> <th class="specalt">render.nodeBorderThreshold</th> <td class="alt">If the number of <i>rendered</i> nodes equals to or exceeds this number, node borders will not be rendered; this value defaults to 400.</td>  </tr>
<tr> <th class="spec">render.nodeLabelThreshold</th>     <td class="">If the number of <i>rendered</i> nodes equals to or exceeds this number, node labels will not be rendered; this value defaults to 200.</td>      </tr>
<tr> <th class="specalt">render.edgeArrowThreshold</th>  <td class="alt">If the number of <i>rendered</i> edges equals to or exceeds this number, edge arrows will not be rendered; this value defaults to 600.</td>   </tr>
<tr> <th class="spec">render.edgeLabelThreshold</th>     <td class="">If the number of <i>rendered</i> edges equals to or exceeds this number, edge labels will not be rendered; this value defaults to 200.</td>      </tr>
<tr> <th class="spec">render.hidpi</th>     <td class="">This property enables/disables HiDPI mode in the network view. When set to true the network will render in the native resolution on 4K Ultra-HD and Retina displays. New in Cytoscape 3.9. Defaults to true.</td>      </tr>
<tr> <th class="spec">render.labelCache</th>     <td class="">This property enables/disables the renderer label cache, which results in a significant rendering speed improvement when enabled. New in Cytoscape 3.9. Defaults to true.</td>      </tr>
<tr> <th class="spec">render.edgeBufferPan</th>     <td class="">This property enables/disables a feature in the renderer which shifts the edge buffer when panning the network, which avoids having to hide edges when panning in certain situations. New in Cytoscape 3.9. Defaults to true. </td>      </tr>
</table>
<br>

When printing networks or exporting to formats such as PostScript, the
highest level of detail is always chosen, regardless of what is
currently being displayed on the screen.


