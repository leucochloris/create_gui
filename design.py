# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 510)
        MainWindow.setMinimumSize(QtCore.QSize(260, 510))
        MainWindow.setMaximumSize(QtCore.QSize(260, 510))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAccessibleName("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(-1, 10, 260, 270))
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 248, 478))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.scrollAreaWidgetContents)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.button_1 = QtWidgets.QPushButton(self.splitter_3)
        self.button_1.setEnabled(True)
        self.button_1.setMouseTracking(False)
        self.button_1.setTabletTracking(False)
        self.button_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_1.setStyleSheet("")
        self.button_1.setInputMethodHints(QtCore.Qt.ImhNone)
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.splitter_3)
        self.button_2.setObjectName("button_2")
        self.verticalLayout.addWidget(self.splitter_3)
        self.button_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_3.setObjectName("button_3")
        self.verticalLayout.addWidget(self.button_3)
        self.button_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_18.setObjectName("button_18")
        self.verticalLayout.addWidget(self.button_18)
        self.button_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_4.setObjectName("button_4")
        self.verticalLayout.addWidget(self.button_4)
        self.splitter_4 = QtWidgets.QSplitter(self.scrollAreaWidgetContents)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.button_5 = QtWidgets.QPushButton(self.splitter_4)
        self.button_5.setObjectName("button_5")
        self.button_10 = QtWidgets.QPushButton(self.splitter_4)
        self.button_10.setObjectName("button_10")
        self.verticalLayout.addWidget(self.splitter_4)
        self.button_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_15.setObjectName("button_15")
        self.verticalLayout.addWidget(self.button_15)
        self.button_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_19.setObjectName("button_19")
        self.verticalLayout.addWidget(self.button_19)
        self.button_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_6.setObjectName("button_6")
        self.verticalLayout.addWidget(self.button_6)
        self.button_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_7.setObjectName("button_7")
        self.verticalLayout.addWidget(self.button_7)
        self.button_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_17.setObjectName("button_17")
        self.verticalLayout.addWidget(self.button_17)
        self.button_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_8.setObjectName("button_8")
        self.verticalLayout.addWidget(self.button_8)
        self.button_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_9.setEnabled(True)
        self.button_9.setMouseTracking(False)
        self.button_9.setTabletTracking(False)
        self.button_9.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_9.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_9.setStyleSheet("")
        self.button_9.setInputMethodHints(QtCore.Qt.ImhNone)
        self.button_9.setObjectName("button_9")
        self.verticalLayout.addWidget(self.button_9)
        self.button_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_11.setObjectName("button_11")
        self.verticalLayout.addWidget(self.button_11)
        self.button_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_12.setObjectName("button_12")
        self.verticalLayout.addWidget(self.button_12)
        self.button_20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_20.setObjectName("button_20")
        self.verticalLayout.addWidget(self.button_20)
        self.button_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button_16.setObjectName("button_16")
        self.verticalLayout.addWidget(self.button_16)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 290, 230, 40))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.button_13 = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_13.setFont(font)
        self.button_13.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.button_13.setObjectName("button_13")
        self.button_14 = QtWidgets.QPushButton(self.splitter)
        self.button_14.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_14.setFont(font)
        self.button_14.setMouseTracking(False)
        self.button_14.setTabletTracking(False)
        self.button_14.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_14.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_14.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.button_14.setInputMethodHints(QtCore.Qt.ImhNone)
        self.button_14.setObjectName("button_14")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 420, 110, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(10, 420, 100, 70))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton.setObjectName("pushButton")
        self.button_copy = QtWidgets.QPushButton(self.splitter_2)
        self.button_copy.setObjectName("button_copy")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 340, 230, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit.setFont(font)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setLineWrapColumnOrWidth(0)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.pressed.connect(self.textEdit.selectAll)
        self.button_copy.pressed.connect(self.textEdit.copy)
        self.pushButton_2.pressed.connect(self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WriteCOM"))
        self.button_1.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.button_1.setText(_translate("MainWindow", "Новый"))
        self.button_2.setText(_translate("MainWindow", "Старый"))
        self.button_3.setText(_translate("MainWindow", "ИДЕНТ"))
        self.button_18.setText(_translate("MainWindow", "Русский акк"))
        self.button_4.setText(_translate("MainWindow", "Много на ПОЛУЧАТЕЛЯ"))
        self.button_5.setText(_translate("MainWindow", "НЕДОСТАТОЧНО СРЕДСТВ"))
        self.button_10.setText(_translate("MainWindow", "Ошибки 3DS"))
        self.button_15.setText(_translate("MainWindow", "Меняет карту"))
        self.button_19.setText(_translate("MainWindow", "Новая карта"))
        self.button_6.setText(_translate("MainWindow", "Дробит"))
        self.button_7.setText(_translate("MainWindow", "Подбирает сумму"))
        self.button_17.setText(_translate("MainWindow", "Фродовый банк"))
        self.button_8.setText(_translate("MainWindow", "Опасное направление"))
        self.button_9.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.button_9.setText(_translate("MainWindow", "Странное поведение"))
        self.button_11.setText(_translate("MainWindow", "Много карт (источников)"))
        self.button_12.setText(_translate("MainWindow", "Большой перевод"))
        self.button_20.setText(_translate("MainWindow", "Меняет IP"))
        self.button_16.setText(_translate("MainWindow", "Большой перевод на МОБИЛЬНЫЙ"))
        self.button_13.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>На идент, что непонятно?! </p></body></html>"))
        self.button_13.setText(_translate("MainWindow", "НА ИДЕНТ "))
        self.button_14.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.button_14.setText(_translate("MainWindow", "СЕЛФИ С КАРТОЙ"))
        self.pushButton_2.setText(_translate("MainWindow", "ОЧИСТИТЬ"))
        self.pushButton.setText(_translate("MainWindow", "Выделить ВСЁ"))
        self.button_copy.setText(_translate("MainWindow", "Копировать"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Выберите причину..."))
