
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt, QDate
from constructor import Ui_MainWindow
import sys
from datetime import date

row = 0


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(20)

        self.ui.tableWidget.setHorizontalHeaderLabels(('Дата', 'Название'))
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.calendarWidget.clicked.connect(self.on_click_calendar)

    def btnClicked(self):
        global row
        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(self.ui.calendarWidget.selectedDate().toString("dd.MM.yyyy")))
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(self.ui.textEdit.toPlainText()))
        row += 1

    def on_click_calendar(self):
        global start_day, calc_day
        calc_date = self.ui.calendarWidget.selectedDate()
        delta_days = start_date.daysTo(calc_date)
        if delta_days > 0:
            self.ui.label_3.setText("До тура будет %s дней!" % delta_days)
        else:
            self.ui.label_3.setText("Выберите более позднюю дату")
        self.ui.label_3.adjustSize()


start_date = QDate.currentDate()
calc_date = QDate.currentDate()



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
