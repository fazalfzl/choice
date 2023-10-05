import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

from common_support.ui.product_options import Ui_Form
from common_support.utils import filter_list, get_product_name_list, Config, get_product_details_by_name


class UI_product_options(QWidget, Ui_Form):
    def __init__(self, ai_label="", add_product_to_current_table=None):
        super(UI_product_options, self).__init__()
        self.config = Config()
        self.products_dpath = self.config.get('products_dpath')
        self.ai_images_dpath = self.config.get('ai_images_dpath')

        self.setupUi(self)
        self.label.setText(ai_label)
        self.product_name_list = get_product_name_list()
        self.add_product_to_current_table=add_product_to_current_table
        products= filter_list(strings=self.product_name_list, search_text=ai_label)



        for i, product in enumerate(products):
            row = i // 4
            col = i % 4

        # for product in products:
            container = QWidget(self)
            layout = QVBoxLayout(container)
            btn:QPushButton=QPushButton(self)
            btn.setFixedSize(100,100)
            container.setFixedSize(140,140)
            btn.product=product
            btn.clicked.connect(self.product_clicked)

            prod_image_gif_file_path = f"{self.products_dpath}/{product}.gif"

            if not os.path.exists(prod_image_gif_file_path):
                prod_image_gif_file_path = f"{self.ai_images_dpath}/{ai_label}.gif"
            # print(prod_image_gif_file_path)
            btn.setStyleSheet(f"border-image: url('{prod_image_gif_file_path}');")

            qlabel = QLabel(container)
            product_details_by_name = get_product_details_by_name(product)
            price = product_details_by_name['price']
            qlabel.setText(f"{product} - {price}")
            qlabel.setAlignment(Qt.AlignCenter)
            layout.addWidget(btn)
            layout.addWidget(qlabel)
            self.SAWC.layout().addWidget(container, row, col)

        self.show()

        if len(products) == 1:
            self.add_product_to_current_table(products[0])
            self.close()

    def product_clicked(self):
        btn: QPushButton = self.sender()
        try:
            if self.add_product_to_current_table :
                self.add_product_to_current_table(btn.product)
                self.close()
        except Exception as e:
            print(e)



