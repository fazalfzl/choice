import os
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from common_support.WeightInput import WeightThread
from common_support.print_bill import PrintBillThread
from common_support.product_options import UI_product_options
from common_support.rec_thread import RecognitionThread
from common_support.setup_labels import UI_setup_labels
from common_support.ui.UI import Ui_Form
from common_support.utils import get_product_details_by_plu
from util_application import initialize_window_layout, update_weight_input, calculate_total, setTable, add_to_bill, \
    clear_bill

version = 0

path_to_dir = os.getcwd()
os.environ["lazafron_version"] = str(version)
os.environ["lazafron_pathtodir"] = path_to_dir


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


        self.PB_left_arrow.clicked.connect(lambda: self.open_products)
        # endregion

        self.initialize_window()

    def open_products(self):
        pass

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
