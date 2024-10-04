import operator
import math
from uiDefiner import Calculator

def percent(value, ofAnother):
    return value/100*ofAnother

#This class acts as a controller for the program, checking button events and calling the corresponding functions.
class AppLogic:
    def __init__(self, calculator: Calculator):
        
        #display vars
        self.lineEdit = calculator.lineEditDisplay
        self.label = calculator.labelDisplay
        
        #calculation vars
        self.labelMainText = ''
        self.linEditMaintext = '0'
        self.operation = None
        self.simbolOperation = ''
        self.value1 = 0
        self.value2 = 0
        self.result = 0

        #Update display when starting
        self.displayUpdate()

    def inputNumberFormat(self, value):
        try:
            valor_float = float(value)
           
            if valor_float.is_integer():
                return int(valor_float)
            return valor_float

        except ValueError:
            if value == '':
                return 0
        
        raise ValueError("Valor inválido")  
      
    def displayUpdate(self):
        self.lineEdit.setText(self.linEditMaintext.replace('.',','))
        self.label.setText(self.labelMainText)
    
    def setDisplayLineEditText(self, text):
        if self.linEditMaintext == '0':
            self.linEditMaintext = ''
        self.linEditMaintext = self.linEditMaintext + text
    
    def setDisplayLabelText(self):
        if self.operation == math.sqrt:
            self.labelMainText = f'{self.simbolOperation}({self.value1})'
            self.displayUpdate()
            return
                
        if self.value2 != 0:
            equalsSimbol = "="
            value2Text = self.value2
        else:
            equalsSimbol = ''
            value2Text = ''

        if self.operation == percent:
            self.labelMainText = f'{self.value1}{self.simbolOperation} de {value2Text}{equalsSimbol}'
            self.displayUpdate()
            return
        
        self.labelMainText = f'{self.value1}{self.simbolOperation}{value2Text}{equalsSimbol}'

    def calculate(self):
        if self.operation == math.sqrt:
            print('funciona')
            self.result = self.inputNumberFormat(self.operation(self.value1))
       
        else:
            self.result = self.inputNumberFormat(self.operation(self.value1,self.value2))  
       
    def sum(self):
        if self.operation is None:
            self.operation = operator.add
            self.value1 = self.inputNumberFormat(self.linEditMaintext)
            self.linEditMaintext = ''
            self.simbolOperation = '+'
            self.value2= 0
        elif self.operation == operator.add:
            self.value2 = self.inputNumberFormat(self.linEditMaintext)
            self.equals()
        elif self.operation != operator.add:
            self.operation = operator.add
            self.simbolOperation = '+'
                        
        self.setDisplayLabelText()

    def subtract(self):
        if self.operation is None:
            self.operation = operator.sub
            self.value1 = self.inputNumberFormat(self.linEditMaintext)
            self.linEditMaintext = ''
            self.simbolOperation = '-'
            self.value2= 0
        elif self.operation == operator.sub:
            self.value2 = self.inputNumberFormat(self.linEditMaintext)
            self.equals()
        elif self.operation != operator.sub:
            self.operation = operator.sub
            self.simbolOperation = '-'
                        
        self.setDisplayLabelText()
    
    def multiplication(self):
        if self.operation is None:
            self.operation = operator.mul
            self.value1 = self.inputNumberFormat(self.linEditMaintext)
            self.linEditMaintext = ''
            self.simbolOperation = '*'
            self.value2= 0
        elif self.operation == operator.mul:
            self.value2 = self.inputNumberFormat(self.linEditMaintext)
            self.equals()
        elif self.operation != operator.mul:
            self.operation = operator.mul
            self.simbolOperation = '*'
                        
        self.setDisplayLabelText()

    def division(self):
        if self.operation is None:
            self.operation = operator.truediv
            self.value1 = self.inputNumberFormat(self.linEditMaintext)
            self.linEditMaintext = ''
            self.simbolOperation = '/'
            self.value2= 0
        elif self.operation == operator.truediv:
            self.value2 = self.inputNumberFormat(self.linEditMaintext)
            self.equals()
        elif self.operation != operator.truediv:
            self.operation = operator.truediv
            self.simbolOperation = '/'
                        
        self.setDisplayLabelText()

    def exponentiation(self):
        if self.operation is None:
            self.operation = operator.pow
            self.value1 = self.inputNumberFormat(self.linEditMaintext)
            self.linEditMaintext = ''
            self.simbolOperation = '^'
            self.value2= 0
        elif self.operation == operator.pow:
            self.value2 = self.inputNumberFormat(self.linEditMaintext)
            self.equals()
        elif self.operation != operator.pow:
            self.operation = operator.pow
            self.simbolOperation = '^'
                        
        self.setDisplayLabelText()

    def quad(self):
        
        self.value2= 0
        self.operation = math.sqrt
        print((self.linEditMaintext))
        self.value1 = self.inputNumberFormat(self.linEditMaintext)
        self.simbolOperation = '√'
        self.linEditMaintext = ''
        self.equals()
                    
    def percent(self):
        
        if self.operation is None:
            self.operation = percent
            self.value1 = self.inputNumberFormat(self.linEditMaintext)
            self.linEditMaintext = ''
            self.simbolOperation = '%'
            self.value2= 0
        elif self.operation == percent:
            self.value2 = self.inputNumberFormat(self.linEditMaintext)
            self.equals()
        elif self.operation != percent:
            self.operation = percent
            self.simbolOperation = '%'
                        
        self.setDisplayLabelText()

    def equals(self):
        if self.operation is None:
            return
                
        self.value2 = self.inputNumberFormat(self.linEditMaintext)
        self.setDisplayLabelText()
        if self.operation is not None:
            self.calculate()
            self.linEditMaintext = str(self.result)
        
        self.operation = None
        
        self.result = 0
    
    def clear(self):
        self.value1 = 0
        self.value2 = 0
        self.operation = None
        self.simbolOperation = ''
        self.result = 0
        self.linEditMaintext = '0'
        self.labelMainText = ''

    def backspace(self):
        text = self.linEditMaintext
        self.linEditMaintext = text[0:len(text)-1]

class AppConect:
    # Ao inicializar quero conectar a minha classe calculator onde crio botoes e estilos da minha calculadora a todos os eventos click dos botões
    def __init__(self,calculator: Calculator) -> None:
        self.buttons = calculator.buttons

    def conect(self, functionConected):
        for button in self.buttons.values():
            button.clicked.connect(functionConected)

if __name__ == "__main__":
  ...