from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class ContentWidget(QWidget):
    title = "Content"

    def __init__(self, parent):
        super(ContentWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTextEdit()
        self.layout.addWidget(self._fileContent)

    def set_file(self, file):
        f = open(file, 'r')
        data = f.read()
        with f:
            try:
                self._fileContent.setText(data)
            except:
                self._fileContent.setText('Could Not Read File Content')
