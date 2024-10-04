import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QMainWindow, QGridLayout,QSizePolicy, QLineEdit,QLabel

#this, recive a layouts and set in a central widget and set a central widget in a one window
class App(QMainWindow):
    def __init__(self,pLayout: QVBoxLayout | None = None) -> None:
        super().__init__() 
        
        self.layout_ = pLayout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout_)
        self.setCentralWidget(self.central_widget)   


class Make_Layout(QGridLayout):
    def __init__(self):
        super().__init__() 
        self._widgets: list[QWidget] = []
        
    @property
    def get_widget(self,index):
        return self._widgets[index]

    
    def set_widgets(self,widgets:list[QWidget],amColumns=0):
        countRow = 0
        countColum = 0
        for widget in widgets:

            self._widgets.append(widget)
            
            self.addWidget(widget, countRow,countColum)
            
            countColum += 1
            if countColum == amColumns:
                countRow += 1
                countColum = 0
