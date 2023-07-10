from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from common_support.ui.product_options import Ui_Form
from common_support.utils import filter_list, get_product_name_list, Config, get_product_details_by_name


class UI_product_options(QWidget, Ui_Form):
    def __init__(self, label="", add_product_to_current_table=None):
        super(UI_product_options, self).__init__()
        self.config = Config()
        self.ai_products_dpath = self.config.get('ai_products_dpath')

        self.setupUi(self)
        self.label.setText(label)

        self.product_name_list = get_product_name_list()

        self.add_product_to_current_table=add_product_to_current_table


        products= filter_list(strings=self.product_name_list,search_text=label)

        for product in products:
            btn:QPushButton=QPushButton(self)
            btn.setFixedSize(100,100)
            product_details_by_name = get_product_details_by_name(product)
            price=product_details_by_name['price']
            btn.setText(product+price)
            btn.setStyleSheet(f"border-image: url('{self.ai_products_dpath}/{product}.gif');")
            self.SAWC.layout().addWidget(btn)
            btn.clicked.connect(self.product_clicked)


    def product_clicked(self):
        btn: QPushButton = self.sender()
        if self.add_product_to_current_table :
            self.add_product_to_current_table(btn.text())



