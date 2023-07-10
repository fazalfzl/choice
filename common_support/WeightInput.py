import serial
from PyQt5.QtCore import QThread, pyqtSignal



class WeightThread(QThread):
    weight = pyqtSignal(str)
    finished = pyqtSignal()
    stopped = pyqtSignal()

    def stop(self):
        self.stopped.emit()

    def __init__(self):
        super().__init__()
    def run(self, best_of_three=False):
        last_weight_value = ""
        list_of_last_values = ["", "", ""]

        try:
            serial_port = serial.Serial('COM3', 2400)
            print(serial_port)
            if serial_port is None:
                return
        except:
            print("no serial port")
            return

        while True:
            try:
                serial_port_read = serial_port.read()
                if serial_port_read == b'[':
                    try:
                        command = serial_port.read(size=8).decode('utf-8').strip()[:-2]

                        if not command.isnumeric():
                            continue
                        command = float(command) / 1000
                        if command > 19:
                            continue
                        weight_value = f'{command:.3f}'

                        if not best_of_three:
                            self.weight.emit(weight_value)
                        else:
                            list_of_last_values.append(weight_value)
                            if len(list_of_last_values) >= 3 and all(
                                    val == list_of_last_values[-1] for val in list_of_last_values[-3:]):
                                if weight_value == last_weight_value:
                                    continue
                                self.weight.emit(weight_value)
                                last_weight_value = weight_value
                                list_of_last_values = ["", "", ""]

                    except Exception as e:
                        print("WEIGHT READING FAILED" + str(e))
                        continue
                    serial_port.flushInput()
            except Exception as e:
                print("exception in weight serial port" + str(e))
                serial_port.close()
                return
