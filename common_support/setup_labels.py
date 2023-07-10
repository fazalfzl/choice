import subprocess
import sys
import threading

from PyQt5.QtWidgets import QWidget, QLabel, QFileDialog, QFormLayout, QPushButton, QLineEdit, QSpinBox

from common_support.ui.setup_labels import Ui_Form
from common_support.utils import filter_list, load_labels, update_label, change_image_filename, Config, \
    populate_table_with_csv, fill_grid, get_product_name_list

conf_list = ['csv_fpath', 'ai_images_dpath', 'labels_fpath', 'model_fpath',
             'name_index', 'price_index', 'code_index', 'unit_index', 'plu_index',
             'code_length', 'qty_length', 'first_char']


def update_from_github(repo_url="https://github.com/fazalfzl/choice.git"):
    temp_dir = "temp_clone"
    subprocess.run(["git", "clone", repo_url, temp_dir], shell=True)
    subprocess.run(["xcopy", temp_dir, ".", "/E", "/H", "/C", "/I", "/Y"])
    subprocess.run(["rd", "/S", "/Q", temp_dir], shell=True)

    # Restart the application
    python_executable = sys.executable
    subprocess.Popen([python_executable] + sys.argv)
    sys.exit(0)


def check_for_update():
    down = threading.Thread(name='scanning', target=lambda: update_from_github())
    down.start()







class UI_setup_labels(QWidget, Ui_Form):
    def __init__(self):
        super(UI_setup_labels, self).__init__()
        self.config = Config()
        self.setupUi(self)
        self._product_name_list = []
        self.reload_grid()
        self.PB_change_label.clicked.connect(self.update_btn_clicked)

        self.conf_list = []
        form_layout = self.SAWC_conf_form.layout()

        self.PB_check_updates.clicked.connect(lambda :check_for_update())

        try:
            for conf in conf_list:
                if "path" in conf:
                    view = QPushButton(self)
                    view.clicked.connect(self.conf_updation)
                elif 'char' in conf:
                    view = QLineEdit(self)
                    view.textChanged.connect(self.conf_updation)
                else:
                    view = QSpinBox(self)
                    view.valueChanged.connect(self.conf_updation)

                view.conf = conf
                init_config = self.config.get(conf)
                if type(view) == QSpinBox:
                    view.setValue(int(init_config if init_config else 0))
                else:
                    view.setText(init_config if init_config else "")

                form_layout.addRow(conf, view)
        except Exception as e:
            print(e)

        self.show_table()

    def conf_updation(self):
        try:
            view: QPushButton or QSpinBox or QLineEdit = self.sender()
            print(view.conf)
            conf = view.conf
            if 'fpath' in conf:
                file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
                if file_path:
                    view.setText(file_path)
                    self.config.set(conf, file_path)
            elif 'dpath' in conf:
                dir_path = QFileDialog.getExistingDirectory(self, "Select Directory")
                if dir_path:
                    view.setText(dir_path)
                    self.config.set(conf, dir_path)
            else:
                self.config.set(conf, view.text())
        except Exception as e:
            print(e)

    @property
    def product_name_list(self):
        return self._product_name_list

    @product_name_list.setter
    def product_name_list(self, value):
        try:
            self._product_name_list = value

            if len(self._product_name_list) == 0:
                return

            for dict_index, label_ in self.labels.items():
                filterd_list = filter_list(self._product_name_list, search_text=label_)
                text = QLabel(self)
                text.setText(str(filterd_list))
                self.widget.layout().addWidget(text, dict_index, 3)
        except Exception as e:
            print(e)

    def show_table(self):
        try:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            populate_table_with_csv(table_widget=self.tableWidget)
            self.product_name_list = get_product_name_list()
        except Exception as e:
            print(e)

    def reload_grid(self):
        try:
            self.widget_2.setDisabled(True)
            self.labels = load_labels()

            # Clear the existing widgets from the layout
            layout = self.widget.layout()
            while layout.count() > 0:
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            for dict_index in self.labels:
                fill_grid(dict_index=dict_index,
                          layout=layout,
                          edit_button_clicked=self.edit_button_clicked,
                          label_=self.labels[dict_index],
                          parent=self
                          )
        except Exception as e:
            print(e)

    def edit_button_clicked(self):
        try:
            btn = self.sender()
            print(btn.label)
            self.to_lineEdit.setText(btn.label)
            self.from_label.setText(btn.label)
            self.widget_2.setEnabled(True)
        except Exception as e:
            print(e)

    def update_btn_clicked(self):
        try:
            from_label = self.from_label.text()
            to_label = self.to_lineEdit.text()
            if len(to_label) > 0 and from_label != to_label:
                print(f"changing {from_label} to {to_label}")
                update_label(old_label=from_label, new_label=to_label)
                change_image_filename(old_filename=from_label, new_filename=to_label)
            self.reload_grid()
        except Exception as e:
            print(e)
