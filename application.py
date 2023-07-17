import os
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QAbstractItemView, QVBoxLayout, QLabel

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


def initialize_window_layout(main_window_object):
    config = Config()
    ai_images_dpath = config.get('ai_images_dpath')
    products_dpath = config.get('products_dpath')
    try:
        product_name_list = get_product_name_list()
        products_with_file = [product for product in product_name_list if
                              any(file.startswith(product) for file in os.listdir(products_dpath))]
        product_name_list = sorted(product_name_list, key=lambda x: x not in products_with_file)

        layout = main_window_object.SAWC_products.layout()
        for index, product in enumerate(product_name_list):
            container = QWidget(main_window_object)
            layout.addWidget(container)

            btn = QPushButton(main_window_object)
            btn.setFixedSize(100, 100)
            container.setFixedSize(140, 140)
            btn.product = product
            btn.clicked.connect(main_window_object.product_clicked)

            files_with_prefix = [file for file in os.listdir(products_dpath) if file.startswith(product)]
            file_path = f"{products_dpath}/{files_with_prefix[0]}" if files_with_prefix else 'default_image.png'
            style = f"border-image: url('{file_path}');"
            btn.setStyleSheet(style)

            label = QLabel(container)
            product_details_by_name = get_product_details_by_name(product)
            price = product_details_by_name['price']
            label.setText(f"{product} - {price}")
            label.setAlignment(Qt.AlignCenter)

            inner_layout = QVBoxLayout(container)
            inner_layout.addWidget(btn)
            inner_layout.addWidget(label)

        return ai_images_dpath

    except Exception as e:
        print(e)


def update_weight_input(tablewidget, qty_item, price_item, amount_item, pb_weight_input):
    row_count = tablewidget.rowCount()
    if row_count <= 0:
        return

    selected_items = tablewidget.selectedItems()
    if selected_items:
        selected_row = selected_items[0].row()
    else:
        selected_row = row_count - 1

    qty = pb_weight_input.text() if not qty_item else str(pb_weight_input)

    qty_item.setText(qty)

    amount = float(price_item.text()) * float(qty_item.text())
    amount = round(amount, 2)
    amount_text = str(amount)
    if amount_item is not None:
        amount_item.setText(amount_text)


def calculate_total(tablewidget):
    if not tablewidget:
        return 0
    total_amount = 0
    rows = tablewidget.rowCount()
    for row in range(rows):
        item = tablewidget.item(row, 3)
        total_amount += float(item.text())
    return total_amount


def setTable(table: QTableWidget):
    config = Config()
    headers = ['ITEM', 'PRICE', 'QTY', 'AMOUNT']
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    table.setColumnWidth(0, int(config.get("bill_table_name_width") or 200))


def add_to_bill(product_name, tablewidget, weight_input):
    product_details_by_name = get_product_details_by_name(name=product_name)

    if tablewidget is not None:
        row_count = tablewidget.rowCount()
        name_text = str(product_details_by_name["name"])
        price_text = str(product_details_by_name["price"])
        unit = product_details_by_name["unit"]
        qty_text = str(weight_input if unit == ('KG' or '0') else "1")
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


def clear_bill(tablewidget=None):
    if not tablewidget:
        return
    tablewidget.clear()
    tablewidget.setRowCount(0)
    setTable(tablewidget)


