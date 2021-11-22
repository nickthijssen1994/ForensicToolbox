import os

from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class ReadElfWidget(QWidget):
    title = "ReadElf"

    def __init__(self, parent):
        super(ReadElfWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTextEdit()
        self._fileContent.acceptRichText()
        self.layout.addWidget(self._fileContent)

    def set_file(self, file):
        stream = os.popen('readelf -h ' + file)
        output = stream.read()
        self._fileContent.setText(output)
