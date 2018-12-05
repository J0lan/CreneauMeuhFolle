# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajout_creneau.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(318, 292)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setMinimumSize(QtCore.QSize(146, 0))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.ok.setFont(font)
        self.ok.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border-width: 2px;\n"
"     border-radius: 10px;   \n"
"     border-color: black;    \n"
"    min-width: 10em;    \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }\n"
"")
        self.ok.setObjectName("ok")
        self.horizontalLayout_5.addWidget(self.ok)
        self.annuler = QtWidgets.QPushButton(Dialog)
        self.annuler.setMinimumSize(QtCore.QSize(146, 0))
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
        self.horizontalLayout_5.addWidget(self.annuler)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.duree = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.duree.setFont(font)
        self.duree.setStyleSheet("QComboBox{\n"
"border : 3px solid black;\n"
"border-radius : 5px;\n"
"background : qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 255), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"padding-left : 10px;\n"
"padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"border : 3px solid darkGreen;\n"
"border-radius : 5px;\n"
"background : yellow;\n"
"padding-left : 10px;\n"
"padding-bottom: 2px\n"
"}\n"
"\n"
"QComboBox::on {\n"
"border : 3px solid transparent;\n"
"border-radius : 5px;\n"
"background : yellow;\n"
"padding-left : 10px;\n"
"padding-bottom: 2px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 3px solid black;\n"
"    color: black;\n"
"    selection-background-color: yellow;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.duree.setEditable(False)
        self.duree.setObjectName("duree")
        self.horizontalLayout_3.addWidget(self.duree)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.plageHor = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.plageHor.setFont(font)
        self.plageHor.setStyleSheet("QComboBox{\n"
"border : 3px solid black;\n"
"border-radius : 5px;\n"
"background : qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 255), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"padding-left : 10px;\n"
"padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"border : 3px solid darkGreen;\n"
"border-radius : 5px;\n"
"background : yellow;\n"
"padding-left : 10px;\n"
"padding-bottom: 2px\n"
"}\n"
"\n"
"QComboBox::on {\n"
"border : 3px solid transparent;\n"
"border-radius : 5px;\n"
"background : yellow;\n"
"padding-left : 10px;\n"
"padding-bottom: 2px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 3px solid black;\n"
"    color: black;\n"
"    selection-background-color: yellow;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.plageHor.setEditable(False)
        self.plageHor.setMaxVisibleItems(24)
        self.plageHor.setObjectName("plageHor")
        self.horizontalLayout_2.addWidget(self.plageHor)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.categorie = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.categorie.setFont(font)
        self.categorie.setStyleSheet("QComboBox{\n"
"border : 3px solid black;\n"
"border-radius : 5px;\n"
"background : qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 255), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"padding-left : 10px;\n"
"padding-bottom: 2px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"border : 3px solid darkGreen;\n"
"border-radius : 5px;\n"
"background : yellow;\n"
"padding-left : 10px;\n"
"padding-bottom: 2px\n"
"}\n"
"\n"
"QComboBox::on {\n"
"border : 3px solid transparent;\n"
"border-radius : 5px;\n"
"background : yellow;\n"
"padding-left : 10px;\n"
"padding-bottom: 2px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 3px solid black;\n"
"    color: black;\n"
"    selection-background-color: yellow;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.categorie.setEditable(False)
        self.categorie.setObjectName("categorie")
        self.horizontalLayout_4.addWidget(self.categorie)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nom = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.nom.setFont(font)
        self.nom.setStyleSheet("QLineEdit {\n"
"     border: 3px solid black;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     selection-background-color: black ;\n"
" }\n"
"QLineEdit::hover {\n"
"     border: 3px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:0.0511364, y2:0.034, stop:0 rgba(255, 255, 255, 255), stop:0.965909 rgba(0, 156, 0, 167));\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     selection-background-color: black ;\n"
" }\n"
"\n"
"QLineEdit::focus {\n"
"     border: 3px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:0.0511364, y2:0.034, stop:0 rgba(255, 255, 255, 255), stop:0.965909 rgba(0, 156, 0, 167));\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     selection-background-color: black ;\n"
" }")
        self.nom.setObjectName("nom")
        self.horizontalLayout.addWidget(self.nom)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ajouter un creneau"))
        self.ok.setText(_translate("Dialog", "Ok"))
        self.annuler.setText(_translate("Dialog", "Annuler"))
        self.label_5.setText(_translate("Dialog", "Duree"))
        self.label_4.setText(_translate("Dialog", "Plage Horaire"))
        self.label_6.setText(_translate("Dialog", "Categorie"))
        self.label.setText(_translate("Dialog", "Nom"))
        self.nom.setPlaceholderText(_translate("Dialog", "Parking 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

