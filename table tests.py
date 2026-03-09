#table tests

import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QLabel, 
    QVBoxLayout, 
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QMainWindow
)

import csv

listedValues = ["Tool", "Quantity", "Condition", "Tag", "Location"]

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.items = []

        self.loadCSV("sampleData.csv")
        
        # print(self.items)

        # set the window title
        self.setWindowTitle('Table test')
        self.setGeometry(100, 100, 640, 420)    #set window size

        #set the layout
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        
        #create the table
        self.table = QTableWidget(self)
        
        print(f"Item count is: {len(self.items)}")
        print(f"Column count is: {len(self.items[0])}")

        self.table.setRowCount(len(self.items))
        self.table.setColumnCount(len(self.items[0]))
        
        self.table.setHorizontalHeaderLabels(
            ["Tool", "Quantity", "Condition", "Tag", "Location"]
            )
        toolValues = [None, None, None, None, None]

        for i, (tool, quantity, condition, tag, location) in enumerate(self.items):
            listedValues = (tool, quantity, condition, tag, location)
            for t in range(0,5):
                toolValues[t] = QTableWidgetItem(listedValues[t])

            """ tool_name = QTableWidgetItem(tool)
            tool_quantity = QTableWidgetItem(quantity)
            tool_condition = QTableWidgetItem(condition)
            tool_tag = QTableWidgetItem(tag)
            tool_location = QTableWidgetItem(location)

            self.table.setItem(i, 0, tool_name)
            self.table.setItem(i, 1, tool_quantity)
            self.table.setItem(i, 2, tool_condition)
            self.table.setItem(i, 3, tool_tag)
            self.table.setItem(i, 4, tool_location) """

            for z in range(0,5):
                self.table.setItem(i, z, toolValues[z])
        
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        layout.addWidget(self.table)

        print("table visible?", self.table.isVisible())
        print("table size:", self.table.size())
        print("geometry:", self.table.geometry())
        print("layout on window:", self.layout())
        
        # show the window
        self.show()
    
    def button_clicked(self):
        print("clicked!")
    
    def loadCSV(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):
                self.items.append(list(row))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())

    """ import sys
    from PyQt6.QtGui import QColor
    from PyQt6.QtWidgets import (QApplication, QTableWidget,
                               QTableWidgetItem)
    
    colors = [("Red", "#FF0000"),
          ("Green", "#00FF00"),
          ("Blue", "#0000FF"),
          ("Black", "#000000"),
          ("White", "#FFFFFF"),
          ("Electric Green", "#41CD52"),
          ("Dark Blue", "#222840"),
          ("Yellow", "#F9E56d")]
    
    def get_rgb_from_hex(code):
        code_hex = code.replace("#", "")
        rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
        return QColor.fromRgb(rgb[0], rgb[1], rgb[2])
    
    app = QApplication(sys.argv)

    table = QTableWidget()
    table.setRowCount(len(colors))
    table.setColumnCount(len(colors[0]) + 1)
    table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])

    for i, (name, code) in enumerate(colors):
        item_name = QTableWidgetItem(name)
        item_code = QTableWidgetItem(code)
        item_color = QTableWidgetItem()
        item_color.setBackground(get_rgb_from_hex(code))
        table.setItem(i, 0, item_name)
        table.setItem(i, 1, item_code)
        table.setItem(i, 2, item_color)

    table.show()
    sys.exit(app.exec()) """