import pandas as pd
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QPushButton


class Ui_ViewAttributesWindow(QMainWindow):
    data = []

    def __init__(self):
        super().__init__()
        self.setObjectName("ViewAttributesWindow")
        self.resize(389, 597)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listView")
        self.verticalLayout.addWidget(self.listWidget)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.selectedAttribute = None
        self.result = False  # True if user clicked Save, False if user clicked Close
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save)
        self.verticalLayout.addWidget(self.save_button)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        self.verticalLayout.addWidget(self.close_button)
        self.axis = None

        self.callback = None

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def save(self):
        self.selectedAttribute = self.listWidget.currentItem().text()
        self.result = True
        self.callback()
        self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "ViewAttributesWindow", "Select attributes"))

    def importData(self, data: pd.DataFrame):
        self.data = data
        columns = self.data.columns.tolist()
        self.listWidget.addItems(columns)
