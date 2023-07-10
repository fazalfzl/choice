
import os
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QAbstractItemView

from common_support.WeightInput import WeightThread
from common_support.print_bill import print_bill, PrintBillThread
from common_support.product_options import UI_product_options
from common_support.rec_thread import RecognitionThread
from common_support.setup_labels import UI_setup_labels
from common_support.ui.UI import Ui_Form
from common_support.utils import get_product_details_by_name, get_product_name_list, get_product_details_by_plu, Config

version = 0

path_to_dir = os.getcwd()
os.environ["lazafron_version"] = str(version)
os.environ["lazafron_pathtodir"] = path_to_dir




def setTable(table: QTableWidget):
    headers = ['ITEM', 'PRICE', 'QTY', 'AMOUNT']
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)

    # Set the table as read-only
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)


def add_to_bill(product_name, tablewidget, weight_input):
    product_details_by_name = get_product_details_by_name(name=product_name)

    if tablewidget is not None:
        row_count = tablewidget.rowCount()
        name_text = str(product_details_by_name["name"])
        price_text = str(product_details_by_name["price"])
        unit = product_details_by_name["unit"]
        qty_text = str(weight_input if unit == 'KG' else "1")
        amount = float(product_details_by_name["price"]) * float(qty_text)
        amount = round(amount, 2)
        amount_text = str(amount)

        # Check if the product is already present in the table
        for row in range(row_count):
            item = tablewidget.item(row, 0)  # Assuming product name is stored in the first column
            if item is not None and item.text() == name_text:
                qty_item = tablewidget.item(row, 2)  # Assuming quantity is stored in the third column
                if qty_item is not None:
                    current_qty = float(qty_item.text())
                    new_qty = current_qty + float(qty_text)
                    qty_text = str(round(new_qty, 3))
                    amount = float(price_text) * new_qty
                    amount = round(amount, 2)
                    amount_text = str(amount)

                    # Update the quantity and amount in the table
                    qty_item.setText(qty_text)
                    amount_item = tablewidget.item(row, 3)  # Assuming amount is stored in the fourth column
                    if amount_item is not None:
                        amount_item.setText(amount_text)

                return

        # Product is not present in the table, add a new row
        tablewidget.insertRow(row_count)
        name = QtWidgets.QTableWidgetItem(name_text)
        price = QtWidgets.QTableWidgetItem(price_text)
        qty = QtWidgets.QTableWidgetItem(qty_text)
        amount = QtWidgets.QTableWidgetItem(amount_text)

        font = QtGui.QFont()
        font.setBold(True)
        name.setFont(font)
        price.setFont(font)
        qty.setFont(font)
        amount.setFont(font)

        tablewidget.setItem(row_count, 0, name)
        tablewidget.setItem(row_count, 1, price)
        tablewidget.setItem(row_count, 2, qty)
        tablewidget.setItem(row_count, 3, amount)


