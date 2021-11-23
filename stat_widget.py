import os

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit


class StatWidget(QWidget):
    title = "Stat"

    def __init__(self, parent):
        super(StatWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.outputField = QTextEdit()
        self.outputField.setReadOnly(True)
        self.layout.addWidget(self.outputField)

    def analyze_file(self, file):
        try:
            stream = os.popen('stat ' + file)
            output = stream.read()
            self.outputField.setText(output)
        except:
            self.outputField.setText('Could Not Read File Content')

    def clear_file(self):
        self.outputField.clear()
