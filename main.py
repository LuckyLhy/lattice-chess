# -*- coding: UTF-8 -*-
import sys

from DotsAndBoxes.main_window_controller import MainWindowController
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindowController()
    window.window.show()
    sys.exit(app.exec_())

