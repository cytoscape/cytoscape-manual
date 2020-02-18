<a id="panels"> </a>
# Panels

**Panels** are floatable/dockable panels designed to cut down on the number of pop-up windows within Cytoscape 
and to create a more unified user experience. 

There are five panels that can be visible or hidden:
- Control Panel (left)
- Tool Panel (bottlom left)
- Table Panel (bottom right)
- Results Panel (right)
- Automation Panel (bottom)

Each panel typically contains multiple tabs. For example the **Control Panel** contains at a minimum the **Network**,
**Style**, **Filter** and **Annotation** tabs. The **Table Panel** contains the **Node Table**, **Edge Table** and
**Network Table** tabs. Analysis results from _Analyzer_ (**Tools → Analyze Network**) 
are shown in **Results Panel**. Installed Apps may add additional tabs.

![](_static/images/Panels/DockWindow-v3_8_0.png)

These panels can compete for valuable screen real-estate (e.g. by making the network view too small), so it is important to manage each panel's state and size properly and acconding to the user's needs.
You can take advantage of these 5 panel states in order to manage the available screen real-estate:
- **Hidden:** A panel can be totally removed from the screen if you find it unnecessary. To do that, just uncheck the corresponding option under the **View** menu (e.g. uncheck **View → Show Results Panel** to hide the _Results Panel_). When a panel is hidden, its tabs no long appear in the sidebar, so in order to show the panel again, you have to check the same menu option.

  Alternatively, you can right-click an empty space on any sidebar to hide/show a panel:
  
  ![](_static/images/Panels/RightClickShowPanel.png)

- **Minimized:** Use the **Minimize** icon ![](_static/images/Panels/MinimizeIcon.png) at the top-right corner of a panel to quickly hide it when it is of no current interest. But differently from the hidden state, the tabs from a minimized panel still appear on the sidebar, so that by clicking any tab, the panel can be shown again as undocked. Notice that some panels (e.g. _Tool Panel_) may be minimized by default.

  In the example below, the _Control_ and _Tool_ panels are minimized (_Results_ and _Automation_ are hidden):
  
  ![](_static/images/Panels/ExampleMinimized.png)

- **Docked:** The most used panels (e.g. _Control_, _Table_) are initially docked by default after a clean installation of Cytoscape. When docked, a panel takes the space that could be used by its adjacent panels and by resizing it, those adjacent panels are resized as well (e.g. by resizing the "Control" panel horizontally, the "View" panel is also resized). If a panel is undocked or floating, use the **Dock** icon ![](_static/images/Panels/DockIcon.png) to make it docked.

  In the screenshot below, all panels are docked, except _Results_ and _Automation_, which are hidden:
  
  ![](_static/images/Panels/ExampleDocked.png)

- **Undocked:** A panel is undocked when the **Undock** icon ![](_static/images/Panels/UndockIcon.png) is clicked or a minimized panel is shown again by clicking one of its tabs on the sidebar. In this state, the panel is displayed over other panels but is still anchored to one of Cytoscape corners. That allows it to be resized more freely (vertically and horizontally) whithout affecting the size of other panels. You can also double-click the undocked panel's title bar to quickly maximize it. And double-clicking the title bar of a maximized panel again will restore it to its previous size. To temporarily hide an undocked panel, just click the **Minimize** icon ![](_static/images/Panels/MinimizeIcon.png). Notice that an undocked panel will also be automatically minimized when other panels or components outside the undocked panel are clicked.

  In the example below, the _Control_ panel is undocked:

  ![](_static/images/Panels/ExampleUndocked.png)

- **Floating:** Use the **Float** icon ![](_static/images/Panels/FloatIcon.png) to completely detach a panel from the Cytoscape desktop. A floating panel has its own window that can be resized, maximized and minimized just like any other application window and it can also be moved to another monitor in a multi-monitor setup. When a panel is floating, its tabs are not removed from the corresponding sidebar in the main desktop window, but you can also use the drop-down in the floating panel's title bar to show another tab's content.

  In the image below, the _Control_, _Table_ and _Tool_ panels are floating:
  
  ![](_static/images/Panels/ExampleFloating.png)
