import sys
import csv
from PyQt6.QtWidgets import QApplication, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem

# class CSVTable(qtable)
def load_csv_to_model(path):
    model = QStandardItemModel()

    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Set headers (first row)
    headers = rows[0]
    model.setHorizontalHeaderLabels(headers)

    # Add data rows
    for row_data in rows[1:]:
        items = [QStandardItem(field) for field in row_data]
        model.appendRow(items)

    return model


app = QApplication(sys.argv)

view = QTableView()
model = load_csv_to_model("sampleData.csv")
view.setModel(model)

view.resize(600, 400)
view.show()

sys.exit(app.exec())