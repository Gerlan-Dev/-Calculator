import sys
from operations import AppConect, AppLogic
from functools import partial
from PySide6.QtWidgets import QApplication

from uiDefiner import Calculator

app = QApplication(sys.argv)
calculator = Calculator()

conection = AppConect(calculator)
logic = AppLogic(calculator)

def defActions(buttons):
    # conect especial buttons in your logic
    buttons['backspace'].clicked.connect(logic.backspace)
    buttons['clear'].clicked.connect(logic.clear)
    buttons['plus'].clicked.connect(logic.sum)
    buttons['minus'].clicked.connect(logic.subtract)
    buttons['mult'].clicked.connect(logic.multiplication)
    buttons['div'].clicked.connect(logic.division)
    buttons['exp'].clicked.connect(logic.exponentiation)
    buttons['quad'].clicked.connect(logic.quad)
    buttons['percent'].clicked.connect(logic.percent)
    buttons['equal'].clicked.connect(logic.equals)
    buttons['comma'].clicked.connect(partial(logic.setDisplayLineEditText,text = '.')) #This is used to pass a factory function with parameters.

    #Whenever a button emits a signal, it connects to a function responsible for updating the display.
    for i in range(10):
        buttons[i].clicked.connect(partial(logic.setDisplayLineEditText,text = str(i))) #This is used to pass a factory function with parameters.

    conection.conect(logic.displayUpdate)

if __name__ == "__main__":
    button = calculator.buttons
    defActions(button)
    app.exec()