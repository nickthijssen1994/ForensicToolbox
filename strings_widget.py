import os

from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class StringsWidget(QWidget):
    title = "Strings"

    def __init__(self, parent):
        super(StringsWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTextEdit()
        self._fileContent.setReadOnly(True)
        self.layout.addWidget(self._fileContent)

    def set_file(self, file):
        stream = os.popen('strings ' + file)
        output = stream.read()
        self._fileContent.setText(output)

    def clear_file(self):
        self._fileContent.clear()
