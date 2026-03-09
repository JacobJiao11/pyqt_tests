import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QLabel, 
    QVBoxLayout, 
    QPushButton,
    QLineEdit,
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # set the window title
        self.setWindowTitle('Hello World')
        #set window size (x cord, y cord, x size, y size)   
        self.setGeometry(100, 100, 320, 210)    

        """ label = [None, None, None, None, None] """

        label = QLabel()

        #create button
        button = QPushButton('CLICK')
        button.clicked.connect(
            self.button_clicked
            )

        #create line edit thing
        line = QLineEdit()
        line.textChanged.connect(label.setText)

        layout = QVBoxLayout()

        #create label
        """ for i in range(0,3):
            label[i] = QLabel(f"this is label {i+1}.")
            layout.addWidget(label[i])
 """
        #place line 
        layout.addWidget(label)
        layout.addWidget(line)

        #add button
        layout.addWidget(button)
        # button.setCheckable(True)   #button becomes toggle

        #set the layout
        self.setLayout(layout)
        
        # show the window
        self.show()
    
    def button_clicked(self):
        print("clicked!")

        self.secondThing

    def secondThing(self):
        print("pft")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    label = QLabel() 
    label.setText('This is a widget.')

    # start the event loop
    sys.exit(app.exec())