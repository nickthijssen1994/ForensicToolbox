import hashlib
import os

from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from collections import OrderedDict as od


class HashWidget(QWidget):
    title = "Hashes"

    def __init__(self, parent):
        super(HashWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self._fileContent = QTextEdit()
        self._fileContent.acceptRichText()
        self.layout.addWidget(self._fileContent)

    def get_hashsums(self, file_path):
        hash_sums = od()
        hash_sums['md5sum'] = hashlib.md5()
        hash_sums['sha1sum'] = hashlib.sha1()
        hash_sums['sha224sum'] = hashlib.sha224()
        hash_sums['sha256sum'] = hashlib.sha256()
        hash_sums['sha384sum'] = hashlib.sha384()
        hash_sums['sha512sum'] = hashlib.sha512()

        with open(file_path, 'rb') as fd:
            data_chunk = fd.read(1024)
            while data_chunk:
                for hashsum in hash_sums.keys():
                    hash_sums[hashsum].update(data_chunk)
                data_chunk = fd.read(1024)

        results = od()
        for key,value in hash_sums.items():
            results[key] = value.hexdigest()
        return results

    def set_file(self, file):
        for key,value in self.get_hashsums(file).items():
            self._fileContent.append(key + ' ' + value)