class UI(QWidget, Ui_Form):

    def __init__(self):
        super(UI, self).__init__()
        self.config = Config()
        self.ai_images_dpath = self.config.get('ai_images_dpath')

        self.ui_product_options = None
        self.setup_labels_window = None

        self.setupUi(self)
        self._weight = None
        # Start the recognition thread

        setTable(self.tableC1)
        setTable(self.tableC2)
        setTable(self.tableC3)

        self.PB_setup_labels.clicked.connect(self.show_setup_labels)

        self.PB_print.clicked.connect(self.print_bill)

        for i, btn in enumerate([self.btn1, self.btn2, self.btn3, self.btn4]):
            btn.clicked.connect(self.show_product_options)

        try:
            self.product_name_list = get_product_name_list()

            for product_name in self.product_name_list:
                btn = QPushButton(self)
                btn.setText(product_name)
                self.SAWC_products.layout().addWidget(btn)
                btn.clicked.connect(self.product_clicked)
        except Exception as e:
            print(e)

        self.PB_weight_input.clicked.connect(lambda: self.weight_input_clicked(qty=""))

        self.PB_1.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "1"))
        self.PB_2.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "2"))
        self.PB_3.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "3"))
        self.PB_4.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "4"))
        self.PB_5.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "5"))
        self.PB_6.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "6"))
        self.PB_7.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "7"))
        self.PB_8.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "8"))
        self.PB_9.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "9"))
        self.PB_zero.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "0"))
        self.PB_dot.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "."))
        self.PB_clear.clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text()[:-1]))
        self.PB_empty.clicked.connect(lambda: self.lineEdit.setText(""))

        self.PB_plu.clicked.connect(self.search_by_plu)
        self.PB_qty.clicked.connect(lambda: self.weight_input_clicked(self.lineEdit.text()))

    def print_bill(self):
        self.PB_print.setEnabled(False)

        try:
            curr_index = self.tabWidget.currentIndex()
            tablewidget = None
            if curr_index == 0:
                tablewidget = self.tableC1
            if curr_index == 1:
                tablewidget = self.tableC2
            if curr_index == 2:
                tablewidget = self.tableC3

            # print_bill(tablewidget)

            self.thread = PrintBillThread(tablewidget)
            self.thread.finished.connect(lambda: self.PB_print.setEnabled(True))  # Enable PB_print after self.thread finishes
            self.thread.start()
        except Exception as e:
            print(e)

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value: pyqtSignal):
        self._weight = value
        self.weight.connect(self.set_weight)

    def set_weight(self, weight):
        self.PB_weight_input.setText(weight)

    def weight_input_clicked(self, qty=""):
        curr_index = self.tabWidget.currentIndex()
        tablewidget = None
        if curr_index == 0:
            tablewidget = self.tableC1
        if curr_index == 1:
            tablewidget = self.tableC2
        if curr_index == 2:
            tablewidget = self.tableC3

        row_count = tablewidget.rowCount()
        if row_count <= 0:
            return

        qty_item = tablewidget.item(row_count - 1, 2)
        price_item = tablewidget.item(row_count - 1, 1)
        amount_item = tablewidget.item(row_count - 1, 3)

        # qty_item.setText(self.PB_weight_input.text() if qty == "" else qty)
        qty_item.setText(self.PB_weight_input.text() if qty == "" else str(qty))

        amount = float(price_item.text()) * float(qty_item.text())
        amount = round(amount, 2)
        amount_text = str(amount)
        if amount_item is not None:
            amount_item.setText(amount_text)

    def product_clicked(self):
        btn: QPushButton = self.sender()
        self.add_product_to_current_table(btn.text())

    def search_by_plu(self):
        try:
            search_plu = self.lineEdit.text()
            self.lineEdit.setText("")
            product_details_by_plu = get_product_details_by_plu(search_plu)
            if not product_details_by_plu:
                return
            product_name = product_details_by_plu['name']
            self.add_product_to_current_table(product_name)
        except Exception as e:
            print(e)

    def show_product_options(self):
        try:
            btn: QPushButton = self.sender()
            label = btn.text()
            print(label)
            if self.ui_product_options:
                self.ui_product_options.close()
            self.ui_product_options = UI_product_options(label=label,
                                                         add_product_to_current_table=self.add_product_to_current_table)
            self.ui_product_options.show()
        except Exception as e:
            print(e)

    def add_product_to_current_table(self, product_name):

        try:
            curr_index = self.tabWidget.currentIndex()
            tablewidget = None
            if curr_index == 0:
                tablewidget = self.tableC1
            if curr_index == 1:
                tablewidget = self.tableC2
            if curr_index == 2:
                tablewidget = self.tableC3

            add_to_bill(product_name, tablewidget, weight_input=self.PB_weight_input.text())
        except Exception as e:
            print(e)

    def show_setup_labels(self):
        try:
            self.setup_labels_window = UI_setup_labels()
            self.setup_labels_window.setStyleSheet("""QScrollBar {\nwidth: 70px;\n}""")
            self.setup_labels_window.showMaximized()
        except Exception as e:
            print(e)

    @pyqtSlot(list)
    def update_labels(self, labels):
        try:
            self.labels = labels
            self.update_ui()
        except Exception as e:
            print(e)

    def update_ui(self):
        try:
            self.btn0.setStyleSheet("border-image: url('captured_image.jpg');")
            for i, btn in enumerate([self.btn1, self.btn2, self.btn3, self.btn4]):
                btn.setText(self.labels[i])
                btn.setStyleSheet(f"border-image: url('{self.ai_images_dpath}/{self.labels[i]}.gif');")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = UI()
    main_window.setStyleSheet("""QScrollBar {\nwidth: 70px;\n}""")

    main_window.showMaximized()

    try:
        recognition_thread = RecognitionThread()
        recognition_thread.start()
        recognition_thread.recognitionFinished.connect(main_window.update_labels)
    except Exception as e:
        print(e)

    try:
        weight_thread = WeightThread()
        weight_thread.start()
        weight_thread.stopped.connect(weight_thread.quit)
        main_window.weight = weight_thread.weight
    except Exception as e:
        print(e)


    sys.exit(app.exec_())
