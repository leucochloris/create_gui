import sys

from design import *  # Импортируем наш интерфейс из файла
from PyQt5 import QtCore, QtGui, QtWidgets, QtCore

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setWindowFlags(self.windowFlags() | QtWidgets.WindowStaysOnTopHint)
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        

        # Здесь прописываем событие нажатия на кнопку 1
        self.ui.button_1.clicked.connect(self.MyFunction_1)

            # Здесь прописываем событие нажатия на кнопку 2
        self.ui.button_2.clicked.connect(self.MyFunction_2)

                # Здесь прописываем событие нажатия на кнопку 3
        self.ui.button_3.clicked.connect(self.MyFunction_3)

                # Здесь прописываем событие нажатия на кнопку 4
        self.ui.button_4.clicked.connect(self.MyFunction_4)

                # Здесь прописываем событие нажатия на кнопку 5
        self.ui.button_5.clicked.connect(self.MyFunction_5)

                   # Здесь прописываем событие нажатия на кнопку 6
        self.ui.button_6.clicked.connect(self.MyFunction_6)

                   # Здесь прописываем событие нажатия на кнопку 7
        self.ui.button_7.clicked.connect(self.MyFunction_7)

                   # Здесь прописываем событие нажатия на кнопку 8
        self.ui.button_8.clicked.connect(self.MyFunction_8)

                   # Здесь прописываем событие нажатия на кнопку 9
        self.ui.button_9.clicked.connect(self.MyFunction_9)

                   # Здесь прописываем событие нажатия на кнопку 10
        self.ui.button_10.clicked.connect(self.MyFunction_10)

                   # Здесь прописываем событие нажатия на кнопку 11
        self.ui.button_11.clicked.connect(self.MyFunction_11)
        
                   # Здесь прописываем событие нажатия на кнопку 12
        self.ui.button_12.clicked.connect(self.MyFunction_12)

                   # Здесь прописываем событие нажатия на кнопку 13
        self.ui.button_13.clicked.connect(self.MyFunction_13)

                   # Здесь прописываем событие нажатия на кнопку 14
        self.ui.button_14.clicked.connect(self.MyFunction_14)

                # Здесь прописываем событие нажатия на кнопку 15
        self.ui.button_15.clicked.connect(self.MyFunction_15)

                # Здесь прописываем событие нажатия на кнопку 16
        self.ui.button_16.clicked.connect(self.MyFunction_16)

                # Здесь прописываем событие нажатия на кнопку 17
        self.ui.button_17.clicked.connect(self.MyFunction_17)

               # Здесь прописываем событие нажатия на кнопку 18
        self.ui.button_18.clicked.connect(self.MyFunction_18)

              # Здесь прописываем событие нажатия на кнопку 19
        self.ui.button_19.clicked.connect(self.MyFunction_19)

              # Здесь прописываем событие нажатия на кнопку 20
        self.ui.button_20.clicked.connect(self.MyFunction_20)


        

# Пока пустая функция которая выполняется при нажатии на кнопку 1
    def MyFunction_1(self):
        a = "Новый ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 2
    def MyFunction_2(self):
        a = "Старый ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 3
    def MyFunction_3(self):
        a = "| ИДЕНТ ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 4
    def MyFunction_4(self):
        a = "Много переводов на ПОЛУЧАТЕЛЯ | Получателя на ИДЕНТ ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 5
    def MyFunction_5(self):
        a = "| Ошибки: НЕДОСТАТОЧНО СРЕДСТВ ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 6
    def MyFunction_6(self):
        a = "| Дробит ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 7
    def MyFunction_7(self):
        a = "| Подбирает сумму ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 8
    def MyFunction_8(self):
        a = "| Опасное направление ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 9
    def MyFunction_9(self):
        a = "| Странное поведение ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 10
    def MyFunction_10(self):
        a = "| Ошибки 3DS ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 11
    def MyFunction_11(self):
        a = "| Много карт (источников)  ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 12
    def MyFunction_12(self):
        a = "| Большой перевод ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 13
    def MyFunction_13(self):
        a = "| На идент: ID + селфи с картой + ОБОСНОВАНИЕ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 14
    def MyFunction_14(self):
        a = "| Запрос: селфи с картой + ОБОСНОВАНИЕ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 15
    def MyFunction_15(self):
        a = "| Меняет карту ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 16
    def MyFunction_16(self):
        a = "| Большой перевод на МОБИЛЬНЫЙ ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 17
    def MyFunction_17(self):
        a = "| Фродовый банк ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 18
    def MyFunction_18(self):
        a = "| Русский аккаунт ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 19
    def MyFunction_19(self):
        a = "| Новая карта ";
        self.ui.textEdit.insertPlainText(a)

# Пока пустая функция которая выполняется при нажатии на кнопку 20
    def MyFunction_20(self):
        a = "| Меняет IP ";
        self.ui.textEdit.insertPlainText(a)
        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
