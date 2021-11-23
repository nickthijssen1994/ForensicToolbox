from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class ContentWidget(QWidget):
    title = "Content"

    def __init__(self, parent):
        super(ContentWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.outputField = QTextEdit()
        self.outputField.setReadOnly(True)
        self.layout.addWidget(self.outputField)

    def analyze_file(self, file):
        try:
            f = open(file, 'r')
            data = f.read()
            f.close()
            self.outputField.setText(data)
        except:
            self.outputField.setText('Could Not Read File Content')

    def clear_file(self):
        self.outputField.clear()
