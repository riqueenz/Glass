# Glass module for FreeCAD
# Copyright (C) 2018, 2020 triplus @ FreeCAD
#
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

"""Glass module for FreeCAD - Gui."""


import FreeCADGui as Gui
import FreeCAD
from PySide import QtGui
from PySide import QtCore

mode = 0
wid = QtGui.QWidget()
mw = Gui.getMainWindow()
p = FreeCAD.ParamGet("User parameter:BaseApp/Glass")


try:
    mw.setDockOptions(mw.dockOptions() | mw.GroupedDragging)
except AttributeError:
    pass


def firstRun():
    """Setup defaults on the first run."""
    pTree = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/DockWindows/TreeView")
    pTree.SetBool("Enabled", True)

    pStyle = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/MainWindow")
    pStyle.SetString("StyleSheet", "Light-blue.qss")
    
    param = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/DockWindows/TreeView')
    param.SetBool("Enabled", True)
    param = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/DockWindows/PropertyView')
    param.SetBool("Enabled", False)
    param = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/DockWindows/DAGView')
    param.SetBool("Enabled", False)
    param = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/DockWindows/ComboView')
    param.SetBool("Enabled", False)
    
    param = FreeCAD.ParamGet('User parameter:BaseApp/MainWindow/DockWindows')
    param.SetBool("Std_ReportView", False)
    param.SetBool("Std_SelectionView", False)
    param.SetBool("Std_ComboView", False)
    param.SetBool("Std_PythonView", False)
    param.SetBool("Std_TreeView", True)
    param.SetBool("Std_PropertyView", False)
    param.SetBool("Std_ReportView", False)
    
    #Disable some toolbars
    param = FreeCAD.ParamGet('User parameter:BaseApp/MainWindow/Toolbars')
    param.SetBool("File", True)
    param.SetBool("Workbench", False)
    param.SetBool("Macro", False)
    param.SetBool("View", True)
    param.SetBool("Navigation", False)
    param.SetBool("Structure", True)
    param.SetBool("Part Design Modeling", True)
    param.SetBool("Part Design Helper", True)
    param.SetBool("Sketcher", True)
    param.SetBool("Sketcher geometries", True)
    param.SetBool("Sketcher constraints", True)
    param.SetBool("Sketcher tools", False)
    param.SetBool("Sketcher B-spline tools", False)
    param.SetBool("Mesure", True)
    param.SetBool("Tabs", True)
    param.SetBool("Sketcher virtual space", False)

    pView = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View")
    pView.SetUnsigned("BackgroundColor", 336897023)
    pView.SetUnsigned("BackgroundColor2", 3857049087)
    pView.SetUnsigned("BackgroundColor3", 3469659903)
    pView.SetUnsigned("BackgroundColor4", 1869583359)
    pView.SetUnsigned("HighlightColor", 3789624575)
    pView.SetUnsigned("SelectionColor", 481107199)
    pView.SetUnsigned("DefaultShapeColor", 3435973887)
    pView.SetUnsigned("DefaultShapeLineColor", 421075455)
    pView.SetUnsigned("DefaultShapeVertexColor", 421075455)
    pView.SetUnsigned("BoundingBoxColor", 4294967295)
    pView.SetUnsigned("AnnotationTextColor", 3402287871)
    pView.SetUnsigned("SketchEdgeColor", 4294967295)
    pView.SetUnsigned("SketchVertexColor", 4294967295)
    pView.SetUnsigned("EditedEdgeColor", 5636095)
    pView.SetUnsigned("EditedVertexColor", 5636095)    
    pView.SetUnsigned("ConstructionColor", 4294902015)
    pView.SetUnsigned("ExternalColor", 1442775295)
    pView.SetUnsigned("InvalidSketchColor", 4278190335)
    pView.SetUnsigned("FullyConstrainedColor", 1044266751)
    pView.SetUnsigned("InternalAlignedGeoColor", 5636095)
    pView.SetUnsigned("FullyConstraintElementColor", 1044266751)
    pView.SetUnsigned("FullyConstraintConstructionElementColor", 2868871167)
    pView.SetUnsigned("FullyConstraintInternalAlignmentColor", 1044266751)
    pView.SetUnsigned("FullyConstraintConstructionPointColor", 1044266751)
    pView.SetUnsigned("ConstrainedIcoColor", 4283760895)
    pView.SetUnsigned("NonDrivingConstrDimColor", 2555903)
    pView.SetUnsigned("ConstrainedDimColor", 4280680703)
    pView.SetUnsigned("ExprBasedConstrDimColor", 4286523135)
    pView.SetUnsigned("DeactivatedConstrDimColor", 2139062271)
    pView.SetUnsigned("CursorTextColor", 5636095)
    pView.SetUnsigned("CursorCrosshairColor", 4294967295)
    pView.SetUnsigned("CreateLineColor", 5636095)
    pView.SetInt("AntiAliasing", 4)
    pView.SetBool("UseVBO", True)
    
    param = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/General')
    param.SetString("AutoloadModule", "PartDesignWorkbench")
    
    #TabBar
    param = FreeCAD.ParamGet('User parameter:BaseApp/TabBar')
    param.SetString("Enabled", "MoocWorkbench,SketcherWorkbench,PartDesignWorkbench,TechDrawWorkbench,A2plusWorkbench,SpreadsheetWorkbench,SMWorkbench,SurfaceWorkbench")
    param.SetString("Orientation", "South")
    param.SetString("Partially", "ArchWorkbench,DraftWorkbench,FemWorkbench,ImageWorkbench,InspectionWorkbench,MeshWorkbench,NoneWorkbench,OpenSCADWorkbench,PartWorkbench,PathWorkbench,PointsWorkbench,RaytracingWorkbench,ReverseEngineeringWorkbench,RobotWorkbench,StartWorkbench,TestWorkbench,WebWorkbench")
    param.SetString("Position", "MoocWorkbench,SketcherWorkbench,PartDesignWorkbench,TechDrawWorkbench,A2plusWorkbench,SpreadsheetWorkbench,SMWorkbench,SurfaceWorkbench,ArchWorkbench,DraftWorkbench,FemWorkbench,ImageWorkbench,InspectionWorkbench,MeshWorkbench,NoneWorkbench,OpenSCADWorkbench,PartWorkbench,PathWorkbench,PointsWorkbench,RaytracingWorkbench,ReverseEngineeringWorkbench,RobotWorkbench,StartWorkbench,TestWorkbench,WebWorkbench")
    param.SetString("PrefButton", "On")
    param.SetString("Style", "IconText")
    
    #A2Plus
    param = FreeCAD.ParamGet('User parameter:Tux/PersistentToolbars/User/A2plusWorkbench')
    param.SetString("Top", "Tabs,Break,File,Structure,Macro,View,Break,A2p_Part,A2p_Constraint,A2p_Misc,A2Diagnostics,A2p_Solver,Break,A2p_View")
    param.SetString("Left", "")
    param.SetString("Right", "")
    param.SetString("Bottom", "Workbench")
    param.SetBool("Saved", True)
    
    #MOOC
    param = FreeCAD.ParamGet('User parameter:Tux/PersistentToolbars/User/MoocWorkbench')
    param.SetString("Top", "Tabs,Break,File,Structure,View,Macro,Break,MOOC")
    param.SetString("Left", "")
    param.SetString("Right", "")
    param.SetString("Bottom", "Workbench")
    param.SetBool("Saved", True)
    
    #PartDesign
    param = FreeCAD.ParamGet('User parameter:Tux/PersistentToolbars/User/PartDesignWorkbench')
    param.SetString("Top", "Break,Tabs,Break,File,Structure,View,Break,Part Design Helper,Part Design Modeling,Measure")
    param.SetString("Left", "")
    param.SetString("Right", "")
    param.SetString("Bottom", "Workbench")
    param.SetBool("Saved", True)
    
    #Sketcher
    param = FreeCAD.ParamGet('User parameter:Tux/PersistentToolbars/User/SketcherWorkbench')
    param.SetString("Top", "Tabs,Break,File,Structure,View,Macro,Break,Sketcher,Sketcher geometries,Sketcher constraints")
    param.SetString("Left", "")
    param.SetString("Right", "")
    param.SetString("Bottom", "Workbench")
    param.SetBool("Saved", True)
    
    #SheetMetal
    param = FreeCAD.ParamGet('User parameter:Tux/PersistentToolbars/User/SMWorkbench')
    param.SetString("Top", "Tabs,Break,File,View,Macro,Structure,Break,Sheet Metal")
    param.SetString("Left", "")
    param.SetString("Right", "")
    param.SetString("Bottom", "Workbench")
    param.SetBool("Saved", True)
    
    #Spreadsheet
    param = FreeCAD.ParamGet('User parameter:Tux/PersistentToolbars/User/SpreadsheetWorkbench')
    param.SetString("Top", "Tabs,Break,File,View,Macro,Structure,Break,Spreadsheet")
    param.SetString("Left", "")
    param.SetString("Right", "")
    param.SetString("Bottom", "Workbench")
    param.SetBool("Saved", True)
    
    #Surface
    param = FreeCAD.ParamGet('User parameter:Tux/PersistentToolbars/User/SurfaceWorkbench')
    param.SetString("Top", "Tabs,Break,File,View,Macro,Structure,Break,Surface")
    param.SetString("Left", "")
    param.SetString("Right", "")
    param.SetString("Bottom", "Workbench")
    param.SetBool("Saved", True)
    
    #TechDraw
    param = FreeCAD.ParamGet('User parameter:Tux/PersistentToolbars/User/TechDrawWorkbench')
    param.SetString("Top", "Break,Tabs,Break,File,Structure,View,Break,TechDraw Dimensions,TechDraw File Access,TechDraw Decoration,TechDraw Pages,TechDraw Annotation,TechDraw Stacking,TechDraw Views,TechDraw Clips,TechDraw Attributes,TechDraw Centerlines,TechDraw Extend Dimensions")
    param.SetString("Left", "")
    param.SetString("Right", "")
    param.SetString("Bottom", "Workbench")
    param.SetBool("Saved", True)
    
    #Fasteners
    param = FreeCAD.ParamGet('User parameter:BaseApp/Preferences/Mod/Fasteners')
    param.SetInt("ScrewToolbarGroupMode", 2)