class UI(QWidget, Ui_Form):

    def __init__(self):
        super(UI, self).__init__()
        self.product_name_list = None
        self.ai_images_dpath = None
        self.products_dpath = None

        self.ui_product_options = None
        self.setup_labels_window = None

        self.setupUi(self)
        self.showMaximized()

        # region EVENT CONNECTIONS

        self.PB_setup_labels.clicked.connect(self.show_setup_labels)
        self.PB_delete_row.clicked.connect(self.delete_row)
        self.PB_print.clicked.connect(self.print_bill)
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
        self.PB_qty.clicked.connect(
            lambda: self.weight_input_clicked(self.lineEdit.text()) or self.lineEdit.setText(""))
        self.tabWidget.currentChanged.connect(self.update_total)

        for i, btn in enumerate([self.btn1, self.btn2, self.btn3, self.btn4]):
            btn.clicked.connect(self.show_product_options)
        # endregion

        self.initialize_window()

    def initialize_window(self):
        setTable(self.tableC1)
        setTable(self.tableC2)
        setTable(self.tableC3)
        self.ai_images_dpath = initialize_window_layout(self)

    def print_bill(self):
        self.PB_print.setEnabled(False)
        try:
            tablewidget = self.get_current_table()
            if not tablewidget:
                return

                # print_bill(tablewidget)

            self.thread = PrintBillThread(tablewidget)
            self.thread.finished.connect(lambda: self.PB_print.setEnabled(
                True) or clear_bill(tablewidget=self.get_current_table()))  # Enable PB_print after self.thread finishes
            self.thread.start()
        except Exception as e:
            print(e)

    def update_total(self):
        self.label_total.setText(f"{calculate_total(self.get_current_table()) :.2f}")

    def weight_input_clicked(self, qty=""):
        tablewidget = self.get_current_table()
        if not tablewidget:
            return

        selected_row, qty_item, price_item, amount_item = self.get_selected_row_items(tablewidget)

        pb_weight_input = self.PB_weight_input.text() if qty == "" else str(qty)

        update_weight_input(tablewidget, qty_item, price_item, amount_item, pb_weight_input)

        self.update_total()

    def get_selected_row_items(self, tablewidget):
        row_count = tablewidget.rowCount()
        if row_count <= 0:
            return None, None, None, None

        selected_items = tablewidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
        else:
            selected_row = row_count - 1

        qty_item = tablewidget.item(selected_row, 2)
        price_item = tablewidget.item(selected_row, 1)
        amount_item = tablewidget.item(selected_row, 3)

        return selected_row, qty_item, price_item, amount_item

    def product_clicked(self):
        btn: QPushButton = self.sender()
        self.add_product_to_current_table(btn.product)

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
            self.ui_product_options = UI_product_options(ai_label=label,
                                                         add_product_to_current_table=self.add_product_to_current_table)

        except Exception as e:
            print(e)

    def add_product_to_current_table(self, product_name):

        try:
            tablewidget = self.get_current_table()
            if not tablewidget:
                return

            add_to_bill(product_name, tablewidget, weight_input=self.PB_weight_input.text())
            tablewidget.scrollToBottom()
            self.update_total()

        except Exception as e:
            print(e)

    def get_current_table(self):
        curr_index = self.tabWidget.currentIndex()
        if curr_index == 0:
            tablewidget = self.tableC1
        elif curr_index == 1:
            tablewidget = self.tableC2
        elif curr_index == 2:
            tablewidget = self.tableC3
        else:
            return False
        return tablewidget

    def show_setup_labels(self):
        try:
            self.setup_labels_window = UI_setup_labels()
            self.setup_labels_window.showMaximized()
            self.setup_labels_window.closeEvent = lambda event: self.initialize_window()
        except Exception as e:
            print(e)

    @pyqtSlot(str)
    def set_weight(self, weight):
        self.PB_weight_input.setText(weight)

    @pyqtSlot(list)
    def update_labels(self, labels):
        try:
            self.update_ui(labels)
        except Exception as e:
            print(e)

    def update_ui(self, labels=["", "", "", ""]):
        try:
            self.btn0.setStyleSheet("border-image: url('captured_image.jpg');")
            prediction_buttons = self.get_prediction_buttons()
            for i, btn in enumerate(prediction_buttons):
                btn.setText(labels[i])
                btn.setStyleSheet(f"border-image: url('{self.ai_images_dpath}/{labels[i]}.gif');")
        except Exception as e:
            print(e)

    def get_prediction_buttons(self):
        prediction_buttons = [self.btn1, self.btn2, self.btn3, self.btn4]
        return prediction_buttons

    def delete_row(self):
        tablewidget = self.get_current_table()
        if not tablewidget:
            return

        selected_items = tablewidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            tablewidget.removeRow(selected_row)
        else:
            tablewidget.removeRow(tablewidget.rowCount() - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = UI()
    try:
        recognition_thread = RecognitionThread()
        recognition_thread.start()
        recognition_thread.recognitionFinished.connect(main_window.update_labels)
    except Exception as e:
        print(e)

    try:
        weight_thread = WeightThread()
        weight_thread.start()
        weight_thread.weight.connect(main_window.set_weight)
        weight_thread.stopped.connect(weight_thread.quit)
    except Exception as e:
        print(e)

    sys.exit(app.exec_())
