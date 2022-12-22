from ui import form
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from avito_scrap import *
from time import sleep

# workder for QThread
class Parse_Worker(QObject):
    finished = pyqtSignal()

    def run(self):
        self.all_products = get_all_products(self.source)
        self.parsed_products = parse_products_to_objects(self.all_products, self.avito_url)
        self.finished.emit()

class Root(QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        self._translate = QtCore.QCoreApplication.translate
        super().__init__()
        self.setupUi(self)
        self.show()
        self.parse_button.clicked.connect(lambda: self.change_status("Downloading..."))
        self.parse_button.clicked.connect(lambda: self.parse_button_push())
        self.clear_table_button.clicked.connect(lambda: self.clear_table_button_push())
        self.most_cheap_button.clicked.connect(lambda: self.most_cheap_button_push())


    def clear_table_button_push(self):
        self.data_table.setRowCount(0)


    def most_cheap_button_push(self):
        most_low_price = get_most_cheap_product(self.parsed_products).price  
        self.data_table.sortItems(1)   
        first_price_item = self.data_table.item(0, 1)
        for row in range(0, self.data_table.rowCount()):
            self.data_table.item(row, 1).setSelected(False)
        first_price_item.setSelected(True)

    def change_status(self, new_status):
        self.status_label.setText(new_status)


    def parse_button_push(self):
        self.product = self.product_lineedit.text()
        self.place = self.region_lineedit.text()
        self.avito_url = self.avito_url = "https://www.avito.ru"
        self.source = f"{self.avito_url}/{self.place}?q={self.product}".replace(" ", "+") 


        self.change_status("Downloading...")
        self.thread = QThread()
        self.parse_worker = Parse_Worker()
        self.parse_worker.moveToThread(self.thread)
        self.parse_worker.product = self.product
        self.parse_worker.place = self.place
        self.parse_worker.avito_url = self.avito_url
        self.parse_worker.source = self.source
        self.thread.started.connect(self.parse_worker.run)
        self.parse_worker.finished.connect(self.thread.quit)
        self.parse_worker.finished.connect(self.parse_worker.deleteLater)
        self.parse_worker.finished.connect(self.upload_table)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

        self.parse_button.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.parse_button.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.status_label.setText("Ready to use")
        )


    def upload_table(self):
        self.all_products = self.parse_worker.all_products
        self.parsed_products = self.parse_worker.parsed_products

        # generate rows from len(products)
        self.data_table.setRowCount(len(self.parsed_products))
        for product, row in zip(self.parsed_products, list(range(0, len(self.parsed_products)))):
            # column
            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", product.title))
            self.data_table.setItem(row, 0, item)

            item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole, product.price)
            self.data_table.setItem(row, 1, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(self._translate("MainWindow", product.href))
            self.data_table.setItem(row, 2, item)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Root()
    sys.exit(app.exec_())