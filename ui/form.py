# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documents/py/avito_scraper/ui/form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 537)
        MainWindow.setStyleSheet("font: 9pt \"Monospace\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.parse_button = QtWidgets.QPushButton(self.centralwidget)
        self.parse_button.setGeometry(QtCore.QRect(200, 10, 80, 52))
        self.parse_button.setObjectName("parse_button")
        self.data_table = QtWidgets.QTableWidget(self.centralwidget)
        self.data_table.setGeometry(QtCore.QRect(20, 107, 661, 371))
        self.data_table.setShowGrid(True)
        self.data_table.setGridStyle(QtCore.Qt.SolidLine)
        self.data_table.setObjectName("data_table")
        self.data_table.setColumnCount(3)
        self.data_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(2, item)
        self.data_table.horizontalHeader().setVisible(True)
        self.data_table.horizontalHeader().setCascadingSectionResizes(False)
        self.data_table.horizontalHeader().setDefaultSectionSize(100)
        self.data_table.horizontalHeader().setHighlightSections(True)
        self.data_table.horizontalHeader().setMinimumSectionSize(25)
        self.data_table.horizontalHeader().setSortIndicatorShown(True)
        self.data_table.horizontalHeader().setStretchLastSection(True)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 179, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.product_label = QtWidgets.QLabel(self.layoutWidget)
        self.product_label.setObjectName("product_label")
        self.gridLayout.addWidget(self.product_label, 0, 0, 1, 1)
        self.product_lineedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.product_lineedit.setObjectName("product_lineedit")
        self.gridLayout.addWidget(self.product_lineedit, 0, 1, 1, 1)
        self.region_label = QtWidgets.QLabel(self.layoutWidget)
        self.region_label.setObjectName("region_label")
        self.gridLayout.addWidget(self.region_label, 1, 0, 1, 1)
        self.region_lineedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.region_lineedit.setObjectName("region_lineedit")
        self.gridLayout.addWidget(self.region_lineedit, 1, 1, 1, 1)
        self.clear_table_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_table_button.setGeometry(QtCore.QRect(591, 483, 91, 23))
        self.clear_table_button.setObjectName("clear_table_button")
        self.most_cheap_button = QtWidgets.QPushButton(self.centralwidget)
        self.most_cheap_button.setGeometry(QtCore.QRect(20, 483, 80, 23))
        self.most_cheap_button.setObjectName("most_cheap_button")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(20, 69, 261, 31))
        self.status_label.setStyleSheet("border: 1px solid rgba(0, 0, 0, 0.3);\n"
"border-radius: 6px;\n"
"font: 16px \"Monospace\";")
        self.status_label.setObjectName("status_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parse_button.setText(_translate("MainWindow", "Scrap"))
        self.data_table.setSortingEnabled(True)
        item = self.data_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.data_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.data_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Href"))
        self.product_label.setText(_translate("MainWindow", "Product"))
        self.region_label.setText(_translate("MainWindow", "Region"))
        self.clear_table_button.setText(_translate("MainWindow", "Clear table"))
        self.most_cheap_button.setText(_translate("MainWindow", "Most cheap"))
        self.status_label.setText(_translate("MainWindow", "Status: Ready to use"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
