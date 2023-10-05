import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QTableWidget, QAbstractItemView

from common_support.utils import Config, get_product_name_list, get_product_details_by_name


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
        for i, product in enumerate(product_name_list):
            row = i // 4
            col = i % 4
        # for index, product in enumerate(product_name_list):
            container = QWidget(main_window_object)
            layout.addWidget(container,row,col)

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
