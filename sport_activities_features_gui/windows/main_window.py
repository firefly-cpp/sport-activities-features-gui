from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets, sip
from sport_activities_features_gui.widgets.graphs_widget import Ui_GraphsWidget
from sport_activities_features_gui.widgets.calendar_widget import Ui_CalendarWidget
from sport_activities_features_gui.widgets.transformations_widget import Ui_TransformationsWidget
from sport_activities_features_gui.widgets.import_data_widget import Ui_ImportDataWidget
from sport_activities_features_gui.models.user import User


class Ui_MainWindow(QMainWindow):
    globalUser: User
    importDataUi: Ui_ImportDataWidget
    graphsUi = Ui_GraphsWidget
    calendarUi = Ui_CalendarWidget
    transformationsUi = Ui_TransformationsWidget

    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName("Sport Activities Features GUI")
        self.setWindowIcon(QtGui.QIcon('./media/Icon.png'))
        self.setEnabled(True)
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabWidget.setGeometry(QtCore.QRect(0, 0, 811, 551))
        self.mainTabWidget.setObjectName("mainTabWidget")
        # IMPORT DATA
        self.tab_ImportData = QtWidgets.QWidget()
        self.tab_ImportData.setObjectName("tab_ImportData")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_ImportData)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainLayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout_1.setContentsMargins(0, 0, 0, 0)
        self.mainLayout_1.setObjectName("mainLayout_1")
        self.mainTabWidget.addTab(self.tab_ImportData, "")
        # GRAPHS
        self.tab_Graphs = QtWidgets.QWidget()
        self.tab_Graphs.setObjectName("tab_Graphs")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_Graphs)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 801, 521))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.mainLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.mainLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainLayout_2.setObjectName("mainLayout_2")
        self.mainTabWidget.addTab(self.tab_Graphs, "")
        # CALENDAR
        self.tab_Calendar = QtWidgets.QWidget()
        self.tab_Calendar.setObjectName("tab_Calendar")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_Calendar)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 801, 521))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.mainLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.mainLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainLayout_4.setObjectName("mainLayout_4")
        self.mainTabWidget.addTab(self.tab_Calendar, "")
        # TRANSFORMATIONS
        self.tab_Transformations = QtWidgets.QWidget()
        self.tab_Transformations.setObjectName("tab_Transformations")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(
            self.tab_Transformations)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 801, 521))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.mainLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.mainLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainLayout_3.setObjectName("mainLayout_3")
        self.mainTabWidget.addTab(self.tab_Transformations, "")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QWidgetAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionImport_Data = QtWidgets.QWidgetAction(self)
        self.actionImport_Data.setObjectName("actionImport_Data")
        self.actionCalendar = QtWidgets.QWidgetAction(self)
        self.actionCalendar.setObjectName("actionCalendar")
        self.actionGraphs = QtWidgets.QWidgetAction(self)
        self.actionGraphs.setObjectName("actionGraphs")
        self.actionTransformations = QtWidgets.QWidgetAction(self)
        self.actionTransformations.setObjectName("actionTransformations")

        self.retranslateUi()
        self.mainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        # TAB WIDGETS
        self.importDataUi = Ui_ImportDataWidget(refMainWindow=self)
        self.mainLayout_1.addWidget(self.importDataUi)
        self.graphsUi = Ui_GraphsWidget(refMainWindow=self)
        self.mainLayout_2.addWidget(self.graphsUi)
        self.calendarUi = Ui_CalendarWidget(refMainWindow=self)
        self.mainLayout_4.addWidget(self.calendarUi)
        self.transformationsUi = Ui_TransformationsWidget(refMainWindow=self)
        self.mainLayout_3.addWidget(self.transformationsUi)        
        

        self.actionExit.triggered.connect(self.close)

    def retranslateUi(self):
        self.setWindowTitle("Sport Activities Features GUI")
        self.mainTabWidget.setTabText(
            self.mainTabWidget.indexOf(self.tab_ImportData), "Import Data")
        self.mainTabWidget.setTabText(
            self.mainTabWidget.indexOf(self.tab_Graphs), "Graphs")
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(
            self.tab_Transformations), "Transformations")
        self.mainTabWidget.setTabText(
            self.mainTabWidget.indexOf(self.tab_Calendar), "Calendar")

        self.actionImport_Data.setText("Import Data")
        self.actionGraphs.setText("Graphs")
        self.actionTransformations.setText("Transformations")
        self.actionCalendar.setText("Calendar")

    # IMPORT GLOBAL USER
    def importGlobalUser(self, user):
        self.setWindowTitle(
            "Sport Activities Features GUI - for profile: \"" + user.username + "\"")
        self.globalUser = user
        self.importDataUi.importGlobalUser(user)
        self.calendarUi.importGlobalUser(user)
        self.graphsUi.importGlobalUser(user)
        self.transformationsUi.importGlobalUser(user)

    def refreshWidget(self, layout, widget, widgetClass):
        layout.removeWidget(widget)
        sip.delete(widget)
        widget = None
        widget = widgetClass(refMainWindow=self)
        layout.addWidget(widget)
        widget.importGlobalUser(self.globalUser)

    def refreshImportDataWidget(self):
        self.refreshWidget(self.mainLayout_1, self.importDataUi, Ui_ImportDataWidget)
    
    def refreshCalendarWidget(self):
        self.refreshWidget(self.mainLayout_4, self.calendarUi, Ui_CalendarWidget)        

    def refreshGraphsWidget(self):
        self.refreshWidget(self.mainLayout_2, self.graphsUi, Ui_GraphsWidget)
    
    def refreshTransformationsWidget(self):
        self.refreshWidget(self.mainLayout_3, self.transformationsUi, Ui_TransformationsWidget)
        
    def refreshAllWidgets(self):
        self.refreshImportDataWidget()
        self.refreshCalendarWidget()
        self.refreshGraphsWidget()
        self.refreshTransformationsWidget()
        