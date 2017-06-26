<a id="programmatic_access_to_cytoscape_features_scripting"> </a>
# Programmatic Access to Cytoscape Features (Scripting)

<a id="programmatic_access_to_cytoscape_features"> </a>
## Programmatic Access to Cytoscape Features

In this chapter, you will learn how to use Cytoscape from the command
line and scripts. These features replace the ***Scripting*** module in
past versions of Cytoscape.

<a id="topics"> </a>
## Topics

-   ***Commands***

-   **RESTful API**

    -   **Command REST API**

    -   **cyREST**

<a id="background"> </a>
## Background

Cytoscape's intuitive graphical user interface is useful for
*interactive* network data integration, analysis, and visualization. It
provides great features for exploratory data analysis, but what happens
if you have hundreds of data files or need to ask someone to execute
your data analysis workflows? It is virtually impossible to apply the
same operations to hundreds of networks manually using a GUI. More
importantly, although you can save your ***results*** as session files,
you cannot save your ***workflows*** if you perform your data analysis
with point-and-click GUI operations. Cytoscape has several options that
support scripting and automating your workflows: Commands and RESTful
API.

The Command feature allows you to script a number of Cytoscape commands
and menu items, and commands can have parameter values that would
normally be provided by a user via Cytoscape dialog box. For example,
*session open file="C:\\myfile.cys"* loads a session from a file
similarly to the **File | Open** menu item. You can create a command
script file that Cytoscape can execute via the **Tools | Execute Command
File** menu item or on the Cytoscape command line at startup.

The RESTful API feature allows you to access Cytoscape from a separate
application, thereby orchestrating Cytoscape operations from that
application. The application may be written in a general programming
language (e.g., Python) that keeps its own data structures, performs
complex flow control, or directly manipulates Cytoscape nodes, edges,
attributes, and visual styles.

The Command feature is useful for executing sequences of commands,
whereas the RESTful API feature is useful when Cytoscape is to be used
as a service relative to an application.

<a id="commands"> </a>
### Commands

![CommandTool.png](_static/images/ProgrammaticAccess/CommandTool.png)

***Commands*** is the built-in Cytoscape feature to automate your
workflow as simple script. You can learn more about this feature in this
section:

-   [Command
    Tool](Command_Tool.html#command-tool)

<a id="restful_api"> </a>
### RESTful API

In some cases, you may need to use fully featured programming languages,
such as Python, R, Ruby, or
[JavaScript](https://en.wikipedia.org/wiki/JavaScript)
to script your workflow. Such languages enable complex control and data
structures, and Cytoscape would be called as a service. For such use
cases, accessing Cytoscape via REST API is the right option.

Cytoscape offers two flavors of REST-style control: REST Commands and
cyREST. REST Commands uses a REST interface to issue script commands.
cyREST uses a REST interface to access the Cytoscape data model as a
document via a formal API.

#### 1. Configuring Automation

While Cytoscape is running, a REST server listens for HTTP requests on a preconfigured port. By default, this port is 1234, but this can be manually configured in two ways.

1.  When starting Cytoscape:

    -   Use [PowerShell](https://en.wikipedia.org/wiki/Windows_PowerShell)
        or Command (For windows)

    -   Start cytoscape by typing the command ```./cytoscape.sh -R 8888``` to start Cytoscape with its REST server listening on port 8888. You can replace 8888 with any valid port number.

2.  From the Cytoscape Preferences Editor:

    -   From the Cytoscape main menu, select Edit --> Preferences --> Properties.
    
    -   In the Cytoscape Preferences Editor, find the Property Name 'rest.port' and set the Value field to your new port number.
    
    -   Restart Cytoscape for this change to take effect.

To test your settings, in your web browser, go to the address ```http://localhost:8888/``` (replace 8888 with your port number if necessary). You should see a JSON list of all available API versions, which should look similar to the one below:

```json
{"availableApiVersions":["v1"]}
```

#### 2. cyREST

![_static/images/ProgrammaticAccess/logo300.png](_static/images/ProgrammaticAccess/logo300.png)

**[cyREST](http://apps.cytoscape.org/apps/cyrest) is a
language-agnostic, programmer-friendly RESTful API module for
Cytoscape**. If you want to build your own workflow with
[R](http://www.r-project.org/), [Python](https://www.python.org/) or
other programming languages along with Cytoscape, this is the option for
you. You can use popular tools, including IPython/Jupyter Notebook and
RStudio as your orchestration tool for your data visualization workflow
with Cytoscape.

![jupyter.png](_static/images/ProgrammaticAccess/jupyter.png)

You can find useful scripts for learning to automate Cytoscape in R and Python in the [Cytoscape Automation for Script Writers](https://github.com/cytoscape/cytoscape-automation/tree/master/for-scripters) repository.

Currently, cyREST is available as an App for Cytoscape 3.2.1 and later,
and requires the Java 8 (or later) virtual machine. As of Cytoscape
v3.3, cyREST is installed automatically with Cytoscape. Please visit the
link below for more information.

-   [cyREST App Store page](http://apps.cytoscape.org/apps/cyrest)
