import hashlib
from collections import OrderedDict as od

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


class HashWidget(QWidget):
    title = "Hashes"

    def __init__(self, parent):
        super(HashWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTableWidget(self)
        self.layout.addWidget(self._fileContent)

    def get_hashsums(self, file_path):
        hash_sums = od()
        hash_sums['md5'] = hashlib.md5()
        hash_sums['sha1'] = hashlib.sha1()
        hash_sums['sha224'] = hashlib.sha224()
        hash_sums['sha256'] = hashlib.sha256()
        hash_sums['sha384'] = hashlib.sha384()
        hash_sums['sha512'] = hashlib.sha512()

        with open(file_path, 'rb') as fd:
            data_chunk = fd.read(1024)
            while data_chunk:
                for hashsum in hash_sums.keys():
                    hash_sums[hashsum].update(data_chunk)
                data_chunk = fd.read(1024)

        results = od()
        for key, value in hash_sums.items():
            results[key] = value.hexdigest()
        return results

    def set_file(self, file):
        data = self.get_hashsums(file).items()
        self._fileContent.setRowCount(len(data))
        self._fileContent.setColumnCount(2)
        self._fileContent.setHorizontalHeaderLabels(["Function", "Hash"])
        for i, (function, filehash) in enumerate(data):
            item_name = QTableWidgetItem(function)
            item_code = QTableWidgetItem(filehash)
            self._fileContent.setItem(i, 0, item_name)
            self._fileContent.setItem(i, 1, item_code)
        self._fileContent.resizeColumnToContents(1)

    def clear_file(self):
        self._fileContent.clear()
