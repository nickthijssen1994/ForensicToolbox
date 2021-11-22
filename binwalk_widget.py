import os

from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class BinwalkWidget(QWidget):
    title = "Binwalk"

    def __init__(self, parent):
        super(BinwalkWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTextEdit()
        self._fileContent.setReadOnly(True)
        self.layout.addWidget(self._fileContent)

    def set_file(self, file):
        try:
            stream = os.popen('binwalk ' + file)
            output = stream.read()
            self._fileContent.setText(output)
        except:
            self._fileContent.setText('Could Not Read File Content')

    def clear_file(self):
        self._fileContent.clear()
