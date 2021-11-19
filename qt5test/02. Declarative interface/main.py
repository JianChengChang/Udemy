import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *
from PyQt5.QtQuick import *
from PyQt5.Qt import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile(r".\02. Declarative interface\main.qml"))

    sys.exit(app.exec_())