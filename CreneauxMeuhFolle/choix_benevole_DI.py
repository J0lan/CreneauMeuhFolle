# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choix_benevole.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(315, 770)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.annuler = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.annuler.setFont(font)
        self.annuler.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border-width: 2px;\n"
"     border-radius: 10px;   \n"
"     border-color: black;    \n"
"    min-width: 10em;    \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.annuler.setObjectName("annuler")
        self.gridLayout.addWidget(self.annuler, 1, 0, 1, 1)
        self.listBenevoles = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.listBenevoles.setFont(font)
        self.listBenevoles.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::selected{\n"
"    background : transparent;\n"
"    color: black\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}")
        self.listBenevoles.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listBenevoles.setTabKeyNavigation(False)
        self.listBenevoles.setProperty("showDropIndicator", True)
        self.listBenevoles.setAlternatingRowColors(True)
        self.listBenevoles.setViewMode(QtWidgets.QListView.ListMode)
        self.listBenevoles.setSelectionRectVisible(True)
        self.listBenevoles.setObjectName("listBenevoles")
        self.gridLayout.addWidget(self.listBenevoles, 0, 0, 1, 1)
        self.supprimer = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.supprimer.setFont(font)
        self.supprimer.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border-width: 2px;\n"
"     border-radius: 10px;   \n"
"     border-color: black;    \n"
"    min-width: 10em;    \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.supprimer.setObjectName("supprimer")
        self.gridLayout.addWidget(self.supprimer, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choisissez un benevole"))
        self.annuler.setText(_translate("Dialog", "Annuler"))
        self.supprimer.setText(_translate("Dialog", "Vider la cellule"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

