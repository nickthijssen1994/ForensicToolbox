import os

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit


class FileWidget(QWidget):
    title = "File"

    def __init__(self, parent):
        super(FileWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTextEdit()
        self.layout.addWidget(self._fileContent)

    def set_file(self, file):
        stream = os.popen('file ' + file)
        output = stream.read()
        self._fileContent.setPlainText(output)
