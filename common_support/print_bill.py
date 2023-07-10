from PyQt5 import QtPrintSupport, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidget

from common_support.image_gen import generate_bill


def print_bill(widget: QTableWidget):
    def print_file(image_png="bill.png"):
        printer = QtPrintSupport.QPrinter()
        printer.setPageMargins(0, 0, 0, 0, QtPrintSupport.QPrinter.Millimeter)
        printer.setFullPage(True)
        pixmap = QPixmap(image_png)
        painter = QtGui.QPainter()
        painter.begin(printer)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

    def table_to_list(tablewidget):
        rows = tablewidget.rowCount()
        columns = tablewidget.columnCount()
        header_labels = []
        for col in range(columns):
            item = tablewidget.horizontalHeaderItem(col)
            if item is not None:
                header_labels.append(item.text())
            else:
                header_labels.append("")

        # Create a list to store the table data
        table_data = []

        # Populate the list with the table data
        for row in range(rows):
            row_data = []
            for col in range(columns):
                item = tablewidget.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            table_data.append(row_data)

        return table_data



    try:
        data = table_to_list(widget)
        generate_bill(data)
        print_file(image_png="bill.png")
    except Exception as e:
        print("test printing", e)



class PrintBillThread(QThread):
    finished = pyqtSignal()  # Signal to indicate that the thread has finished

    def __init__(self, widget):
        super(PrintBillThread, self).__init__()
        self.widget = widget

    def run(self):
        print_bill(self.widget)
        self.finished.emit()