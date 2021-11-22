import sys
from PySide6.QtCore import QStandardPaths, Slot
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog,
                               QMainWindow, QTextEdit, QWidget, QVBoxLayout, QTabWidget, QPushButton)

from binwalk_widget import BinwalkWidget
from file_widget import FileWidget
from strings_widget import StringsWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        available_geometry = self.screen().availableGeometry()
        self.resize(available_geometry.width() / 3,
                    available_geometry.height() / 2)
        self.setWindowTitle("Forensic Toolbox")

        self._filePath = ""
        self._fileContent = QTextEdit()

        file_menu = self.menuBar().addMenu("&File")
        icon = QIcon.fromTheme("document-open")
        open_action = QAction(icon, "&Open", self,
                              shortcut=QKeySequence.Open, triggered=self.open)
        file_menu.addAction(open_action)
        icon = QIcon.fromTheme("application-exit")
        exit_action = QAction(icon, "E&xit", self,
                              shortcut="Ctrl+Q", triggered=self.close)
        file_menu.addAction(exit_action)

        self.tabsWidget = TabsWidget(self)
        self.setCentralWidget(self.tabsWidget)

        self.show()

    def closeEvent(self, event):
        event.accept()

    @Slot()
    def open(self):
        file_dialog = QFileDialog(self)
        home_location = QStandardPaths.writableLocation(QStandardPaths.HomeLocation)
        file_dialog.setDirectory(home_location)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedFiles()[0]
            self._filePath = url

            f = open(url, 'r')
            with f:
                data = f.read()
                self._fileContent.setText(data)

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)


class TabsWidget(QWidget):

    def __init__(self, parent):
        super(TabsWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.binwalkWidget = BinwalkWidget(self)
        self.stringsWidget = StringsWidget(self)
        self.fileWidget = FileWidget(self)
        self.tabs.resize(300, 200)

        self.tabs.addTab(self.binwalkWidget, "Binwalk")
        self.tabs.addTab(self.stringsWidget, "Strings")
        self.tabs.addTab(self.fileWidget, "File")

        self.layout.addWidget(self.tabs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec())
