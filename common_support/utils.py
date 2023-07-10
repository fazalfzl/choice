import os
from PyQt5.QtWidgets import QTableWidgetItem, QLabel, QPushButton


class Config:
    def __init__(self, filepath="config.txt"):
        try:
            self.filepath = filepath
            if not os.path.exists(filepath):
                open(filepath, 'w').close()
        except Exception as e:
            print(e)

    def set(self, key, value):
        try:
            config = self.load_config()
            config[key] = value
            self.save_config(config)
        except Exception as e:
            print(e)

    def get(self, key):
        try:
            config = self.load_config()
            return config.get(key)
        except Exception as e:
            print(e)

    def load_config(self):
        config = {}
        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
            for line in lines:
                key, value = line.strip().split('=')
                config[key] = value
        except:
            pass
        return config

    def save_config(self, config):
        try:
            with open(self.filepath, 'w') as file:
                for key, value in config.items():
                    file.write(f"{key}={value}\n")
        except Exception as e:
            print(e)


def filter_list(strings, search_text):
    try:
        filtered_list = []
        search_text = search_text.lower()  # Convert search text to lowercase for case-insensitive comparison
        for string in strings:
            if string.lower().startswith(search_text):
                filtered_list.append(string)
        return filtered_list
    except Exception as e:
        print(e)


def load_labels():
    config = Config()
    labels_fpath = config.get('labels_fpath')
    try:
        return {i: line.strip() for i, line in enumerate(open(labels_fpath, 'r').readlines())}
    except Exception as e:
        print("exception in load labels" + str(e))


def update_label(old_label, new_label):
    try:
        config = Config()
        labels_fpath = config.get('labels_fpath')
        with open(labels_fpath, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.strip() == old_label:
                lines[i] = new_label + '\n'
                break

        with open(labels_fpath, 'w') as file:
            file.writelines(lines)

        print(f"Label '{old_label}' updated to '{new_label}' in the file '{labels_fpath}'.")
    except Exception as e:
        print("Exception occurred while updating label:", str(e))


def change_image_filename(old_filename, new_filename):
    try:
        config = Config()
        ai_images_dpath = config.get('ai_images_dpath')
        # Get the full paths of the old and new image files
        old_path = os.path.join(ai_images_dpath, old_filename + ".gif")
        new_path = os.path.join(ai_images_dpath, new_filename + ".gif")

        # Rename the image file
        os.rename(old_path, new_path)

        print(f"Image file '{old_filename}.gif' renamed to '{new_filename}.gif'.")
    except Exception as e:
        print("Exception occurred while changing image filename:", str(e))


def populate_table_with_csv(table_widget):
    try:
        config = Config()
        csv_file_path = config.get("csv_fpath")
        with open(csv_file_path, 'r') as file:
            lines = file.readlines()
            table_widget.setRowCount(len(lines))
            table_widget.setColumnCount(len(lines[0].split(',')))
            for row, line in enumerate(lines):
                items = line.split(',')
                for col, item in enumerate(items):
                    table_item = QTableWidgetItem(item.strip())
                    table_widget.setItem(row, col, table_item)
    except Exception as e:
        print(e)


def fill_grid(dict_index, layout, edit_button_clicked, label_, parent):
    try:
        config = Config()
        ai_images_dpath = config.get('ai_images_dpath')
        text = QLabel(parent)
        btn = QPushButton(parent)
        editbtn = QPushButton(parent)
        editbtn.setText('edit')
        editbtn.label = label_
        editbtn.clicked.connect(edit_button_clicked)
        btn.setFixedSize(60, 60)
        text.setText(label_)
        btn.setStyleSheet(f"border-image: url('{ai_images_dpath}/{label_}.gif');")
        layout.addWidget(text, dict_index, 0)
        layout.addWidget(btn, dict_index, 1)
        layout.addWidget(editbtn, dict_index, 2)
    except Exception as e:
        print(e)


def get_product_name_list():
    try:
        config = Config()
        csv_file_path = config.get("csv_fpath")
        name_index = config.get("name_index")
        if name_index:
            product_name_list = []

            with open(csv_file_path, 'r') as file:
                lines = file.readlines()

            for line in lines:
                items = line.split(',')
                if len(items) >= int(name_index):
                    product_name = items[int(name_index) - 1].strip()
                    product_name_list.append(product_name)

            return product_name_list

        return []
    except Exception as e:
        print(e)


def get_product_details_by_name(name):
    try:
        config = Config()
        csv_file_path = config.get("csv_fpath")
        name_index = config.get("name_index")
        price_index = config.get("price_index")
        code_index = config.get("code_index")
        unit_index = config.get("unit_index")
        plu_index = config.get("plu_index")
        if name_index and price_index and code_index and unit_index:

            with open(csv_file_path, 'r') as file:
                lines = file.readlines()

            for line in lines:
                items = line.split(',')
                if len(items) >= int(name_index):
                    product_name = items[int(name_index) - 1].strip()

                    if product_name == name:
                        return {
                            "name": items[int(name_index) - 1].strip(),
                            "price": items[int(price_index) - 1].strip(),
                            "code": items[int(code_index) - 1].strip(),
                            "unit": items[int(unit_index) - 1].strip(),
                            "plu": items[int(plu_index) - 1].strip(),
                        }
            return None
    except Exception as e:
        print(e)


def get_product_details_by_plu(plu):
    try:
        config = Config()
        csv_file_path = config.get("csv_fpath")
        name_index = config.get("name_index")
        price_index = config.get("price_index")
        code_index = config.get("code_index")
        unit_index = config.get("unit_index")
        plu_index = config.get("plu_index")
        if name_index and price_index and code_index and unit_index:

            with open(csv_file_path, 'r') as file:
                lines = file.readlines()

            for line in lines:
                items = line.split(',')
                if len(items) >= int(name_index):
                    product_plu = items[int(plu_index) - 1].strip()

                    if product_plu == plu:
                        return {
                            "name": items[int(name_index) - 1].strip(),
                            "price": items[int(price_index) - 1].strip(),
                            "code": items[int(code_index) - 1].strip(),
                            "unit": items[int(unit_index) - 1].strip(),
                            "plu": items[int(plu_index) - 1].strip(),
                        }

            return None
    except Exception as e:
        print(e)
