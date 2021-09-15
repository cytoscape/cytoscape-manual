<a id="command_line_arguments"> </a>
# Command Line Arguments


Cytoscape recognizes a number of optional command line arguments,
including run-time specification of network files, node and edge data
files, and session files. This is the output generated when Cytoscape is
executed with the _-h_ or _--help_ flag:

    usage: cytoscape.{sh|bat} [OPTIONS]
     -h,--help             Print this message.
     -v,--version          Print the version number.
     -s,--session <file>   Load a cytoscape session (.cys) file.
     -N,--network <file>   Load a network file (any format).
     -P,--props <file>     Load cytoscape properties file (Java properties
                           format) or individual property: -P name=value.
     -V,--vizmap <file>    Load vizmap properties file (Cytoscape VizMap
                           format).
     -S,--script <file>    Execute commands from script file.
     -R,--rest <port>      Start a rest service.

Any file specified for an option may be specified as either a path or as
a URL. For example you can specify a network as a file (assuming that
myNet.sif exists in the current working directory):
`cytoscape.sh -N myNet.sif`.

Note: if there are spaces in the file path, be sure to put quotes around
it:
`cytoscape.bat -N "C:\Program Files\Cytoscape\sampleData\galFiltered.sif"`.

Or you can specify a network as a URL:
`cytoscape.sh -N http://example.com/myNet.sif`.

<table cellspacing="0" style="table-layout: fixed; width: 700px">
<caption>Command Line Arguments</caption>
<colgroup> <col style="width:170px">                           <col style="width:530px"> </colgroup>
<tbody>
<tr> <th>Argument</th>                                         <th>Description</th>                                                                      </tr>
<tr> <th class="spec ulcase">-h,--help</th>                    <td class="">This flag generates the help output you see above and exits.</td>            </tr>
<tr> <th class="specalt ulcase">-v,--version</th>              <td class="alt">This flag prints the version number of Cytoscape and exits.</td>          </tr>
<tr> <th class="spec ulcase">-s,--session &lt;file&gt;</th>    <td class="">This option specifies a session file to be loaded. Since only one session file can be loaded at a given time, this option may only specified once on a given command line. The option expects a <code>.cys</code> Cytoscape session file. It is customary, although not necessary, for session file names to contain the .cys extension.</td> </tr>
<tr> <th class="specalt ulcase">-N,--network &lt;file&gt;</th> <td class="alt">This option is used to load all types of network files. SIF, GML, and XGMML files can all be loaded using the -N option. You can specify as many networks as desired on a single command line.</td> </tr>
<tr> <th class="spec ulcase">-P,--props &lt;file&gt;</th>      <td class="">This option specifies Cytoscape properties. Properties can be specified either as a properties file (in Java's standard properties format), or as individual properties. To specify individual properties, you must specify the property name followed by the property value where the name and value are separated by the '=' sign. For example to specify the defaultSpeciesName: <code>cytoscape.sh -P defaultSpeciesName=Human</code>. If you would like to include spaces in your property, simply enclose the name and value in quotation marks: <code>cytoscape.sh -P "defaultSpeciesName=Homo Sapiens"</code>. The property option subsumes previous options -noCanonicalization, -species, and -bioDataServer. Now it would look like: <code>cytoscape.sh </code> <code>-P defaultSpeciesName=Human </code> <code>-P noCanonicalization=true </code> <code>-P bioDataServer=myServer</code>.</td> </tr>
<tr> <th class="specalt ulcase">-V,--vizmap &lt;file&gt;</th>  <td class="alt">This option specifies a Style file.</td>                                  </tr>
<tr> <th class="spec ulcase">-S,--script &lt;file&gt;</th>     <td class="">This option executes commands from a specifed Cytoscape script file.</td>    </tr>
<tr> <th class="specalt ulcase">-R,--rest &lt;port&gt;</th>    <td class="alt">This option starts a Cytoscape REST service on the specified port.</td>   </tr>
</tbody>
</table>
<br>
  
  
All options described above (except for starting a REST service) can be
accessed from the menu once Cytoscape is running.
