import sys

from PySide6.QtCore import QStandardPaths, Slot
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog,
                               QMainWindow, QWidget, QVBoxLayout, QTabWidget)

from binwalk_widget import BinwalkWidget
from content_widget import ContentWidget
from exiftool_widget import ExifToolWidget
from file_widget import FileWidget
from hash_widget import HashWidget
from libraries_widget import LibrariesWidget
from readelf_widget import ReadElfWidget
from stat_widget import StatWidget
from strings_widget import StringsWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        available_geometry = self.screen().availableGeometry()
        self.resize((available_geometry.width() / 3) * 2,
                    (available_geometry.height() / 4) * 3)
        self.setWindowTitle("Forensic Toolbox")

        self._filePath = ""

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
        self.tabsWidget.analyze_file('example.txt')

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
            self.tabsWidget.analyze_file(url)

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)


class TabsWidget(QWidget):

    def __init__(self, parent):
        super(TabsWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.widgets = []
        self.widgets.append(ContentWidget(self))
        self.widgets.append(FileWidget(self))
        self.widgets.append(StatWidget(self))
        self.widgets.append(HashWidget(self))
        self.widgets.append(ExifToolWidget(self))
        self.widgets.append(BinwalkWidget(self))
        self.widgets.append(StringsWidget(self))
        self.widgets.append(ReadElfWidget(self))
        self.widgets.append(LibrariesWidget(self))
        for widget in self.widgets:
            self.tabs.addTab(widget, widget.title)

        self.layout.addWidget(self.tabs)

    def analyze_file(self, file):
        self.clear_file()
        for widget in self.widgets:
            try:
                widget.analyze_file(file)
            except:
                print("Could Not Read File")

    def clear_file(self):
        for widget in self.widgets:
            widget.clear_file()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec())
