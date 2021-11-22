from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class ContentWidget(QWidget):
    title = "Content"

    def __init__(self, parent):
        super(ContentWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTextEdit()
        self._fileContent.setReadOnly(True)
        self.layout.addWidget(self._fileContent)

    def set_file(self, file):
        try:
            f = open(file, 'r')
            data = f.read()
            f.close()
            self._fileContent.setText(data)
        except:
            self._fileContent.setText('Could Not Read File Content')

    def clear_file(self):
        self._fileContent.clear()
