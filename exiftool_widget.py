import os

from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class ExifToolWidget(QWidget):
    title = "ExifTool"

    def __init__(self, parent):
        super(ExifToolWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTextEdit()
        self._fileContent.acceptRichText()
        self.layout.addWidget(self._fileContent)

    def set_file(self, file):
        stream = os.popen('exiftool ' + file)
        output = stream.read()
        self._fileContent.setText(output)
