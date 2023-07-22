from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QCalendarWidget

from PyQt6.QtGui import QPalette, QTextCharFormat
from PyQt6.QtCore import Qt
from datetime import datetime
import numpy as np

from sport_activities_features_gui.models.user import User


class Ui_CalendarWidget(QWidget):
    globalUser: User

    def __init__(self):
        super().__init__()
        self.setObjectName("calendarWidget")
        self.resize(800, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = QCalendarWidget(self.gridLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.begin_date = None
        self.end_date = None

        self.highlight_format = QTextCharFormat()
        self.highlight_format.setBackground(self.palette().brush(QPalette.ColorRole.Highlight))
        self.highlight_format.setForeground(self.palette().color(QPalette.ColorRole.HighlightedText))

        # self.calendarWidget.clicked.connect(self.date_is_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    # IMPORT GLOBAL USER
    def importGlobalUser(self, user):
        self.globalUser = user
        self.setup()

    def highlightDates(self):
        if 'start_time' in self.globalUser.data:
            for date in self.globalUser.data['start_time'].unique():
                self.calendarWidget.setDateTextFormat(self.toDatetime(date), self.highlight_format)
        else:
            print('No dates to highlight')

    def toDatetime(self, date):
        """
        Converts a numpy datetime64 object to a python datetime object
        Input:
        date - a np.datetime64 object
        Output:
        DATE - a python datetime object
        """

        if date is not None and str(date) != str(np.datetime64('NaT')):
            timestamp = ((date - np.datetime64('1970-01-01T00:00:00'))
                         / np.timedelta64(1, 's'))
            return datetime.utcfromtimestamp(timestamp)
        else:
            return datetime.now()

    def setup(self):
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.NoSelection)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.DayOfWeek.Monday)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.highlightDates()
