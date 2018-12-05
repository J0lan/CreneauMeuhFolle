# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetre_principale.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1191, 825)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.centralWidget.setFont(font)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_9.setSpacing(3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab::selected{\n"
"color : rgb(200, 200, 0);\n"
"}\n"
"\n"
"QTabBar::tab:!selected{\n"
"color: grey;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background : qlineargradient(spread:pad, x1:0.722, y1:1, x2:0.652, y2:0.778545, stop:0.960227 rgba(211, 211, 211, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-color: darkGrey;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    border: 2px solid #C4C4C3;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    padding-left : 4px;\n"
"    padding-right : 4px\n"
"\n"
"}\n"
"\n"
"QTabWidget::pane { \n"
"    border: 3px solid darkGrey;\n"
"    border-radius : 10px;\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.vendredi = QtWidgets.QWidget()
        self.vendredi.setObjectName("vendredi")
        self.gridLayout = QtWidgets.QGridLayout(self.vendredi)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.rechercheV = QtWidgets.QComboBox(self.vendredi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rechercheV.sizePolicy().hasHeightForWidth())
        self.rechercheV.setSizePolicy(sizePolicy)
        self.rechercheV.setMinimumSize(QtCore.QSize(0, 15))
        self.rechercheV.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.rechercheV.setFont(font)
        self.rechercheV.setStyleSheet("QComboBox{\n"
"border : 3px solid black;\n"
"border-radius : 5px;\n"
"background : qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 255), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"padding-left : 10px;\n"
"padding-bottom: 2px\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    height: 20px;\n"
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
        self.rechercheV.setObjectName("rechercheV")
        self.rechercheV.addItem("")
        self.horizontalLayout_6.addWidget(self.rechercheV)
        self.supRechercheV = QtWidgets.QPushButton(self.vendredi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supRechercheV.sizePolicy().hasHeightForWidth())
        self.supRechercheV.setSizePolicy(sizePolicy)
        self.supRechercheV.setMinimumSize(QtCore.QSize(30, 30))
        self.supRechercheV.setMaximumSize(QtCore.QSize(30, 30))
        self.supRechercheV.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.supRechercheV.setText("")
        self.supRechercheV.setObjectName("supRechercheV")
        self.horizontalLayout_6.addWidget(self.supRechercheV)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.NbCBeneV = QtWidgets.QLabel(self.vendredi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NbCBeneV.sizePolicy().hasHeightForWidth())
        self.NbCBeneV.setSizePolicy(sizePolicy)
        self.NbCBeneV.setMinimumSize(QtCore.QSize(20, 40))
        self.NbCBeneV.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NbCBeneV.setFont(font)
        self.NbCBeneV.setStyleSheet("QLabel{\n"
"border : 3px solid black;\n"
"border-radius : 5px;\n"
"padding: 3px;\n"
"margin : 0px;\n"
"}")
        self.NbCBeneV.setAlignment(QtCore.Qt.AlignCenter)
        self.NbCBeneV.setObjectName("NbCBeneV")
        self.verticalLayout_4.addWidget(self.NbCBeneV)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.ResumeBenevoleV = QtWidgets.QTableWidget(self.vendredi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResumeBenevoleV.sizePolicy().hasHeightForWidth())
        self.ResumeBenevoleV.setSizePolicy(sizePolicy)
        self.ResumeBenevoleV.setMinimumSize(QtCore.QSize(0, 90))
        self.ResumeBenevoleV.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ResumeBenevoleV.setFont(font)
        self.ResumeBenevoleV.setStyleSheet("QHeaderView::section {\n"
"    padding : 5px;\n"
"     font: medium \"Cooper Black\";\n"
"     font-size: 14px;\n"
"         background : qlineargradient(spread:reflect, x1:0.499682, y1:0.5, x2:0.5, y2:0, stop:0.355932 rgba(255, 255, 255, 255), stop:0.903955 rgba(248, 82, 0, 73));\n"
"}\n"
"\n"
"\n"
"QTableWidget {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.363636 rgba(222, 222, 222, 164), stop:0.602273 rgba(222, 222, 222, 164)); alternate-background-color: rgb(255, 255, 160);\n"
"    border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"     gridline-color: black;\n"
"}\n"
"\n"
"QTableWidget::hover {border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;}")
        self.ResumeBenevoleV.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ResumeBenevoleV.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ResumeBenevoleV.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ResumeBenevoleV.setTabKeyNavigation(True)
        self.ResumeBenevoleV.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.ResumeBenevoleV.setObjectName("ResumeBenevoleV")
        self.ResumeBenevoleV.setColumnCount(4)
        self.ResumeBenevoleV.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleV.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleV.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleV.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleV.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleV.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleV.setHorizontalHeaderItem(3, item)
        self.ResumeBenevoleV.horizontalHeader().setDefaultSectionSize(200)
        self.horizontalLayout_3.addWidget(self.ResumeBenevoleV)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollAtTopV = QtWidgets.QPushButton(self.vendredi)
        self.scrollAtTopV.setMinimumSize(QtCore.QSize(30, 30))
        self.scrollAtTopV.setMaximumSize(QtCore.QSize(30, 30))
        self.scrollAtTopV.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.scrollAtTopV.setText("")
        self.scrollAtTopV.setObjectName("scrollAtTopV")
        self.verticalLayout_5.addWidget(self.scrollAtTopV)
        self.scrollAtBottomV = QtWidgets.QPushButton(self.vendredi)
        self.scrollAtBottomV.setMinimumSize(QtCore.QSize(30, 30))
        self.scrollAtBottomV.setMaximumSize(QtCore.QSize(30, 30))
        self.scrollAtBottomV.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.scrollAtBottomV.setText("")
        self.scrollAtBottomV.setObjectName("scrollAtBottomV")
        self.verticalLayout_5.addWidget(self.scrollAtBottomV)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.creneauVendredi = QtWidgets.QTableWidget(self.vendredi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.creneauVendredi.setFont(font)
        self.creneauVendredi.setStyleSheet("QHeaderView::section {\n"
"     border : 1px  solid black;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"     font: medium \"Cooper Black\";\n"
"     font-size: 18px;\n"
"     background : qlineargradient(spread:reflect, x1:0.499682, y1:0.5, x2:0.5, y2:0, stop:0.355932 rgba(255, 255, 255, 255), stop:0.903955 rgba(248, 82, 0, 73));\n"
"}\n"
"QTableWidget{\n"
"    background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"    gridline-color :  Gray;\n"
"}\n"
"\n"
"")
        self.creneauVendredi.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.creneauVendredi.setAlternatingRowColors(True)
        self.creneauVendredi.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.creneauVendredi.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.creneauVendredi.setObjectName("creneauVendredi")
        self.creneauVendredi.setColumnCount(24)
        self.creneauVendredi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauVendredi.setHorizontalHeaderItem(23, item)
        self.creneauVendredi.horizontalHeader().setStretchLastSection(True)
        self.creneauVendredi.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.creneauVendredi, 1, 0, 1, 1)
        self.tabWidget.addTab(self.vendredi, "")
        self.samedi = QtWidgets.QWidget()
        self.samedi.setObjectName("samedi")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.samedi)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.rechercheS = QtWidgets.QComboBox(self.samedi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rechercheS.sizePolicy().hasHeightForWidth())
        self.rechercheS.setSizePolicy(sizePolicy)
        self.rechercheS.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.rechercheS.setFont(font)
        self.rechercheS.setStyleSheet("QComboBox{\n"
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
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 3px solid black;\n"
"    color: black;\n"
"    selection-background-color: yellow;\n"
"    selection-color: black;\n"
"}")
        self.rechercheS.setMaxVisibleItems(10)
        self.rechercheS.setObjectName("rechercheS")
        self.rechercheS.addItem("")
        self.horizontalLayout_9.addWidget(self.rechercheS)
        self.supRechercheS = QtWidgets.QPushButton(self.samedi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supRechercheS.sizePolicy().hasHeightForWidth())
        self.supRechercheS.setSizePolicy(sizePolicy)
        self.supRechercheS.setMinimumSize(QtCore.QSize(30, 30))
        self.supRechercheS.setMaximumSize(QtCore.QSize(30, 30))
        self.supRechercheS.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.supRechercheS.setText("")
        self.supRechercheS.setObjectName("supRechercheS")
        self.horizontalLayout_9.addWidget(self.supRechercheS)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.NbCBeneS = QtWidgets.QLabel(self.samedi)
        self.NbCBeneS.setMinimumSize(QtCore.QSize(20, 40))
        self.NbCBeneS.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NbCBeneS.setFont(font)
        self.NbCBeneS.setAccessibleName("")
        self.NbCBeneS.setAccessibleDescription("")
        self.NbCBeneS.setStyleSheet("QLabel{\n"
"border : 3px solid black;\n"
"border-radius : 5px;\n"
"padding: 3px;\n"
"margin : 0px;\n"
"}")
        self.NbCBeneS.setAlignment(QtCore.Qt.AlignCenter)
        self.NbCBeneS.setObjectName("NbCBeneS")
        self.verticalLayout_6.addWidget(self.NbCBeneS)
        self.horizontalLayout_14.addLayout(self.verticalLayout_6)
        self.ResumeBenevoleS = QtWidgets.QTableWidget(self.samedi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResumeBenevoleS.sizePolicy().hasHeightForWidth())
        self.ResumeBenevoleS.setSizePolicy(sizePolicy)
        self.ResumeBenevoleS.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ResumeBenevoleS.setFont(font)
        self.ResumeBenevoleS.setStyleSheet("QHeaderView::section {\n"
"    padding : 5px;\n"
"     font: medium \"Cooper Black\";\n"
"     font-size: 14px;\n"
"         background : qlineargradient(spread:reflect, x1:0.499682, y1:0.5, x2:0.5, y2:0, stop:0.355932 rgba(255, 255, 255, 255), stop:0.903955 rgba(248, 82, 0, 73));\n"
"}\n"
"\n"
"\n"
"QTableWidget {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.363636 rgba(222, 222, 222, 164), stop:0.602273 rgba(222, 222, 222, 164)); alternate-background-color: rgb(255, 255, 160);\n"
"    border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"     gridline-color: black;\n"
"}\n"
"\n"
"QTableWidget::hover {border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;}")
        self.ResumeBenevoleS.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ResumeBenevoleS.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ResumeBenevoleS.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ResumeBenevoleS.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.ResumeBenevoleS.setObjectName("ResumeBenevoleS")
        self.ResumeBenevoleS.setColumnCount(4)
        self.ResumeBenevoleS.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleS.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleS.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleS.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleS.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleS.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResumeBenevoleS.setHorizontalHeaderItem(3, item)
        self.ResumeBenevoleS.horizontalHeader().setDefaultSectionSize(200)
        self.horizontalLayout_14.addWidget(self.ResumeBenevoleS)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollAtTopS = QtWidgets.QPushButton(self.samedi)
        self.scrollAtTopS.setMinimumSize(QtCore.QSize(30, 30))
        self.scrollAtTopS.setMaximumSize(QtCore.QSize(30, 30))
        self.scrollAtTopS.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.scrollAtTopS.setText("")
        self.scrollAtTopS.setObjectName("scrollAtTopS")
        self.verticalLayout_7.addWidget(self.scrollAtTopS)
        self.scrollAtBottomS = QtWidgets.QPushButton(self.samedi)
        self.scrollAtBottomS.setMinimumSize(QtCore.QSize(30, 30))
        self.scrollAtBottomS.setMaximumSize(QtCore.QSize(30, 30))
        self.scrollAtBottomS.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.scrollAtBottomS.setText("")
        self.scrollAtBottomS.setObjectName("scrollAtBottomS")
        self.verticalLayout_7.addWidget(self.scrollAtBottomS)
        self.horizontalLayout_14.addLayout(self.verticalLayout_7)
        self.gridLayout_5.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)
        self.creneauSamedi = QtWidgets.QTableWidget(self.samedi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.creneauSamedi.setFont(font)
        self.creneauSamedi.setStyleSheet("QHeaderView::section {\n"
"     border : 1px  solid black;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"     font: medium \"Cooper Black\";\n"
"     font-size: 18px;\n"
"     background : qlineargradient(spread:reflect, x1:0.499682, y1:0.5, x2:0.5, y2:0, stop:0.355932 rgba(255, 255, 255, 255), stop:0.903955 rgba(248, 82, 0, 73));\n"
"}\n"
"QTableWidget{\n"
"    background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"    gridline-color :  Gray;\n"
"    \n"
"}\n"
"\n"
"")
        self.creneauSamedi.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.creneauSamedi.setAlternatingRowColors(True)
        self.creneauSamedi.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.creneauSamedi.setObjectName("creneauSamedi")
        self.creneauSamedi.setColumnCount(24)
        self.creneauSamedi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.creneauSamedi.setHorizontalHeaderItem(23, item)
        self.creneauSamedi.horizontalHeader().setStretchLastSection(True)
        self.creneauSamedi.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.creneauSamedi, 1, 0, 1, 1)
        self.tabWidget.addTab(self.samedi, "")
        self.Benevoles = QtWidgets.QWidget()
        self.Benevoles.setObjectName("Benevoles")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Benevoles)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nbBenevoles = QtWidgets.QLabel(self.Benevoles)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.nbBenevoles.setFont(font)
        self.nbBenevoles.setAlignment(QtCore.Qt.AlignCenter)
        self.nbBenevoles.setObjectName("nbBenevoles")
        self.horizontalLayout_2.addWidget(self.nbBenevoles)
        self.ajoutBenevole2 = QtWidgets.QPushButton(self.Benevoles)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ajoutBenevole2.sizePolicy().hasHeightForWidth())
        self.ajoutBenevole2.setSizePolicy(sizePolicy)
        self.ajoutBenevole2.setMinimumSize(QtCore.QSize(350, 30))
        self.ajoutBenevole2.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.ajoutBenevole2.setFont(font)
        self.ajoutBenevole2.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 2px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.ajoutBenevole2.setObjectName("ajoutBenevole2")
        self.horizontalLayout_2.addWidget(self.ajoutBenevole2)
        self.supBenevole = QtWidgets.QPushButton(self.Benevoles)
        self.supBenevole.setMinimumSize(QtCore.QSize(350, 30))
        self.supBenevole.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.supBenevole.setFont(font)
        self.supBenevole.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 2px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.supBenevole.setObjectName("supBenevole")
        self.horizontalLayout_2.addWidget(self.supBenevole)
        self.scrollAtBottomB = QtWidgets.QPushButton(self.Benevoles)
        self.scrollAtBottomB.setMinimumSize(QtCore.QSize(30, 30))
        self.scrollAtBottomB.setMaximumSize(QtCore.QSize(30, 30))
        self.scrollAtBottomB.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.scrollAtBottomB.setText("")
        self.scrollAtBottomB.setObjectName("scrollAtBottomB")
        self.horizontalLayout_2.addWidget(self.scrollAtBottomB)
        self.scrollAtTopB = QtWidgets.QPushButton(self.Benevoles)
        self.scrollAtTopB.setMinimumSize(QtCore.QSize(30, 30))
        self.scrollAtTopB.setMaximumSize(QtCore.QSize(30, 30))
        self.scrollAtTopB.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.scrollAtTopB.setText("")
        self.scrollAtTopB.setObjectName("scrollAtTopB")
        self.horizontalLayout_2.addWidget(self.scrollAtTopB)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 10, 0, 1, 1)
        self.tabBenevoles = QtWidgets.QTableWidget(self.Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.tabBenevoles.setFont(font)
        self.tabBenevoles.setStyleSheet("QHeaderView::section {\n"
"     border : 1px  solid black;\n"
"     padding: 0px;\n"
"     font: medium \"Cooper Black\";\n"
"     font-size: 16px;\n"
"     background : rgba(221, 103, 0,40);\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 green, stop: 0.5 yellow , stop: 1 red); \n"
"selection-color : black;\n"
"gridline-color : Gray}\n"
"\n"
"")
        self.tabBenevoles.setAlternatingRowColors(True)
        self.tabBenevoles.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabBenevoles.setRowCount(99)
        self.tabBenevoles.setColumnCount(11)
        self.tabBenevoles.setObjectName("tabBenevoles")
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabBenevoles.setHorizontalHeaderItem(10, item)
        self.tabBenevoles.horizontalHeader().setSortIndicatorShown(False)
        self.tabBenevoles.horizontalHeader().setStretchLastSection(False)
        self.tabBenevoles.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout_4.addWidget(self.tabBenevoles, 9, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(11, 0, 5, 11)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.supRechercheBene = QtWidgets.QPushButton(self.Benevoles)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supRechercheBene.sizePolicy().hasHeightForWidth())
        self.supRechercheBene.setSizePolicy(sizePolicy)
        self.supRechercheBene.setMinimumSize(QtCore.QSize(30, 30))
        self.supRechercheBene.setMaximumSize(QtCore.QSize(30, 30))
        self.supRechercheBene.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.supRechercheBene.setText("")
        self.supRechercheBene.setObjectName("supRechercheBene")
        self.horizontalLayout_8.addWidget(self.supRechercheBene)
        self.rechercheBenevoles = QtWidgets.QLineEdit(self.Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.rechercheBenevoles.setFont(font)
        self.rechercheBenevoles.setStyleSheet("QLineEdit {\n"
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
        self.rechercheBenevoles.setObjectName("rechercheBenevoles")
        self.horizontalLayout_8.addWidget(self.rechercheBenevoles)
        self.radioFiltreNom = QtWidgets.QRadioButton(self.Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.radioFiltreNom.setFont(font)
        self.radioFiltreNom.setStyleSheet("QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"    background-color : white;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked::hover{\n"
"    background-color :yellow;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"")
        self.radioFiltreNom.setChecked(True)
        self.radioFiltreNom.setObjectName("radioFiltreNom")
        self.horizontalLayout_8.addWidget(self.radioFiltreNom)
        self.radioFiltreCat = QtWidgets.QRadioButton(self.Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.radioFiltreCat.setFont(font)
        self.radioFiltreCat.setStyleSheet("QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"    background-color : white;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked::hover{\n"
"    background-color :yellow;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"")
        self.radioFiltreCat.setObjectName("radioFiltreCat")
        self.horizontalLayout_8.addWidget(self.radioFiltreCat)
        self.radioFiltreArtiste = QtWidgets.QRadioButton(self.Benevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.radioFiltreArtiste.setFont(font)
        self.radioFiltreArtiste.setStyleSheet("QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"    background-color : white;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked::hover{\n"
"    background-color :yellow;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"")
        self.radioFiltreArtiste.setObjectName("radioFiltreArtiste")
        self.horizontalLayout_8.addWidget(self.radioFiltreArtiste)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.tabWidget.addTab(self.Benevoles, "")
        self.Creneaux = QtWidgets.QWidget()
        self.Creneaux.setObjectName("Creneaux")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Creneaux)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabCreneaux = QtWidgets.QTableWidget(self.Creneaux)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.tabCreneaux.setFont(font)
        self.tabCreneaux.setStyleSheet("QHeaderView::section {\n"
"     border : 1px  solid black;\n"
"     padding: 0px;\n"
"     font: medium \"Cooper Black\";\n"
"     font-size: 18px;\n"
"     background : rgba(221, 103, 0,40);\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 green, stop: 0.5 yellow , stop: 1 red); \n"
"selection-color : black;\n"
"gridline-color : Gray}\n"
"\n"
"")
        self.tabCreneaux.setAlternatingRowColors(True)
        self.tabCreneaux.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabCreneaux.setRowCount(200)
        self.tabCreneaux.setColumnCount(6)
        self.tabCreneaux.setObjectName("tabCreneaux")
        item = QtWidgets.QTableWidgetItem()
        self.tabCreneaux.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabCreneaux.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabCreneaux.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabCreneaux.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabCreneaux.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabCreneaux.setHorizontalHeaderItem(5, item)
        self.tabCreneaux.horizontalHeader().setDefaultSectionSize(182)
        self.tabCreneaux.horizontalHeader().setStretchLastSection(False)
        self.tabCreneaux.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_3.addWidget(self.tabCreneaux, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nbCreneaux = QtWidgets.QLabel(self.Creneaux)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.nbCreneaux.setFont(font)
        self.nbCreneaux.setAlignment(QtCore.Qt.AlignCenter)
        self.nbCreneaux.setObjectName("nbCreneaux")
        self.horizontalLayout.addWidget(self.nbCreneaux)
        self.ajoutCreneau2 = QtWidgets.QPushButton(self.Creneaux)
        self.ajoutCreneau2.setMinimumSize(QtCore.QSize(350, 30))
        self.ajoutCreneau2.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.ajoutCreneau2.setFont(font)
        self.ajoutCreneau2.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 2px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.ajoutCreneau2.setObjectName("ajoutCreneau2")
        self.horizontalLayout.addWidget(self.ajoutCreneau2)
        self.supCreneau = QtWidgets.QPushButton(self.Creneaux)
        self.supCreneau.setMinimumSize(QtCore.QSize(350, 30))
        self.supCreneau.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.supCreneau.setFont(font)
        self.supCreneau.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 2px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.supCreneau.setObjectName("supCreneau")
        self.horizontalLayout.addWidget(self.supCreneau)
        self.scrollAtBottomC = QtWidgets.QPushButton(self.Creneaux)
        self.scrollAtBottomC.setMinimumSize(QtCore.QSize(30, 30))
        self.scrollAtBottomC.setMaximumSize(QtCore.QSize(30, 30))
        self.scrollAtBottomC.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.scrollAtBottomC.setText("")
        self.scrollAtBottomC.setObjectName("scrollAtBottomC")
        self.horizontalLayout.addWidget(self.scrollAtBottomC)
        self.scrollAtTopC = QtWidgets.QPushButton(self.Creneaux)
        self.scrollAtTopC.setMinimumSize(QtCore.QSize(30, 30))
        self.scrollAtTopC.setMaximumSize(QtCore.QSize(30, 30))
        self.scrollAtTopC.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.scrollAtTopC.setText("")
        self.scrollAtTopC.setObjectName("scrollAtTopC")
        self.horizontalLayout.addWidget(self.scrollAtTopC)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(11, 0, 5, 11)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.supRechercheCre = QtWidgets.QPushButton(self.Creneaux)
        self.supRechercheCre.setMinimumSize(QtCore.QSize(30, 30))
        self.supRechercheCre.setMaximumSize(QtCore.QSize(30, 30))
        self.supRechercheCre.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.supRechercheCre.setText("")
        self.supRechercheCre.setObjectName("supRechercheCre")
        self.horizontalLayout_10.addWidget(self.supRechercheCre)
        self.rechercheCreneaux = QtWidgets.QLineEdit(self.Creneaux)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.rechercheCreneaux.setFont(font)
        self.rechercheCreneaux.setStyleSheet("QLineEdit {\n"
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
        self.rechercheCreneaux.setObjectName("rechercheCreneaux")
        self.horizontalLayout_10.addWidget(self.rechercheCreneaux)
        self.radioCreFiltreNom = QtWidgets.QRadioButton(self.Creneaux)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.radioCreFiltreNom.setFont(font)
        self.radioCreFiltreNom.setStyleSheet("QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"    background-color : white;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked::hover{\n"
"    background-color :yellow;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"")
        self.radioCreFiltreNom.setChecked(True)
        self.radioCreFiltreNom.setObjectName("radioCreFiltreNom")
        self.horizontalLayout_10.addWidget(self.radioCreFiltreNom)
        self.radioCreFiltreCat = QtWidgets.QRadioButton(self.Creneaux)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.radioCreFiltreCat.setFont(font)
        self.radioCreFiltreCat.setStyleSheet("QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"    background-color : white;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked::hover{\n"
"    background-color :yellow;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"")
        self.radioCreFiltreCat.setObjectName("radioCreFiltreCat")
        self.horizontalLayout_10.addWidget(self.radioCreFiltreCat)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Creneaux, "")
        self.Outils = QtWidgets.QWidget()
        self.Outils.setObjectName("Outils")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Outils)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CategorieCreneaux_LAYOUT = QtWidgets.QVBoxLayout()
        self.CategorieCreneaux_LAYOUT.setContentsMargins(0, 11, 11, 11)
        self.CategorieCreneaux_LAYOUT.setSpacing(6)
        self.CategorieCreneaux_LAYOUT.setObjectName("CategorieCreneaux_LAYOUT")
        self.label = QtWidgets.QLabel(self.Outils)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.CategorieCreneaux_LAYOUT.addWidget(self.label)
        self.listCatCre = QtWidgets.QListWidget(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listCatCre.sizePolicy().hasHeightForWidth())
        self.listCatCre.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.listCatCre.setFont(font)
        self.listCatCre.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.listCatCre.setAlternatingRowColors(True)
        self.listCatCre.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listCatCre.setObjectName("listCatCre")
        self.CategorieCreneaux_LAYOUT.addWidget(self.listCatCre)
        self.categorieSup = QtWidgets.QLineEdit(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categorieSup.sizePolicy().hasHeightForWidth())
        self.categorieSup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.categorieSup.setFont(font)
        self.categorieSup.setStyleSheet("QLineEdit {\n"
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
        self.categorieSup.setInputMask("")
        self.categorieSup.setText("")
        self.categorieSup.setAlignment(QtCore.Qt.AlignCenter)
        self.categorieSup.setObjectName("categorieSup")
        self.CategorieCreneaux_LAYOUT.addWidget(self.categorieSup)
        self.ajoutCategorie = QtWidgets.QPushButton(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ajoutCategorie.sizePolicy().hasHeightForWidth())
        self.ajoutCategorie.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ajoutCategorie.setFont(font)
        self.ajoutCategorie.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.ajoutCategorie.setObjectName("ajoutCategorie")
        self.CategorieCreneaux_LAYOUT.addWidget(self.ajoutCategorie)
        self.supCategorie = QtWidgets.QPushButton(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supCategorie.sizePolicy().hasHeightForWidth())
        self.supCategorie.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.supCategorie.setFont(font)
        self.supCategorie.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.supCategorie.setObjectName("supCategorie")
        self.CategorieCreneaux_LAYOUT.addWidget(self.supCategorie)
        self.CategorieCreneaux_LAYOUT.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.CategorieCreneaux_LAYOUT, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listHoraire = QtWidgets.QListWidget(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listHoraire.sizePolicy().hasHeightForWidth())
        self.listHoraire.setSizePolicy(sizePolicy)
        self.listHoraire.setMinimumSize(QtCore.QSize(0, 0))
        self.listHoraire.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.listHoraire.setFont(font)
        self.listHoraire.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.listHoraire.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listHoraire.setAlternatingRowColors(True)
        self.listHoraire.setObjectName("listHoraire")
        self.verticalLayout.addWidget(self.listHoraire)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.Outils_LAYOUT = QtWidgets.QVBoxLayout()
        self.Outils_LAYOUT.setContentsMargins(0, 11, 11, 11)
        self.Outils_LAYOUT.setSpacing(6)
        self.Outils_LAYOUT.setObjectName("Outils_LAYOUT")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.moyenne = QtWidgets.QLabel(self.Outils)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.moyenne.setFont(font)
        self.moyenne.setAlignment(QtCore.Qt.AlignCenter)
        self.moyenne.setObjectName("moyenne")
        self.horizontalLayout_12.addWidget(self.moyenne)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.Outils)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.quantiteCreneau = QtWidgets.QComboBox(self.Outils)
        self.quantiteCreneau.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.quantiteCreneau.setFont(font)
        self.quantiteCreneau.setStyleSheet("QComboBox{\n"
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
        self.quantiteCreneau.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.quantiteCreneau.setObjectName("quantiteCreneau")
        self.quantiteCreneau.addItem("")
        self.quantiteCreneau.addItem("")
        self.quantiteCreneau.addItem("")
        self.quantiteCreneau.addItem("")
        self.quantiteCreneau.addItem("")
        self.quantiteCreneau.addItem("")
        self.quantiteCreneau.addItem("")
        self.quantiteCreneau.addItem("")
        self.quantiteCreneau.addItem("")
        self.quantiteCreneau.addItem("")
        self.horizontalLayout_12.addWidget(self.quantiteCreneau)
        self.Outils_LAYOUT.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ajoutBenevole = QtWidgets.QPushButton(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ajoutBenevole.sizePolicy().hasHeightForWidth())
        self.ajoutBenevole.setSizePolicy(sizePolicy)
        self.ajoutBenevole.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ajoutBenevole.setFont(font)
        self.ajoutBenevole.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.ajoutBenevole.setObjectName("ajoutBenevole")
        self.horizontalLayout_4.addWidget(self.ajoutBenevole)
        self.ajoutCreneau = QtWidgets.QPushButton(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ajoutCreneau.sizePolicy().hasHeightForWidth())
        self.ajoutCreneau.setSizePolicy(sizePolicy)
        self.ajoutCreneau.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ajoutCreneau.setFont(font)
        self.ajoutCreneau.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding: 6px;}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.ajoutCreneau.setObjectName("ajoutCreneau")
        self.horizontalLayout_4.addWidget(self.ajoutCreneau)
        self.Outils_LAYOUT.addLayout(self.horizontalLayout_4)
        self.triBenevoles = QtWidgets.QGroupBox(self.Outils)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.triBenevoles.setFont(font)
        self.triBenevoles.setStyleSheet("QGroupBox{\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"QGroupBox::hover{\n"
"     border: 3px solid darkgreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"    background-color: transparent;\n"
"    subcontrol-position: top-center;\n"
"    subcontrol-origin : margin;\n"
"}\n"
"\n"
"")
        self.triBenevoles.setObjectName("triBenevoles")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.triBenevoles)
        self.gridLayout_23.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_23.setSpacing(6)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.radioTriSMax = QtWidgets.QRadioButton(self.triBenevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioTriSMax.setFont(font)
        self.radioTriSMax.setStyleSheet("QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"    background-color : white;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked::hover{\n"
"    background-color :yellow;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"")
        self.radioTriSMax.setObjectName("radioTriSMax")
        self.gridLayout_23.addWidget(self.radioTriSMax, 4, 0, 1, 1)
        self.radioTriNom = QtWidgets.QRadioButton(self.triBenevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioTriNom.setFont(font)
        self.radioTriNom.setStyleSheet("QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"    background-color : white;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked::hover{\n"
"    background-color :yellow;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"")
        self.radioTriNom.setChecked(True)
        self.radioTriNom.setObjectName("radioTriNom")
        self.gridLayout_23.addWidget(self.radioTriNom, 1, 0, 1, 1)
        self.radioTriSMin = QtWidgets.QRadioButton(self.triBenevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioTriSMin.setFont(font)
        self.radioTriSMin.setStyleSheet("QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"    background-color : white;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked::hover{\n"
"    background-color :yellow;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"")
        self.radioTriSMin.setObjectName("radioTriSMin")
        self.gridLayout_23.addWidget(self.radioTriSMin, 5, 0, 1, 1)
        self.radioTriVMin = QtWidgets.QRadioButton(self.triBenevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioTriVMin.setFont(font)
        self.radioTriVMin.setStyleSheet("QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"    background-color : white;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked::hover{\n"
"    background-color :yellow;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"")
        self.radioTriVMin.setObjectName("radioTriVMin")
        self.gridLayout_23.addWidget(self.radioTriVMin, 3, 0, 1, 1)
        self.radioTriVMax = QtWidgets.QRadioButton(self.triBenevoles)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioTriVMax.setFont(font)
        self.radioTriVMax.setStyleSheet("QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"    background-color : white;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked::hover{\n"
"    background-color :yellow;\n"
"    border-radius : 8px;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border-radius : 9px;\n"
"    border : 3px solid black;    \n"
"}\n"
"")
        self.radioTriVMax.setObjectName("radioTriVMax")
        self.gridLayout_23.addWidget(self.radioTriVMax, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem1, 0, 0, 1, 1)
        self.Outils_LAYOUT.addWidget(self.triBenevoles)
        self.respectVoeux = QtWidgets.QGroupBox(self.Outils)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.respectVoeux.setFont(font)
        self.respectVoeux.setStyleSheet("QGroupBox{\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"QGroupBox::hover{\n"
"     border: 3px solid darkgreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"    background-color: transparent;\n"
"    subcontrol-position: top-center;\n"
"    subcontrol-origin : margin;\n"
"}")
        self.respectVoeux.setObjectName("respectVoeux")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.respectVoeux)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.voeuxCreneaux = QtWidgets.QCheckBox(self.respectVoeux)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voeuxCreneaux.sizePolicy().hasHeightForWidth())
        self.voeuxCreneaux.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.voeuxCreneaux.setFont(font)
        self.voeuxCreneaux.setStyleSheet("QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked::hover{\n"
"    background-color : yellow;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"\n"
"")
        self.voeuxCreneaux.setChecked(True)
        self.voeuxCreneaux.setObjectName("voeuxCreneaux")
        self.verticalLayout_3.addWidget(self.voeuxCreneaux)
        self.voeuxArtistes = QtWidgets.QCheckBox(self.respectVoeux)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voeuxArtistes.sizePolicy().hasHeightForWidth())
        self.voeuxArtistes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.voeuxArtistes.setFont(font)
        self.voeuxArtistes.setStyleSheet("QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked::hover{\n"
"    background-color : yellow;\n"
"    border : 2px solid black;    \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed{\n"
"    background-color : yellow;\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"\n"
"")
        self.voeuxArtistes.setChecked(True)
        self.voeuxArtistes.setObjectName("voeuxArtistes")
        self.verticalLayout_3.addWidget(self.voeuxArtistes)
        self.Outils_LAYOUT.addWidget(self.respectVoeux)
        self.horaireArtistes = QtWidgets.QTableWidget(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horaireArtistes.sizePolicy().hasHeightForWidth())
        self.horaireArtistes.setSizePolicy(sizePolicy)
        self.horaireArtistes.setMinimumSize(QtCore.QSize(706, 160))
        self.horaireArtistes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.horaireArtistes.setFont(font)
        self.horaireArtistes.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.horaireArtistes.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horaireArtistes.setStyleSheet("\n"
"QHeaderView::section {\n"
"     border : 1px  solid black;\n"
"     padding: 0px;\n"
"     font: medium \"Cooper Black\";\n"
"     font-size: 18px;\n"
"     background : rgba(221, 103, 0,40);\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 green, stop: 0.5 yellow , stop: 1 red); \n"
"selection-color : black;\n"
"gridline-color : Gray}\n"
"\n"
"\n"
"\n"
"QTableWidget::hover {\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;}\n"
"\n"
"QHeaderView::section {\n"
"    padding : 5px;\n"
"    font-size: 18px;\n"
"    font : medium \"Cooper Black\";\n"
"    background : qlineargradient(spread:reflect, x1:0.499682, y1:0.5, x2:0.5, y2:0, stop:0.355932 rgba(255, 255, 255, 255), stop:0.903955 rgba(248, 82, 0, 73));\n"
"}\n"
"\n"
"")
        self.horaireArtistes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.horaireArtistes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.horaireArtistes.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.horaireArtistes.setAlternatingRowColors(True)
        self.horaireArtistes.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.horaireArtistes.setObjectName("horaireArtistes")
        self.horaireArtistes.setColumnCount(2)
        self.horaireArtistes.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        item.setFont(font)
        self.horaireArtistes.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        item.setFont(font)
        self.horaireArtistes.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        item.setFont(font)
        self.horaireArtistes.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        item.setFont(font)
        self.horaireArtistes.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        item.setFont(font)
        self.horaireArtistes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        item.setFont(font)
        self.horaireArtistes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.horaireArtistes.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.horaireArtistes.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.horaireArtistes.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.horaireArtistes.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.horaireArtistes.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.horaireArtistes.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.horaireArtistes.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.horaireArtistes.setItem(3, 1, item)
        self.horaireArtistes.horizontalHeader().setDefaultSectionSize(330)
        self.horaireArtistes.verticalHeader().setDefaultSectionSize(35)
        self.Outils_LAYOUT.addWidget(self.horaireArtistes)
        self.progressBarV = QtWidgets.QProgressBar(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBarV.sizePolicy().hasHeightForWidth())
        self.progressBarV.setSizePolicy(sizePolicy)
        self.progressBarV.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.progressBarV.setFont(font)
        self.progressBarV.setStyleSheet("QProgressBar {\n"
"    border: 3px solid grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.0511364, y2:0.034, stop:0 rgba(255, 255, 255, 255), stop:0.965909 rgba(0, 156, 0, 167));\n"
"    margin : 0.5px;\n"
"    width : 12px\n"
"}")
        self.progressBarV.setProperty("value", 50)
        self.progressBarV.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBarV.setTextVisible(True)
        self.progressBarV.setInvertedAppearance(False)
        self.progressBarV.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBarV.setObjectName("progressBarV")
        self.Outils_LAYOUT.addWidget(self.progressBarV)
        self.progressBarS = QtWidgets.QProgressBar(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBarS.sizePolicy().hasHeightForWidth())
        self.progressBarS.setSizePolicy(sizePolicy)
        self.progressBarS.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.progressBarS.setFont(font)
        self.progressBarS.setStyleSheet("QProgressBar {\n"
"    border: 3px solid grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 0, 138));\n"
"    margin : 0.5px;\n"
"    width : 12px\n"
"}")
        self.progressBarS.setProperty("value", 50)
        self.progressBarS.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBarS.setObjectName("progressBarS")
        self.Outils_LAYOUT.addWidget(self.progressBarS)
        self.progressBarT = QtWidgets.QProgressBar(self.Outils)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBarT.sizePolicy().hasHeightForWidth())
        self.progressBarT.setSizePolicy(sizePolicy)
        self.progressBarT.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.progressBarT.setFont(font)
        self.progressBarT.setStyleSheet("QProgressBar {\n"
"    border: 3px solid grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 66));\n"
"    margin : 0.5px;\n"
"    width : 12px\n"
"}")
        self.progressBarT.setProperty("value", 50)
        self.progressBarT.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBarT.setObjectName("progressBarT")
        self.Outils_LAYOUT.addWidget(self.progressBarT)
        self.gridLayout_2.addLayout(self.Outils_LAYOUT, 0, 2, 1, 1)
        self.tabWidget.addTab(self.Outils, "")
        self.ResumeVendredi = QtWidgets.QWidget()
        self.ResumeVendredi.setStyleSheet("")
        self.ResumeVendredi.setObjectName("ResumeVendredi")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ResumeVendredi)
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_6.setSpacing(3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.list0CreneauV = QtWidgets.QListWidget(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list0CreneauV.setFont(font)
        self.list0CreneauV.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list0CreneauV.setAlternatingRowColors(True)
        self.list0CreneauV.setObjectName("list0CreneauV")
        self.verticalLayout_2.addWidget(self.list0CreneauV)
        self.allVen0 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allVen0.setFont(font)
        self.allVen0.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allVen0.setObjectName("allVen0")
        self.verticalLayout_2.addWidget(self.allVen0)
        self.noneVen0 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneVen0.setFont(font)
        self.noneVen0.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneVen0.setObjectName("noneVen0")
        self.verticalLayout_2.addWidget(self.noneVen0)
        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.list1CreneauV = QtWidgets.QListWidget(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list1CreneauV.setFont(font)
        self.list1CreneauV.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list1CreneauV.setAlternatingRowColors(True)
        self.list1CreneauV.setObjectName("list1CreneauV")
        self.verticalLayout_8.addWidget(self.list1CreneauV)
        self.allVen1 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allVen1.setFont(font)
        self.allVen1.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allVen1.setObjectName("allVen1")
        self.verticalLayout_8.addWidget(self.allVen1)
        self.noneVen1 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneVen1.setFont(font)
        self.noneVen1.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneVen1.setObjectName("noneVen1")
        self.verticalLayout_8.addWidget(self.noneVen1)
        self.gridLayout_6.addLayout(self.verticalLayout_8, 0, 1, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.list2CreneauV = QtWidgets.QListWidget(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list2CreneauV.setFont(font)
        self.list2CreneauV.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list2CreneauV.setAlternatingRowColors(True)
        self.list2CreneauV.setObjectName("list2CreneauV")
        self.verticalLayout_9.addWidget(self.list2CreneauV)
        self.allVen2 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allVen2.setFont(font)
        self.allVen2.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allVen2.setObjectName("allVen2")
        self.verticalLayout_9.addWidget(self.allVen2)
        self.noneVen2 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneVen2.setFont(font)
        self.noneVen2.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneVen2.setObjectName("noneVen2")
        self.verticalLayout_9.addWidget(self.noneVen2)
        self.gridLayout_6.addLayout(self.verticalLayout_9, 0, 2, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.list3CreneauV = QtWidgets.QListWidget(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list3CreneauV.setFont(font)
        self.list3CreneauV.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list3CreneauV.setAlternatingRowColors(True)
        self.list3CreneauV.setObjectName("list3CreneauV")
        self.verticalLayout_10.addWidget(self.list3CreneauV)
        self.allVen3 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allVen3.setFont(font)
        self.allVen3.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allVen3.setObjectName("allVen3")
        self.verticalLayout_10.addWidget(self.allVen3)
        self.noneVen3 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneVen3.setFont(font)
        self.noneVen3.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneVen3.setObjectName("noneVen3")
        self.verticalLayout_10.addWidget(self.noneVen3)
        self.gridLayout_6.addLayout(self.verticalLayout_10, 0, 3, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_11.addWidget(self.label_11)
        self.list4CreneauV = QtWidgets.QListWidget(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list4CreneauV.setFont(font)
        self.list4CreneauV.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list4CreneauV.setAlternatingRowColors(True)
        self.list4CreneauV.setObjectName("list4CreneauV")
        self.verticalLayout_11.addWidget(self.list4CreneauV)
        self.allVen4 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allVen4.setFont(font)
        self.allVen4.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allVen4.setObjectName("allVen4")
        self.verticalLayout_11.addWidget(self.allVen4)
        self.noneVen4 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneVen4.setFont(font)
        self.noneVen4.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneVen4.setObjectName("noneVen4")
        self.verticalLayout_11.addWidget(self.noneVen4)
        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 4, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_12.addWidget(self.label_9)
        self.list5CreneauV = QtWidgets.QListWidget(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list5CreneauV.setFont(font)
        self.list5CreneauV.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list5CreneauV.setAlternatingRowColors(True)
        self.list5CreneauV.setObjectName("list5CreneauV")
        self.verticalLayout_12.addWidget(self.list5CreneauV)
        self.allVen5 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allVen5.setFont(font)
        self.allVen5.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allVen5.setObjectName("allVen5")
        self.verticalLayout_12.addWidget(self.allVen5)
        self.noneVen5 = QtWidgets.QPushButton(self.ResumeVendredi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneVen5.setFont(font)
        self.noneVen5.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneVen5.setObjectName("noneVen5")
        self.verticalLayout_12.addWidget(self.noneVen5)
        self.gridLayout_6.addLayout(self.verticalLayout_12, 0, 5, 1, 1)
        self.tabWidget.addTab(self.ResumeVendredi, "")
        self.ResumeSamedi = QtWidgets.QWidget()
        self.ResumeSamedi.setObjectName("ResumeSamedi")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.ResumeSamedi)
        self.gridLayout_22.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_22.setSpacing(3)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_14.addWidget(self.label_14)
        self.list0CreneauS = QtWidgets.QListWidget(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list0CreneauS.setFont(font)
        self.list0CreneauS.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list0CreneauS.setAlternatingRowColors(True)
        self.list0CreneauS.setObjectName("list0CreneauS")
        self.verticalLayout_14.addWidget(self.list0CreneauS)
        self.allSam0 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allSam0.setFont(font)
        self.allSam0.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allSam0.setObjectName("allSam0")
        self.verticalLayout_14.addWidget(self.allSam0)
        self.noneSam0 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneSam0.setFont(font)
        self.noneSam0.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneSam0.setObjectName("noneSam0")
        self.verticalLayout_14.addWidget(self.noneSam0)
        self.gridLayout_22.addLayout(self.verticalLayout_14, 0, 0, 1, 1)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_18.addWidget(self.label_17)
        self.list5CreneauS = QtWidgets.QListWidget(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list5CreneauS.setFont(font)
        self.list5CreneauS.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list5CreneauS.setAlternatingRowColors(True)
        self.list5CreneauS.setObjectName("list5CreneauS")
        self.verticalLayout_18.addWidget(self.list5CreneauS)
        self.allSam5 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allSam5.setFont(font)
        self.allSam5.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allSam5.setObjectName("allSam5")
        self.verticalLayout_18.addWidget(self.allSam5)
        self.noneSam5 = QtWidgets.QPushButton(self.ResumeSamedi)
        self.noneSam5.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneSam5.setFont(font)
        self.noneSam5.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneSam5.setObjectName("noneSam5")
        self.verticalLayout_18.addWidget(self.noneSam5)
        self.gridLayout_22.addLayout(self.verticalLayout_18, 0, 5, 1, 1)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_16.addWidget(self.label_13)
        self.list3CreneauS = QtWidgets.QListWidget(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list3CreneauS.setFont(font)
        self.list3CreneauS.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list3CreneauS.setAlternatingRowColors(True)
        self.list3CreneauS.setObjectName("list3CreneauS")
        self.verticalLayout_16.addWidget(self.list3CreneauS)
        self.allSam3 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allSam3.setFont(font)
        self.allSam3.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allSam3.setObjectName("allSam3")
        self.verticalLayout_16.addWidget(self.allSam3)
        self.noneSam3 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneSam3.setFont(font)
        self.noneSam3.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneSam3.setObjectName("noneSam3")
        self.verticalLayout_16.addWidget(self.noneSam3)
        self.gridLayout_22.addLayout(self.verticalLayout_16, 0, 3, 1, 1)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_15 = QtWidgets.QLabel(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_15.addWidget(self.label_15)
        self.list2CreneauS = QtWidgets.QListWidget(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list2CreneauS.setFont(font)
        self.list2CreneauS.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list2CreneauS.setAlternatingRowColors(True)
        self.list2CreneauS.setObjectName("list2CreneauS")
        self.verticalLayout_15.addWidget(self.list2CreneauS)
        self.allSam2 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allSam2.setFont(font)
        self.allSam2.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allSam2.setObjectName("allSam2")
        self.verticalLayout_15.addWidget(self.allSam2)
        self.noneSam2 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneSam2.setFont(font)
        self.noneSam2.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneSam2.setObjectName("noneSam2")
        self.verticalLayout_15.addWidget(self.noneSam2)
        self.gridLayout_22.addLayout(self.verticalLayout_15, 0, 2, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_13.addWidget(self.label_12)
        self.list1CreneauS = QtWidgets.QListWidget(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list1CreneauS.setFont(font)
        self.list1CreneauS.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list1CreneauS.setAlternatingRowColors(True)
        self.list1CreneauS.setObjectName("list1CreneauS")
        self.verticalLayout_13.addWidget(self.list1CreneauS)
        self.allSam1 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allSam1.setFont(font)
        self.allSam1.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allSam1.setObjectName("allSam1")
        self.verticalLayout_13.addWidget(self.allSam1)
        self.noneSam1 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneSam1.setFont(font)
        self.noneSam1.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneSam1.setObjectName("noneSam1")
        self.verticalLayout_13.addWidget(self.noneSam1)
        self.gridLayout_22.addLayout(self.verticalLayout_13, 0, 1, 1, 1)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_17.addWidget(self.label_16)
        self.list4CreneauS = QtWidgets.QListWidget(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.list4CreneauS.setFont(font)
        self.list4CreneauS.setStyleSheet("QListWidget{background-color: white; alternate-background-color: rgb(255, 255, 160);\n"
"     border: 3px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"    selection-background : qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    selection-color : black\n"
"}\n"
"\n"
"QListWidget::hover{\n"
"     border: 3px solid darkGreen;\n"
"     border-radius: 10px;\n"
"     padding: 0px;\n"
"}\n"
"\n"
"QListWidget::item::hover{\n"
"    background :qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.039548 rgba(0, 156, 0, 80), stop:0.966102 rgba(0, 156, 0, 80), stop:1 rgba(0, 0, 0, 255));\n"
"    color: black;\n"
"    border : 1px solid black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QListWidget::indicator::checked{\n"
"    background-color : qlineargradient(spread:reflect, x1:0.1, y1:0.1, x2:0.5, y2:0.5, stop:0.801136 rgba(255, 255, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    border : 3px solid black;    \n"
"}\n"
"\n"
"QListWidget::indicator::unchecked{\n"
"    background-color : white;\n"
"    border : 2px solid black;    \n"
"}")
        self.list4CreneauS.setAlternatingRowColors(True)
        self.list4CreneauS.setObjectName("list4CreneauS")
        self.verticalLayout_17.addWidget(self.list4CreneauS)
        self.allSam4 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.allSam4.setFont(font)
        self.allSam4.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.allSam4.setObjectName("allSam4")
        self.verticalLayout_17.addWidget(self.allSam4)
        self.noneSam4 = QtWidgets.QPushButton(self.ResumeSamedi)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        self.noneSam4.setFont(font)
        self.noneSam4.setStyleSheet("QPushButton{   \n"
"     background-color: qlineargradient(spread:pad, x1:0.738227, y1:0.278, x2:0, y2:1, stop:0 rgba(255, 255, 255, 0), stop:0.710227 rgba(255, 255, 0, 255));   \n"
"     border-style: outset;    \n"
"     border: 3px solid black;\n"
"     border-radius: 10px;       \n"
"    padding-top: 6px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton::hover{   background-color: yellow;    border-style: inset;  border-color: darkGreen }\n"
"QPushButton::pressed {    background-color: yellow;    border-style: inset; border-color:beige }")
        self.noneSam4.setObjectName("noneSam4")
        self.verticalLayout_17.addWidget(self.noneSam4)
        self.gridLayout_22.addLayout(self.verticalLayout_17, 0, 4, 1, 1)
        self.tabWidget.addTab(self.ResumeSamedi, "")
        self.gridLayout_9.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1191, 25))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.menuFichier = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.menuFichier.setFont(font)
        self.menuFichier.setObjectName("menuFichier")
        self.menuCalcul_Auto = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.menuCalcul_Auto.setFont(font)
        self.menuCalcul_Auto.setObjectName("menuCalcul_Auto")
        self.menuAffichage = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.menuAffichage.setFont(font)
        self.menuAffichage.setObjectName("menuAffichage")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        self.mainToolBar.setFont(font)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.statusBar.setFont(font)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.actionQuitter.setFont(font)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionImport = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.actionImport.setFont(font)
        self.actionImport.setObjectName("actionImport")
        self.actionEnSavoirPlus = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.actionEnSavoirPlus.setFont(font)
        self.actionEnSavoirPlus.setObjectName("actionEnSavoirPlus")
        self.actionEnregistrer = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setKerning(False)
        self.actionEnregistrer.setFont(font)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionExport = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.actionExport.setFont(font)
        self.actionExport.setObjectName("actionExport")
        self.actionCalculAuto = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.actionCalculAuto.setFont(font)
        self.actionCalculAuto.setObjectName("actionCalculAuto")
        self.actionReinitialiser = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.actionReinitialiser.setFont(font)
        self.actionReinitialiser.setObjectName("actionReinitialiser")
        self.actionZoom = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.actionZoom.setFont(font)
        self.actionZoom.setObjectName("actionZoom")
        self.actionDezoomer = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.actionDezoomer.setFont(font)
        self.actionDezoomer.setObjectName("actionDezoomer")
        self.actionResetPolice = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.actionResetPolice.setFont(font)
        self.actionResetPolice.setObjectName("actionResetPolice")
        self.actionDerniereSvg = QtWidgets.QAction(MainWindow)
        self.actionDerniereSvg.setObjectName("actionDerniereSvg")
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuFichier.addAction(self.actionReinitialiser)
        self.menuFichier.addAction(self.actionDerniereSvg)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionImport)
        self.menuFichier.addAction(self.actionExport)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuCalcul_Auto.addAction(self.actionCalculAuto)
        self.menuAffichage.addAction(self.actionZoom)
        self.menuAffichage.addAction(self.actionDezoomer)
        self.menuAffichage.addSeparator()
        self.menuAffichage.addAction(self.actionResetPolice)
        self.menuBar.addAction(self.menuFichier.menuAction())
        self.menuBar.addAction(self.menuCalcul_Auto.menuAction())
        self.menuBar.addAction(self.menuAffichage.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.quantiteCreneau.setCurrentIndex(3)
        self.scrollAtTopV.clicked.connect(self.creneauVendredi.scrollToTop)
        self.scrollAtBottomB.clicked.connect(self.tabBenevoles.scrollToBottom)
        self.scrollAtTopS.clicked.connect(self.creneauSamedi.scrollToTop)
        self.scrollAtTopB.clicked.connect(self.tabBenevoles.scrollToTop)
        self.scrollAtBottomS.clicked.connect(self.creneauSamedi.scrollToBottom)
        self.categorieSup.returnPressed.connect(self.ajoutCategorie.click)
        self.scrollAtTopC.clicked.connect(self.tabCreneaux.scrollToTop)
        self.supRechercheBene.clicked.connect(self.rechercheBenevoles.clear)
        self.supRechercheCre.clicked.connect(self.rechercheCreneaux.clear)
        self.scrollAtBottomV.clicked.connect(self.creneauVendredi.scrollToBottom)
        self.scrollAtBottomC.clicked.connect(self.tabCreneaux.scrollToBottom)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Creneaux Meuh Folle"))
        MainWindow.setStatusTip(_translate("MainWindow", "Meuh Folle 2017 - Best Meuh Folle Ever"))
        self.tabWidget.setStatusTip(_translate("MainWindow", "Meuh Folle 2017 - Best Meuh Folle Ever"))
        self.rechercheV.setItemText(0, _translate("MainWindow", "Aucun"))
        self.NbCBeneV.setText(_translate("MainWindow", "Aucun bénévole sélectionné"))
        item = self.ResumeBenevoleV.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Voeux :"))
        item = self.ResumeBenevoleV.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Remarque : "))
        item = self.ResumeBenevoleV.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Categorie 1"))
        item = self.ResumeBenevoleV.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Categorie 2"))
        item = self.ResumeBenevoleV.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Categorie 3"))
        item = self.ResumeBenevoleV.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Artiste Vendredi"))
        item = self.creneauVendredi.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "09H-10H"))
        item = self.creneauVendredi.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "10H-11H"))
        item = self.creneauVendredi.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "11H-12H"))
        item = self.creneauVendredi.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "12H-13H"))
        item = self.creneauVendredi.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "13H-14H"))
        item = self.creneauVendredi.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "14H-15H"))
        item = self.creneauVendredi.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "15H-16H"))
        item = self.creneauVendredi.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "16H-17H"))
        item = self.creneauVendredi.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "17H-18H"))
        item = self.creneauVendredi.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "18H-19H"))
        item = self.creneauVendredi.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "19H-20H"))
        item = self.creneauVendredi.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "20H-21H"))
        item = self.creneauVendredi.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "21H-22H"))
        item = self.creneauVendredi.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "22H-23H"))
        item = self.creneauVendredi.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "23H-00H"))
        item = self.creneauVendredi.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "00H-01H"))
        item = self.creneauVendredi.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "01H-02H"))
        item = self.creneauVendredi.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "02H-03H"))
        item = self.creneauVendredi.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "03H-04H"))
        item = self.creneauVendredi.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "04H-05H"))
        item = self.creneauVendredi.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "05H-06H"))
        item = self.creneauVendredi.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "06H-07H"))
        item = self.creneauVendredi.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "07H-08H"))
        item = self.creneauVendredi.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "08H-09H"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vendredi), _translate("MainWindow", "Vendredi"))
        self.rechercheS.setItemText(0, _translate("MainWindow", "Aucun"))
        self.NbCBeneS.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.NbCBeneS.setText(_translate("MainWindow", "Aucun bénévole sélectionné"))
        item = self.ResumeBenevoleS.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Voeux :"))
        item = self.ResumeBenevoleS.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Remarque :"))
        item = self.ResumeBenevoleS.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Categorie 1"))
        item = self.ResumeBenevoleS.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Categorie 2"))
        item = self.ResumeBenevoleS.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Categorie 3"))
        item = self.ResumeBenevoleS.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Artiste Samedi"))
        item = self.creneauSamedi.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "09H-10H"))
        item = self.creneauSamedi.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "10H-11H"))
        item = self.creneauSamedi.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "11H-12H"))
        item = self.creneauSamedi.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "12H-13H"))
        item = self.creneauSamedi.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "13H-14H"))
        item = self.creneauSamedi.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "14H-15H"))
        item = self.creneauSamedi.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "15H-16H"))
        item = self.creneauSamedi.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "16H-17H"))
        item = self.creneauSamedi.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "17H-18H"))
        item = self.creneauSamedi.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "18H-19H"))
        item = self.creneauSamedi.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "19H-20H"))
        item = self.creneauSamedi.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "20H-21H"))
        item = self.creneauSamedi.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "21H-22H"))
        item = self.creneauSamedi.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "22H-23H"))
        item = self.creneauSamedi.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "23H-00H"))
        item = self.creneauSamedi.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "00H-01H"))
        item = self.creneauSamedi.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "01H-02H"))
        item = self.creneauSamedi.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "02H-03H"))
        item = self.creneauSamedi.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "03H-04H"))
        item = self.creneauSamedi.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "04H-05H"))
        item = self.creneauSamedi.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "05H-06H"))
        item = self.creneauSamedi.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "06H-07H"))
        item = self.creneauSamedi.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "07H-08H"))
        item = self.creneauSamedi.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "08H-09H"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.samedi), _translate("MainWindow", "Samedi"))
        self.nbBenevoles.setText(_translate("MainWindow", "Nombre de benevoles : 0"))
        self.ajoutBenevole2.setText(_translate("MainWindow", "Ajouter un bénévole"))
        self.supBenevole.setText(_translate("MainWindow", "Supprimer un bénévole"))
        self.tabBenevoles.setSortingEnabled(False)
        item = self.tabBenevoles.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nom Prenom"))
        item = self.tabBenevoles.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Voeux 1"))
        item = self.tabBenevoles.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Voeux 2"))
        item = self.tabBenevoles.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Voeux 3"))
        item = self.tabBenevoles.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Artiste Vendredi"))
        item = self.tabBenevoles.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Artistes Samedi"))
        item = self.tabBenevoles.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Remarques"))
        item = self.tabBenevoles.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Creneaux Vendredi"))
        item = self.tabBenevoles.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Creneaux Samedi"))
        item = self.tabBenevoles.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Nb Creneaux Vendredi"))
        item = self.tabBenevoles.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Nb Creneaux Samedi"))
        self.rechercheBenevoles.setPlaceholderText(_translate("MainWindow", "Rechercher un bénévole par nom ou prénom"))
        self.radioFiltreNom.setText(_translate("MainWindow", "Nom prénom"))
        self.radioFiltreCat.setText(_translate("MainWindow", "Categorie"))
        self.radioFiltreArtiste.setText(_translate("MainWindow", "Artiste"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Benevoles), _translate("MainWindow", "Benevoles"))
        self.tabCreneaux.setSortingEnabled(False)
        item = self.tabCreneaux.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tabCreneaux.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Plage Horaire"))
        item = self.tabCreneaux.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Duree"))
        item = self.tabCreneaux.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Categorie"))
        item = self.tabCreneaux.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Benevoles Vendredi"))
        item = self.tabCreneaux.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Benevoles Samedi"))
        self.nbCreneaux.setText(_translate("MainWindow", "Nombre de creneaux : 0"))
        self.ajoutCreneau2.setText(_translate("MainWindow", "Ajouter un creneau"))
        self.supCreneau.setText(_translate("MainWindow", "Supprimer un creneau"))
        self.rechercheCreneaux.setPlaceholderText(_translate("MainWindow", "Rechercher un créneau par nom"))
        self.radioCreFiltreNom.setText(_translate("MainWindow", "Nom"))
        self.radioCreFiltreCat.setText(_translate("MainWindow", "Categorie"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Creneaux), _translate("MainWindow", "Creneaux"))
        self.label.setText(_translate("MainWindow", "Catégorie de Créneaux"))
        self.listCatCre.setStatusTip(_translate("MainWindow", "Les catégories cochées apparaitront dans les tableaux Vendredi et Samedi"))
        self.categorieSup.setToolTip(_translate("MainWindow", "Ajouter une nouvelle categorie"))
        self.categorieSup.setStatusTip(_translate("MainWindow", "Entrer ici une nouvelle catégorie de créneau"))
        self.categorieSup.setPlaceholderText(_translate("MainWindow", "Nouvelle catégorie"))
        self.ajoutCategorie.setStatusTip(_translate("MainWindow", "Valider l\'ajout (Touche entrée)"))
        self.ajoutCategorie.setText(_translate("MainWindow", "Ajouter catégorie"))
        self.supCategorie.setStatusTip(_translate("MainWindow", "Supprimer la catégorie séléctionnée"))
        self.supCategorie.setText(_translate("MainWindow", "Supprimer catégorie"))
        self.label_2.setText(_translate("MainWindow", "Horaires"))
        self.listHoraire.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.listHoraire.setStatusTip(_translate("MainWindow", "Les horaires cochés apparaitront dans les tableaux Vendredi et Samedi"))
        self.listHoraire.setSortingEnabled(False)
        self.moyenne.setStatusTip(_translate("MainWindow", "Nombre de d\'heure moyen par jour par bénévole"))
        self.moyenne.setText(_translate("MainWindow", "Moyenne :"))
        self.label_3.setText(_translate("MainWindow", "Nombre de créneaux par bénévole :"))
        self.quantiteCreneau.setStatusTip(_translate("MainWindow", "Choix du nombre d\'heure maximum par jour par bénévole"))
        self.quantiteCreneau.setItemText(0, _translate("MainWindow", "1"))
        self.quantiteCreneau.setItemText(1, _translate("MainWindow", "2"))
        self.quantiteCreneau.setItemText(2, _translate("MainWindow", "3"))
        self.quantiteCreneau.setItemText(3, _translate("MainWindow", "4"))
        self.quantiteCreneau.setItemText(4, _translate("MainWindow", "5"))
        self.quantiteCreneau.setItemText(5, _translate("MainWindow", "6"))
        self.quantiteCreneau.setItemText(6, _translate("MainWindow", "7"))
        self.quantiteCreneau.setItemText(7, _translate("MainWindow", "8"))
        self.quantiteCreneau.setItemText(8, _translate("MainWindow", "9"))
        self.quantiteCreneau.setItemText(9, _translate("MainWindow", "10"))
        self.ajoutBenevole.setStatusTip(_translate("MainWindow", "Ajouter un nouveau bénévole"))
        self.ajoutBenevole.setText(_translate("MainWindow", "Ajouter Bénévole"))
        self.ajoutCreneau.setStatusTip(_translate("MainWindow", "Ajouter un nouveau créneau"))
        self.ajoutCreneau.setText(_translate("MainWindow", "Ajouter Créneau"))
        self.triBenevoles.setStatusTip(_translate("MainWindow", "Option de tri du tableau Bénévoles"))
        self.triBenevoles.setTitle(_translate("MainWindow", "Tri du tableau bénévoles par :"))
        self.radioTriSMax.setText(_translate("MainWindow", "Nombre de créneaux du Samedi (10 --> 0)"))
        self.radioTriNom.setText(_translate("MainWindow", "Nom Prénom"))
        self.radioTriSMin.setText(_translate("MainWindow", "Nombre de créneaux du Samedi (0 --> 10)"))
        self.radioTriVMin.setText(_translate("MainWindow", "Nombre de créneaux du Vendredi (0 --> 10)"))
        self.radioTriVMax.setText(_translate("MainWindow", "Nombre de créneaux du Vendredi (10 --> 0)"))
        self.respectVoeux.setStatusTip(_translate("MainWindow", "Respect ou non des choix de catégorie de créneaux et/ou d\'artistes"))
        self.respectVoeux.setTitle(_translate("MainWindow", "Permet d\'outrepasser les demandes des bénévoles"))
        self.voeuxCreneaux.setText(_translate("MainWindow", "Respecter les voeux de créneaux"))
        self.voeuxArtistes.setText(_translate("MainWindow", "Respecter les voeux d\'artistes"))
        self.horaireArtistes.setStatusTip(_translate("MainWindow", "Remplir par la programmation (Eviter les accents, Respecter la même casse que le formulaire)"))
        self.horaireArtistes.setSortingEnabled(False)
        item = self.horaireArtistes.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "19h-21h"))
        item = self.horaireArtistes.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "21h-23h"))
        item = self.horaireArtistes.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "23h-01h"))
        item = self.horaireArtistes.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "01h-03h"))
        item = self.horaireArtistes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Artistes du Vendredi"))
        item = self.horaireArtistes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Artistes du Samedi"))
        __sortingEnabled = self.horaireArtistes.isSortingEnabled()
        self.horaireArtistes.setSortingEnabled(False)
        self.horaireArtistes.setSortingEnabled(__sortingEnabled)
        self.progressBarV.setStatusTip(_translate("MainWindow", "Avancement du Vendredi"))
        self.progressBarV.setFormat(_translate("MainWindow", "%p%"))
        self.progressBarS.setStatusTip(_translate("MainWindow", "Avancement du Samedi"))
        self.progressBarT.setStatusTip(_translate("MainWindow", "Avancement Total"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Outils), _translate("MainWindow", "Outils"))
        self.ResumeVendredi.setStatusTip(_translate("MainWindow", "Les Bénévoles apparaissent ici en résumé par nombre de Créneaux. Les bénévoles décochés n\'apparaitront pas dans les choix du tableau Vendredi"))
        self.label_6.setText(_translate("MainWindow", "Aucun Créneau"))
        self.allVen0.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneVen0.setText(_translate("MainWindow", "Tout désélectionner"))
        self.label_7.setText(_translate("MainWindow", "1 Créneau"))
        self.allVen1.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneVen1.setText(_translate("MainWindow", "Tout désélectionner"))
        self.label_10.setText(_translate("MainWindow", "2 Créneaux"))
        self.allVen2.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneVen2.setText(_translate("MainWindow", "Tout désélectionner"))
        self.label_8.setText(_translate("MainWindow", "3 Créneaux"))
        self.allVen3.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneVen3.setText(_translate("MainWindow", "Tout désélectionner"))
        self.label_11.setText(_translate("MainWindow", "4 Créneaux"))
        self.allVen4.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneVen4.setText(_translate("MainWindow", "Tout désélectionner"))
        self.label_9.setText(_translate("MainWindow", "5 Créneaux et plus"))
        self.allVen5.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneVen5.setText(_translate("MainWindow", "Tout désélectionner"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ResumeVendredi), _translate("MainWindow", "Resume Vendredi"))
        self.ResumeSamedi.setStatusTip(_translate("MainWindow", "Les Bénévoles apparaissent ici en résumé par nombre de Créneaux. Les bénévoles décochés n\'apparaitront pas dans les choix du tableau Samedi"))
        self.label_14.setText(_translate("MainWindow", "Aucun Créneau"))
        self.allSam0.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneSam0.setText(_translate("MainWindow", "Tout désélectionner"))
        self.label_17.setText(_translate("MainWindow", "5 Créneaux et plus"))
        self.allSam5.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneSam5.setText(_translate("MainWindow", "Tout désélectionner"))
        self.label_13.setText(_translate("MainWindow", "3 Créneaux"))
        self.allSam3.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneSam3.setText(_translate("MainWindow", "Tout désélectionner"))
        self.label_15.setText(_translate("MainWindow", "2 Créneaux"))
        self.allSam2.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneSam2.setText(_translate("MainWindow", "Tout désélectionner"))
        self.label_12.setText(_translate("MainWindow", "1 Créneau"))
        self.allSam1.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneSam1.setText(_translate("MainWindow", "Tout désélectionner"))
        self.label_16.setText(_translate("MainWindow", "4 Créneaux"))
        self.allSam4.setText(_translate("MainWindow", "Tout sélectionner"))
        self.noneSam4.setText(_translate("MainWindow", "Tout désélectionner"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ResumeSamedi), _translate("MainWindow", "Resume Samedi"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuCalcul_Auto.setTitle(_translate("MainWindow", "Calcul Auto"))
        self.menuAffichage.setTitle(_translate("MainWindow", "Affichage"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionQuitter.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionImport.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionEnSavoirPlus.setText(_translate("MainWindow", "En savoir plus"))
        self.actionEnregistrer.setText(_translate("MainWindow", "Enregistrer"))
        self.actionEnregistrer.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExport.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionCalculAuto.setText(_translate("MainWindow", "Calcul Auto"))
        self.actionCalculAuto.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionReinitialiser.setText(_translate("MainWindow", "Reinitialiser"))
        self.actionReinitialiser.setShortcut(_translate("MainWindow", "Ctrl+Alt+Z"))
        self.actionZoom.setText(_translate("MainWindow", "Agrandir Police"))
        self.actionZoom.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.actionDezoomer.setText(_translate("MainWindow", "Réduire Police"))
        self.actionDezoomer.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionResetPolice.setText(_translate("MainWindow", "Police par défaut"))
        self.actionResetPolice.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.actionDerniereSvg.setText(_translate("MainWindow", "Derniere sauvegarde"))
        self.actionDerniereSvg.setShortcut(_translate("MainWindow", "Ctrl+Z"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

