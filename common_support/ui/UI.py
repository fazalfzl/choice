# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mhdfa\OneDrive\Desktop\AI\choice\common_support\ui\UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1167, 654)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("QPushButton {    width: 80px; height: 80px;}")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.btn2 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setText("")
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 0, 0, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setText("")
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 0, 1, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setText("")
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setObjectName("btn1")
        self.gridLayout_2.addWidget(self.btn1, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 180))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 180))
        self.scrollArea.setStyleSheet("QScrollBar {\n"
"width: 80px;\n"
"height: 50px;\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.SAWC_products = QtWidgets.QWidget()
        self.SAWC_products.setGeometry(QtCore.QRect(0, 0, 562, 128))
        self.SAWC_products.setObjectName("SAWC_products")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.SAWC_products)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea.setWidget(self.SAWC_products)
        self.gridLayout_2.addWidget(self.scrollArea, 2, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 3)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_3)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"    height: 30px;  /* Adjust the height of the tabs */\n"
"    width: 120px;  /* Adjust the width of the tabs */\n"
"    font-size: 16px;  /* Adjust the font size of the tabs */\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tabC1 = QtWidgets.QWidget()
        self.tabC1.setObjectName("tabC1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabC1)
        self.gridLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableC1 = QtWidgets.QTableWidget(self.tabC1)
        self.tableC1.setStyleSheet("QTableWidgetItem {\n"
"background-color: rgb(255, 255, 127);\n"
"}")
        self.tableC1.setObjectName("tableC1")
        self.tableC1.setColumnCount(0)
        self.tableC1.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableC1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabC1, "")
        self.tabC2 = QtWidgets.QWidget()
        self.tabC2.setObjectName("tabC2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tabC2)
        self.gridLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tableC2 = QtWidgets.QTableWidget(self.tabC2)
        self.tableC2.setObjectName("tableC2")
        self.tableC2.setColumnCount(0)
        self.tableC2.setRowCount(0)
        self.gridLayout_7.addWidget(self.tableC2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabC2, "")
        self.tabC3 = QtWidgets.QWidget()
        self.tabC3.setObjectName("tabC3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tabC3)
        self.gridLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tableC3 = QtWidgets.QTableWidget(self.tabC3)
        self.tableC3.setObjectName("tableC3")
        self.tableC3.setColumnCount(0)
        self.tableC3.setRowCount(0)
        self.gridLayout_8.addWidget(self.tableC3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabC3, "")
        self.tab_feed = QtWidgets.QWidget()
        self.tab_feed.setObjectName("tab_feed")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_feed)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn0 = QtWidgets.QPushButton(self.tab_feed)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy)
        self.btn0.setMaximumSize(QtCore.QSize(150, 150))
        self.btn0.setText("")
        self.btn0.setObjectName("btn0")
        self.gridLayout_4.addWidget(self.btn0, 0, 0, 1, 1)
        self.PB_setup_labels = QtWidgets.QPushButton(self.tab_feed)
        self.PB_setup_labels.setObjectName("PB_setup_labels")
        self.gridLayout_4.addWidget(self.PB_setup_labels, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_feed, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setStyleSheet("QPushButton {    width: 50px; height: 50px;\n"
"background-color: rgb(0, 255, 255);\n"
"color: rgb(0, 85, 0);\n"
"    font: 75 24pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.PB_1 = QtWidgets.QPushButton(self.widget_7)
        self.PB_1.setObjectName("PB_1")
        self.gridLayout_11.addWidget(self.PB_1, 0, 0, 1, 1)
        self.PB_2 = QtWidgets.QPushButton(self.widget_7)
        self.PB_2.setObjectName("PB_2")
        self.gridLayout_11.addWidget(self.PB_2, 0, 1, 1, 1)
        self.PB_3 = QtWidgets.QPushButton(self.widget_7)
        self.PB_3.setObjectName("PB_3")
        self.gridLayout_11.addWidget(self.PB_3, 0, 2, 1, 1)
        self.PB_4 = QtWidgets.QPushButton(self.widget_7)
        self.PB_4.setObjectName("PB_4")
        self.gridLayout_11.addWidget(self.PB_4, 1, 0, 1, 1)
        self.PB_5 = QtWidgets.QPushButton(self.widget_7)
        self.PB_5.setObjectName("PB_5")
        self.gridLayout_11.addWidget(self.PB_5, 1, 1, 1, 1)
        self.PB_6 = QtWidgets.QPushButton(self.widget_7)
        self.PB_6.setObjectName("PB_6")
        self.gridLayout_11.addWidget(self.PB_6, 1, 2, 1, 1)
        self.PB_7 = QtWidgets.QPushButton(self.widget_7)
        self.PB_7.setObjectName("PB_7")
        self.gridLayout_11.addWidget(self.PB_7, 2, 0, 1, 1)
        self.PB_8 = QtWidgets.QPushButton(self.widget_7)
        self.PB_8.setObjectName("PB_8")
        self.gridLayout_11.addWidget(self.PB_8, 2, 1, 1, 1)
        self.PB_9 = QtWidgets.QPushButton(self.widget_7)
        self.PB_9.setObjectName("PB_9")
        self.gridLayout_11.addWidget(self.PB_9, 2, 2, 1, 1)
        self.PB_dot = QtWidgets.QPushButton(self.widget_7)
        self.PB_dot.setObjectName("PB_dot")
        self.gridLayout_11.addWidget(self.PB_dot, 3, 0, 1, 1)
        self.PB_zero = QtWidgets.QPushButton(self.widget_7)
        self.PB_zero.setObjectName("PB_zero")
        self.gridLayout_11.addWidget(self.PB_zero, 3, 1, 1, 1)
        self.PB_clear = QtWidgets.QPushButton(self.widget_7)
        self.PB_clear.setObjectName("PB_clear")
        self.gridLayout_11.addWidget(self.PB_clear, 3, 2, 1, 1)
        self.gridLayout_10.addWidget(self.widget_7, 1, 0, 1, 1)
        self.widget_8 = QtWidgets.QWidget(self.widget_5)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.PB_qty = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_qty.sizePolicy().hasHeightForWidth())
        self.PB_qty.setSizePolicy(sizePolicy)
        self.PB_qty.setObjectName("PB_qty")
        self.gridLayout_13.addWidget(self.PB_qty, 1, 0, 1, 1)
        self.PB_plu = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_plu.sizePolicy().hasHeightForWidth())
        self.PB_plu.setSizePolicy(sizePolicy)
        self.PB_plu.setObjectName("PB_plu")
        self.gridLayout_13.addWidget(self.PB_plu, 0, 0, 1, 1)
        self.PB_delete_row = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_delete_row.sizePolicy().hasHeightForWidth())
        self.PB_delete_row.setSizePolicy(sizePolicy)
        self.PB_delete_row.setObjectName("PB_delete_row")
        self.gridLayout_13.addWidget(self.PB_delete_row, 2, 0, 1, 1)
        self.gridLayout_10.addWidget(self.widget_8, 1, 1, 1, 1)
        self.gridLayout_9.addWidget(self.widget_5, 2, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_12.setContentsMargins(6, 0, 6, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.PB_print = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_print.sizePolicy().hasHeightForWidth())
        self.PB_print.setSizePolicy(sizePolicy)
        self.PB_print.setObjectName("PB_print")
        self.gridLayout_12.addWidget(self.PB_print, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.widget_6, 3, 0, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.widget_4)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_15.setContentsMargins(6, 0, 6, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.PB_empty = QtWidgets.QPushButton(self.widget_9)
        self.PB_empty.setObjectName("PB_empty")
        self.gridLayout_15.addWidget(self.PB_empty, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_15.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.PB_weight_input = QtWidgets.QPushButton(self.widget_9)
        self.PB_weight_input.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 14pt \"Wide Latin\";\n"
"color: rgb(255, 0, 0);")
        self.PB_weight_input.setObjectName("PB_weight_input")
        self.gridLayout_15.addWidget(self.PB_weight_input, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_9)
        self.label.setStyleSheet("font: 14pt \"Wide Latin\";")
        self.label.setObjectName("label")
        self.gridLayout_15.addWidget(self.label, 0, 3, 1, 1)
        self.label_total = QtWidgets.QLabel(self.widget_9)
        self.label_total.setStyleSheet("font: 14pt \"Wide Latin\";")
        self.label_total.setObjectName("label_total")
        self.gridLayout_15.addWidget(self.label_total, 0, 4, 1, 1)
        self.gridLayout_9.addWidget(self.widget_9, 1, 0, 1, 1)
        self.gridLayout_9.setRowStretch(0, 1)
        self.gridLayout_6.addWidget(self.widget_4, 1, 0, 1, 1)
        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_3.addWidget(self.widget_3, 0, 2, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn1.setText(_translate("Form", "***"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabC1), _translate("Form", "C1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabC2), _translate("Form", "C2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabC3), _translate("Form", "C3"))
        self.PB_setup_labels.setText(_translate("Form", "SETUP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_feed), _translate("Form", "feed"))
        self.PB_1.setText(_translate("Form", "1"))
        self.PB_2.setText(_translate("Form", "2"))
        self.PB_3.setText(_translate("Form", "3"))
        self.PB_4.setText(_translate("Form", "4"))
        self.PB_5.setText(_translate("Form", "5"))
        self.PB_6.setText(_translate("Form", "6"))
        self.PB_7.setText(_translate("Form", "7"))
        self.PB_8.setText(_translate("Form", "8"))
        self.PB_9.setText(_translate("Form", "9"))
        self.PB_dot.setText(_translate("Form", "."))
        self.PB_zero.setText(_translate("Form", "0"))
        self.PB_clear.setText(_translate("Form", "<="))
        self.PB_qty.setText(_translate("Form", "QTY"))
        self.PB_plu.setText(_translate("Form", "PLU"))
        self.PB_delete_row.setText(_translate("Form", "DELETE ROW"))
        self.PB_print.setText(_translate("Form", "PRINT"))
        self.PB_empty.setText(_translate("Form", "X"))
        self.PB_weight_input.setText(_translate("Form", "0.00"))
        self.label.setText(_translate("Form", "TOTAL :"))
        self.label_total.setText(_translate("Form", "0.00"))
