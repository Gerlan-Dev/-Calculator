import sys
import uiConstructor as ui
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QSizePolicy, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

style1 =""" QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """
style2 ="""QPushButton {
                background-color: #00BFFF;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #87CEFA;
            }
            QPushButton:pressed {
                background-color: #1E90FF;
            }
        """
style3 = """QPushButton {
                background-color: #0346bf;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #87CEFA;
            }
            QPushButton:pressed {
                background-color: #1E90FF;
            }
        """
class Calculator:

    #Buttons defination    
    def __init__(self) -> None:
        self.buttons = {
        "backspace": QPushButton('↩'), "clear": QPushButton('C'),  "percent": QPushButton('%'),    "exp": QPushButton('^'),
        "empt2": QPushButton(''),       "empt": QPushButton(''),    "quad": QPushButton('√'),       "mult": QPushButton('X'),
        9: QPushButton('9'),            8: QPushButton('8'),        7: QPushButton('7'),            "div": QPushButton('/'),
        6: QPushButton('6'),            5: QPushButton('5'),        4: QPushButton('4'),            "minus": QPushButton('-'), 
        1: QPushButton('1'),            2: QPushButton('2'),        3: QPushButton('3'),            "plus": QPushButton('+'),
        "minu+": QPushButton('+/-'),    0: QPushButton('0'),        "comma": QPushButton(','),      "equal": QPushButton("="),
    }
        #Buttons widgets style
        for button in self.buttons.values():
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            button.setStyleSheet(style1)

        #Style special buttons
        self.buttons['minu+'].setStyleSheet(style2)
        self.buttons['comma'].setStyleSheet(style2)
        self.buttons['equal'].setStyleSheet(style3)

        # Set style 2 by number buttons
        for i in range(10):
            self.buttons[i].setStyleSheet(style2)
        
        self.main_layout = QVBoxLayout()
        
        # creation a label
        self.labelDisplay = QLabel()
        self.labelDisplay.setFixedHeight(20)
        self.labelDisplay.setAlignment(Qt.AlignRight)
        self.labelDisplay.setContentsMargins(0, 0, 10, 0)
        self.labelDisplay.setStyleSheet("""
            QLabel {
                color: #333;
                font-size: 18px;
            }
        """)

        # Creation of a line edit
        self.lineEditDisplay = QLineEdit("")
        self.lineEditDisplay.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  # Faz a QLabel expandir
        self.lineEditDisplay.setFixedHeight(80)
        self.lineEditDisplay.setAlignment(Qt.AlignRight)
        self.lineEditDisplay.setStyleSheet("""
            QLineEdit {
                color: #333;
                font-size: 28px;
                font-weight: bold;
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                text-align: right;
            }
        """)

        # add QLabel in line edit at top position
        self.main_layout.addWidget(self.labelDisplay)
        self.main_layout.addWidget(self.lineEditDisplay)
        
        
        # create the buttons layout (Grid)
        self.grid_layout = ui.Make_Layout()
        self.grid_layout.set_widgets(list(self.buttons.values()), 4)  # 4 colunas de botões
        
        # add buttons at layout
        self.main_layout.addLayout(self.grid_layout)

        self.mainWindow = ui.App(self.main_layout)
        self.mainWindow.setMinimumWidth(350)
        self.mainWindow.setMinimumHeight(450)
        self.mainWindow.show()

        # Set program name
        self.mainWindow.setWindowTitle("Calculadora +/-*")

        # set program icon
        self.mainWindow.setWindowIcon(QIcon("icons/my_calculator_icon.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = Calculator()
    app.exec()