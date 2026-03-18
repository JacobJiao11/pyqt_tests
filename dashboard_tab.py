#table tests

import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QLabel, 
    QVBoxLayout,
    QHBoxLayout, 
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QMainWindow,
    QAbstractItemView,
    QMessageBox,
    QGroupBox
)


import csv

class myDashboard(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #create main layout
        self.mainLayout = QHBoxLayout(self)

        #create table layout
        self.create_layout("Who's currently In?")

        #create note layout
        self.create_layout("Student Notes: ")

        #create tool layout
        self.create_layout("Available Tools: ")

        #populate it

        self.setLayout(self.mainLayout)
        # show the window
        self.show()
    
    def create_layout(self, textBox):
        layout = QVBoxLayout()

        header = QLineEdit()
        header.setText(textBox)
        header.setReadOnly(True)
        layout.addWidget(header)

        data = QTableWidget()
        layout.addWidget(data)

        self.mainLayout.addLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = myDashboard()

    # start the event loop
    sys.exit(app.exec())