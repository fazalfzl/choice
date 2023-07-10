from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from common_support.ui.product_options import Ui_Form
from common_support.utils import filter_list, get_product_name_list


class UI_product_options(QWidget, Ui_Form):
    def __init__(self, label="", add_product_to_current_table=None):
        super(UI_product_options, self).__init__()
        self.setupUi(self)
        self.label.setText(label)

        self.product_name_list = get_product_name_list()

        self.add_product_to_current_table=add_product_to_current_table

        products= filter_list(strings=self.product_name_list,search_text=label)

        for product in products:
            btn=QPushButton(self)
            btn.setText(product)
            self.SAWC.layout().addWidget(btn)
            btn.clicked.connect(self.product_clicked)


    def product_clicked(self):
        btn: QPushButton = self.sender()
        if self.add_product_to_current_table :
            self.add_product_to_current_table(btn.text())



