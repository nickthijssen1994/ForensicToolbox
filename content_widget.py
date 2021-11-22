from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class ContentWidget(QWidget):
    title = "Content"

    def __init__(self, parent):
        super(ContentWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTextEdit()
        self.layout.addWidget(self._fileContent)

    def set_file(self, file):
        f = open(file, 'rb')
        with f:
            try:
                data = f.read()
                data = data.decode('utf-8')
                self._fileContent.setPlainText(data)
            except:
                self._fileContent.setPlainText('Could Not Read File Content')