def findDock():
    """Find combo view widget."""
    global dock
    dock = mw.findChild(QtGui.QDockWidget, "Tree view")


def createActions():
    """Create actions."""
    a1 = QtGui.QAction(mw)
    a1.setParent(mw)
    a1.setText("Glass toggle dock mode")
    a1.setObjectName("GlassToggleMode")
    a1.setShortcut(QtGui.QKeySequence("Q, 1"))
    a1.triggered.connect(setMode)
    mw.addAction(a1)
    a2 = QtGui.QAction(mw)
    a2.setParent(mw)
    a2.setText("Glass toggle dock visibility")
    a2.setObjectName("GlassToggleVisibility")
    a2.setShortcut(QtGui.QKeySequence("Q, 2"))
    a2.triggered.connect(setVisibility)
    mw.addAction(a2)


def applyGlass(boolean, widget):
    """Apply or remove glass."""
    try:
        if boolean:
            widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        else:
            widget.setWindowFlags(dock.windowFlags() & ~QtCore.
                                  Qt.
                                  FramelessWindowHint)
    except:
        pass
    try:
        widget.setAttribute(QtCore.Qt.WA_NoSystemBackground, boolean)
    except:
        pass
    try:
        widget.setAttribute(QtCore.Qt.WA_TranslucentBackground, boolean)
    except:
        pass
    try:
        if boolean:
            widget.setStyleSheet("background:transparent; border:none; color:black;")
        else:
            widget.setStyleSheet("")
    except:
        pass
    try:
        widget.setAutoFillBackground(boolean)
    except:
        pass
    try:
        if boolean:
            widget.setVerticalScrollBarPolicy((QtCore.Qt.ScrollBarAlwaysOff))
        else:
            widget.setVerticalScrollBarPolicy((QtCore.Qt.ScrollBarAsNeeded))
    except:
        pass
    try:
        if boolean:
            widget.setHorizontalScrollBarPolicy((QtCore.Qt.ScrollBarAlwaysOff))
        else:
            widget.setHorizontalScrollBarPolicy((QtCore.Qt.ScrollBarAsNeeded))
    except:
        pass
    try:
        widget.setDocumentMode(boolean)
    except:
        pass
    try:
        widget.tabBar().setDrawBase(False)
    except:
        pass
    try:
        if boolean:
            widget.header().hide()
        else:
            widget.header().show()
    except:
        pass


