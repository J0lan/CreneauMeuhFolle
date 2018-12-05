# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajout_benevole.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ajout_Benevoles(object):
    def setupUi(self, Ajout_Benevoles):
        Ajout_Benevoles.setObjectName("Ajout_Benevoles")
        Ajout_Benevoles.resize(381, 350)
        self.gridLayout = QtWidgets.QGridLayout(Ajout_Benevoles)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lnom = QtWidgets.QLabel(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lnom.setFont(font)
        self.lnom.setObjectName("lnom")
        self.horizontalLayout.addWidget(self.lnom)
        self.nom = QtWidgets.QLineEdit(Ajout_Benevoles)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lcre1 = QtWidgets.QLabel(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lcre1.setFont(font)
        self.lcre1.setObjectName("lcre1")
        self.horizontalLayout_2.addWidget(self.lcre1)
        self.cre1 = QtWidgets.QComboBox(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cre1.setFont(font)
        self.cre1.setStyleSheet("QComboBox{\n"
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
        self.cre1.setObjectName("cre1")
        self.horizontalLayout_2.addWidget(self.cre1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lcre2 = QtWidgets.QLabel(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lcre2.setFont(font)
        self.lcre2.setObjectName("lcre2")
        self.horizontalLayout_3.addWidget(self.lcre2)
        self.cre2 = QtWidgets.QComboBox(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cre2.setFont(font)
        self.cre2.setStyleSheet("QComboBox{\n"
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
        self.cre2.setObjectName("cre2")
        self.horizontalLayout_3.addWidget(self.cre2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lcre3 = QtWidgets.QLabel(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lcre3.setFont(font)
        self.lcre3.setObjectName("lcre3")
        self.horizontalLayout_4.addWidget(self.lcre3)
        self.cre3 = QtWidgets.QComboBox(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cre3.setFont(font)
        self.cre3.setStyleSheet("QComboBox{\n"
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
        self.cre3.setObjectName("cre3")
        self.horizontalLayout_4.addWidget(self.cre3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lartisteV = QtWidgets.QLabel(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lartisteV.setFont(font)
        self.lartisteV.setObjectName("lartisteV")
        self.horizontalLayout_5.addWidget(self.lartisteV)
        self.artisteV = QtWidgets.QComboBox(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.artisteV.setFont(font)
        self.artisteV.setStyleSheet("QComboBox{\n"
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
        self.artisteV.setObjectName("artisteV")
        self.horizontalLayout_5.addWidget(self.artisteV)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lremarques = QtWidgets.QLabel(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lremarques.setFont(font)
        self.lremarques.setObjectName("lremarques")
        self.horizontalLayout_7.addWidget(self.lremarques)
        self.remarques = QtWidgets.QLineEdit(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.remarques.setFont(font)
        self.remarques.setStyleSheet("QLineEdit {\n"
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
        self.remarques.setPlaceholderText("")
        self.remarques.setObjectName("remarques")
        self.horizontalLayout_7.addWidget(self.remarques)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ok = QtWidgets.QPushButton(Ajout_Benevoles)
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
        self.horizontalLayout_8.addWidget(self.ok)
        self.annuler = QtWidgets.QPushButton(Ajout_Benevoles)
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
        self.horizontalLayout_8.addWidget(self.annuler)
        self.gridLayout.addLayout(self.horizontalLayout_8, 7, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lartisteS = QtWidgets.QLabel(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lartisteS.setFont(font)
        self.lartisteS.setObjectName("lartisteS")
        self.horizontalLayout_6.addWidget(self.lartisteS)
        self.artisteS = QtWidgets.QComboBox(Ajout_Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.artisteS.setFont(font)
        self.artisteS.setStyleSheet("QComboBox{\n"
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
        self.artisteS.setObjectName("artisteS")
        self.horizontalLayout_6.addWidget(self.artisteS)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)

        self.retranslateUi(Ajout_Benevoles)
        QtCore.QMetaObject.connectSlotsByName(Ajout_Benevoles)

    def retranslateUi(self, Ajout_Benevoles):
        _translate = QtCore.QCoreApplication.translate
        Ajout_Benevoles.setWindowTitle(_translate("Ajout_Benevoles", "Ajouter un benevole"))
        self.lnom.setText(_translate("Ajout_Benevoles", "Nom Prenom"))
        self.nom.setPlaceholderText(_translate("Ajout_Benevoles", "Moreau Jolan"))
        self.lcre1.setText(_translate("Ajout_Benevoles", "Categorie de creneaux 1"))
        self.lcre2.setText(_translate("Ajout_Benevoles", "Categorie de creneaux 2"))
        self.lcre3.setText(_translate("Ajout_Benevoles", "Categorie de creneaux 3"))
        self.lartisteV.setText(_translate("Ajout_Benevoles", "Artiste du Vendredi"))
        self.lremarques.setText(_translate("Ajout_Benevoles", "Remarques"))
        self.ok.setText(_translate("Ajout_Benevoles", "Ok"))
        self.annuler.setText(_translate("Ajout_Benevoles", "Annuler"))
        self.lartisteS.setText(_translate("Ajout_Benevoles", "Artiste du Samedi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ajout_Benevoles = QtWidgets.QDialog()
    ui = Ui_Ajout_Benevoles()
    ui.setupUi(Ajout_Benevoles)
    Ajout_Benevoles.show()
    sys.exit(app.exec_())

