import os
import subprocess

from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class ReadElfWidget(QWidget):
    title = "ReadElf"

    def __init__(self, parent):
        super(ReadElfWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTextEdit()
        self._fileContent.setReadOnly(True)
        self.layout.addWidget(self._fileContent)

    def set_file(self, file):
        ssh = subprocess.Popen(["readelf", "-h", file],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True,
                               bufsize=0)
        for line in ssh.stdout:
            self._fileContent.append(line.strip())
        # try:
        #     stream = os.popen('readelf -h' + file)
        #     output = stream.read()
        #     self._fileContent.setText(output)
        # except:
        #     self._fileContent.setText('Could Not Read File Content')

    def clear_file(self):
        self._fileContent.clear()
