import sys

from PySide6.QtCore import QStandardPaths, Slot, QFile
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtMultimedia import (QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog,
                               QMainWindow)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self._file = ""
        self._fileReader = QFile()
        self._player = QMediaPlayer()

        self._player.errorOccurred.connect(self._player_error)

        file_menu = self.menuBar().addMenu("&File")
        icon = QIcon.fromTheme("document-open")
        open_action = QAction(icon, "&Open...", self,
                              shortcut=QKeySequence.Open, triggered=self.open)
        file_menu.addAction(open_action)
        icon = QIcon.fromTheme("application-exit")
        exit_action = QAction(icon, "E&xit", self,
                              shortcut="Ctrl+Q", triggered=self.close)
        file_menu.addAction(exit_action)

        self._video_widget = QVideoWidget()
        self.setCentralWidget(self._video_widget)
        self._player.setVideoOutput(self._video_widget)

    def closeEvent(self, event):
        event.accept()

    @Slot()
    def open(self):
        file_dialog = QFileDialog(self)
        home_location = QStandardPaths.writableLocation(QStandardPaths.HomeLocation)
        file_dialog.setDirectory(home_location)
        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
            self._file = url
            self._fileReader = QFile(url)
            
            self._player.setSource(url)
            self._player.play()

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    @Slot(QMediaPlayer.Error, str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    available_geometry = main_win.screen().availableGeometry()
    main_win.resize(available_geometry.width() / 3,
                    available_geometry.height() / 2)
    main_win.setWindowTitle("Forensic Toolbox")
    main_win.show()
    sys.exit(app.exec())
