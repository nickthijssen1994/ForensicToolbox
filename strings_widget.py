import os

from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class StringsWidget(QWidget):
    title = "Strings"

    def __init__(self, parent):
        super(StringsWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.outputField = QTextEdit()
        self.outputField.setReadOnly(True)
        self.layout.addWidget(self.outputField)

    def analyze_file(self, file):
        try:
            stream = os.popen('strings ' + file)
            output = stream.read()
            self.outputField.setText(output)
        except:
            self.outputField.setText('Could Not Read File Content')

    def clear_file(self):
        self.outputField.clear()