def widgetList(boolean):
    """List of child widgets."""
    children = []
    children.append(dock)

    child = True
    while child:
        child = False
        for i in children:
            if i.children():
                for c in i.children():
                    if c not in children:
                        children.append(c)
                        child = True

    for child in children:
        applyGlass(boolean, child)


def setMode():
    """Set dock or overlay widget mode."""
    global mode
    mdi = mw.findChild(QtGui.QMdiArea)

    if mode == 0:
        dock.setParent(mdi)
        dock.setTitleBarWidget(wid)
        wid.hide()
        dock.show()
        widgetList(True)
        mode = 1
    else:
        dock.setParent(mw)
        dock.setTitleBarWidget(None)
        mw.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
        dock.show()
        widgetList(False)
        mode = 0

    onResize()


def setVisibility():
    """Toggle visibility."""
    dock.toggleViewAction().trigger()


def onResize():
    """Resize dock."""
    mdi = mw.findChild(QtGui.QMdiArea)

    if mode == 1:
        x = 0
        y = 0
        w = mdi.geometry().width() / 100 * 20
        h = (mdi.geometry().height() -
             mdi.findChild(QtGui.QTabBar).geometry().height())
        dock.setGeometry(x, y, w, h)

    if str(Gui.activeView()) == "View3DInventor":
        dock.show()
    else:
        dock.hide()


def onStart():
    """Start the glass module."""
    if mw.property("eventLoop"):
        timer.stop()
        timer.timeout.disconnect(onStart)
        findDock()
        createActions()
        if p.GetBool("glassAuto", 1):
            setMode() # activate Glass mode
        timer.timeout.connect(onResize)
        timer.start(2000)


if p.GetBool("FirstRun", 1):
    """Setup defaults on the first run."""
    firstRun()
    p.SetBool("FirstRun", 0)


timer = QtCore.QTimer()
timer.timeout.connect(onStart)
timer.start(500)
