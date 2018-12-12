# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 17:42:25 2017
²
@author: GANJO
"""

#!/usr/bin/python3
# -*- coding: utf-8 -*-



import sys
import os
import time

from PyQt5 import QtWidgets , QtGui, QtCore
from PyQt5.QtCore import QSettings as Qst

import svg_donnees as Svg
import MessBox as M

from creneaux import Creneaux
from benevoles import Benevoles

from Jour import Jour
from resume import Resume

from functools import partial

import fenetre_principale_UI  # import du fichier UImainwindow.py généré par pyuic5 (Qt Creator)
import choix_benevole_DI
import ajout_creneau_DI
import ajout_benevole_DI


PATH = os.getcwd()
FOLDER_IMG= os.path.join(PATH,"Image")
OPTION = os.path.join(PATH,"doc","__init.ini")

IMG_CROIX = os.path.join(FOLDER_IMG,"croix.png")
IMG_FLECHE_BAS = os.path.join(FOLDER_IMG,"flecheverslebas.png")
IMG_FLECHE_HAUT = os.path.join(FOLDER_IMG,"flecheverslehaut.png")
IMG_LANCEMENT = os.path.join(FOLDER_IMG,"lancement.png")
IMG_ICON = os.path.join(FOLDER_IMG,"icon.png")

DEFAULT_POLICE_SIZE = 11

HORAIRE = ["09H-10H", "10H-11H", "11H-12H", "12H-13H", "13H-14H", "14H-15H", "15H-16H", "16H-17H",
           "17H-18H", "18H-19H", "19H-20H", "20H-21H", "21H-22H", "22H-23H", "23H-00H", "00H-01H", "01H-02H", "02H-03H",
           "03H-04H", "04H-05H", "05H-06H", "06H-07H", "07H-08H", "08H-09H"]

def remplir_tab_resume(tableau,label,benevole,jour):
    item = M.item_normal_non_editable(benevole.cre1)
    tableau.setItem(0,0,item)
    item = M.item_normal_non_editable(benevole.cre2)
    tableau.setItem(0,1,item)
    item = M.item_normal_non_editable(benevole.cre3)
    tableau.setItem(0,2,item)
    if jour == "V" :
        item = M.item_normal_non_editable(benevole.artiste_vendredi)
    elif jour == "S":
        item = M.item_normal_non_editable(benevole.artiste_samedi)
    tableau.setItem(0,3,item)
    item = M.item_normal_non_editable(benevole.remarques)
    tableau.setSpan(1,0,1,4)
    tableau.setItem(1,0,item)
    if jour == "V" :
        label.setText(benevole.nom + " : {}h de creneau".format(len(benevole.creneaux_vendredi)))
    elif jour == "S" :
        label.setText(benevole.nom + " : {}h de creneau".format(len(benevole.creneaux_samedi)))

def set_valeur_combobox(index, tab):
        MyWindow.ETAT_SVG = False
        row = tab.currentRow()
        column = tab.currentColumn()
        item = M.item_normal(index)
        tab.removeCellWidget(row, column)
        tab.setItem(row, column, item)

def supprimer_combobox(tab, previousRow, previousColumn):
    MyWindow.ETAT_SVG = False
    tab.removeCellWidget(previousRow, previousColumn)


class MyWindow(QtWidgets.QMainWindow):
    """
    Cette Classe hérite de la fenetre graphique definit avec Qt Creator et attribut à chaque action sa fonctionnalité
    """

    ETAT_SVG = True
    LISTE_OBJET_POLICE = []
    horaire = [] #Variable de class indiquant la plage horaire de  24h (définit plus bas à modifier)
    etatHor = [] #↑vairble de class indiquant les horaires a afficher
    quantiteCreneau = 1 #nombre de creneau par benevole par jour ; 1creneau = 1H
    artiste_samediV = []
    artiste_samediS = []
    resumeVen = ''
    resumeSam = ''
    syntheseVen = ''
    syntheseSam = ''
    dictResumeVen = {}
    dictResumeSam = {}

    def __init__(self, parent=None):#constructeur
        MyWindow.LISTE_OBJET_POLICE = []
        QtWidgets.QMainWindow.__init__(self, parent)# mauvaise méthode super(MyWindow, self).__init__(parent)

        self.move(100,100) #placement de la fenetre (à vérifier)
        self.ui = fenetre_principale_UI.Ui_MainWindow() #création de l'objet contenant les widgets de la fenetre graphique
        self.ui.setupUi(self) #on place les Widgets dans la fenêtre

########################################### Chargement Titre Fenetre, onglet, statuBar
        self.setWindowTitle("Créneaux - Meuh Folle") #Titre de le fenetre
        self.ui.statusBar.showMessage("Meuh Folle 2017 - Best Meuh Folle ever") #Petit message d'accueil
########################################### Ajout d'icones
        self.setWindowIcon(QtGui.QIcon(IMG_ICON)) #icone fenetre
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(IMG_FLECHE_HAUT)) #icone remonter dans le tableau
        self.ui.scrollAtTopB.setIcon(icon)
        self.ui.scrollAtTopC.setIcon(icon)
        self.ui.scrollAtTopV.setIcon(icon)
        self.ui.scrollAtTopS.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(IMG_FLECHE_BAS)) #icone pour descendre dans le tableau
        self.ui.scrollAtBottomB.setIcon(icon)
        self.ui.scrollAtBottomC.setIcon(icon)
        self.ui.scrollAtBottomV.setIcon(icon)
        self.ui.scrollAtBottomS.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(IMG_CROIX)) #icone pour stoppper la recherche de benevoles dans le tableau
        self.ui.supRechercheV.setIcon(icon)
        self.ui.supRechercheS.setIcon(icon)
        self.ui.supRechercheBene.setIcon(icon)
        self.ui.supRechercheCre.setIcon(icon)


########################################## initialisation TRI benevoles
        self.ui.tabBenevoles.sortByColumn(0,QtCore.Qt.AscendingOrder)
        self.ui.radioTriNom.setChecked(True)
##########################################  Chargement ComboBox
        qte = Svg.Load.charger_variable(OPTION,"quantiteCreneau")
        if qte == False:
            qte=4
        MyWindow.quantiteCreneau = int(Svg.Load.charger_combobox(str(qte),self.ui.quantiteCreneau))
########################################## Chargement et MeP des Tableaux Benevoles et Creneaux et horairesartiste_samedi

        Creneaux.set_list_creneaux() # chargement de la liste de creneaux depuis le fichier de sauvegarde
        Creneaux.tri_creneaux()
        Creneaux.remplir_tab_creneau(self.ui.tabCreneaux) #ecriture de la liste de creneaux dele tableau
        Benevoles.set_list_benevoles() # chargement de la liste de benevoles depuis le fichier de sauvegarde
        Benevoles.remplir_tab_benevoles(self.ui.tabBenevoles,MyWindow.quantiteCreneau) #ecriture de la liste de benevoles dans le tableau benevoles
        self.oldCreneaux = Creneaux.listCreneaux
        self.oldBenevoles = Benevoles.listBenevoles

        self.nb_creneaux() # on indique le nombre de creneaux (en bas du tableau Creneaux)
        self.nb_benevoles() #on indique le nombre de benevoles (en bas du tableau Benevoles)
        self.moyenne_nombre_creneau()
        MyWindow.artiste_samediV, MyWindow.artiste_samediS = Svg.Load.charger_horaire_artistes(OPTION,self.ui.horaireArtistes) # On charge le tableau des artiste_samedi des soirées et on attirbut au variable global cette liste


        self.ui.tabCreneaux.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.ui.tabBenevoles.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
########################################## Chargement et MeP des ListWidget listCatCre, listHoraire
        Creneaux.charger_categorie_creneau(self.ui.listCatCre)
        MyWindow.etatHor = Svg.Load.charger_horaire(OPTION,self.ui.listHoraire)
        if len(MyWindow.etatHor) == 0:
            MyWindow.etatHor = ["0"]*24
##########################################  Chargement  RACCOURCIS
        self.ui.shortcut_entreeV = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Enter),self.ui.creneauVendredi)
        self.ui.shortcut_returnV = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return),self.ui.creneauVendredi)
        self.ui.shortcut_entreeS = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Enter),self.ui.creneauSamedi)
        self.ui.shortcut_returnS = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return),self.ui.creneauSamedi)
#        self.ui.shortcut_echapC = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape),self.ui.tabCreneaux)

########################################## Chargement ListeResume
        MyWindow.dictResumeVen["0"] = self.ui.list0CreneauV
        MyWindow.dictResumeVen["1"] = self.ui.list1CreneauV
        MyWindow.dictResumeVen["2"] = self.ui.list2CreneauV
        MyWindow.dictResumeVen["3"] = self.ui.list3CreneauV
        MyWindow.dictResumeVen["4"] = self.ui.list4CreneauV
        MyWindow.dictResumeVen["5"] = self.ui.list5CreneauV

        MyWindow.dictResumeSam["0"] = self.ui.list0CreneauS
        MyWindow.dictResumeSam["1"] = self.ui.list1CreneauS
        MyWindow.dictResumeSam["2"] = self.ui.list2CreneauS
        MyWindow.dictResumeSam["3"] = self.ui.list3CreneauS
        MyWindow.dictResumeSam["4"] = self.ui.list4CreneauS
        MyWindow.resumeVen = Resume(self.ui.list0CreneauV, self.ui.list1CreneauV, self.ui.list2CreneauV, self.ui.list3CreneauV, self.ui.list4CreneauV, self.ui.list5CreneauV, "V",MyWindow.quantiteCreneau)
        MyWindow.resumeSam = Resume(self.ui.list0CreneauS, self.ui.list1CreneauS, self.ui.list2CreneauS, self.ui.list3CreneauS, self.ui.list4CreneauS, self.ui.list5CreneauS, "S",MyWindow.quantiteCreneau)


        ##################### Respecter les voeux
        self.ui.voeuxArtistes.setCheckState(QtCore.Qt.Checked) #A l'ouverture on respecte toujours les voeux d'artiste_samedi
        self.ui.voeuxCreneaux.setCheckState(QtCore.Qt.Checked) #A l'ouverture on respecte toujours les voeux de creneaux
        ##################### ProgressBar
        self.maj_progress_bar()

        self.home()

    def home(self):
        ############################## MENUBAR ######################################################################
                ############### Affichage #################
        self.ui.actionZoom.triggered.connect(partial(self.action_zoom, 1))
        self.ui.actionDezoomer.triggered.connect(partial(self.action_zoom, -1))
        self.ui.actionResetPolice.triggered.connect(partial(self.action_zoom, 0))
#        self.ui.actionDerniereSvg.triggered.connect(self.charger_derniere_version)
        self.ui.actionQuitter.triggered.connect(self.closeEvent)        # Fichier-->Quitter "ctrl+Q"
        self.ui.actionEnregistrer.triggered.connect(self.save)        # Fichier-->Enregistrer "ctrl+S"
        self.ui.actionCalculAuto.triggered.connect(self.calcul_auto)
        # Import-->Import Creneau, Benevoles et Double (si les deux viennent du même fichier)
        self.ui.actionImport.triggered.connect(self.import_donnees)
        self.ui.actionExport.triggered.connect(self.export)

        self.ui.actionReinitialiser.triggered.connect(self.reset)
        ############### PAR ONGLET ###################################################################################

        ### VENDREDI &&&&& SAMEDI ###############
        self.ui.tabWidget.currentChanged.connect(self.choix_onglet)

        ############### Vendredi ################
        self.ui.ResumeBenevoleV.cellClicked.connect(self.modif_cell_tableau_resume)
        self.ui.creneauVendredi.itemClicked.connect(self.choix_creneau)
        self.ui.rechercheV.activated.connect(self.recherche)
        self.ui.supRechercheV.clicked.connect(self.recherche_stop)
        self.ui.creneauVendredi.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.ResumeBenevoleV.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.ResumeBenevoleV.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ############### Samedi ##################
        self.ui.ResumeBenevoleS.cellClicked.connect(self.modif_cell_tableau_resume)
        self.ui.creneauSamedi.itemClicked.connect(self.choix_creneau)
        self.ui.rechercheS.currentIndexChanged.connect(self.recherche)
        self.ui.supRechercheS.clicked.connect(self.recherche_stop)
        self.ui.creneauSamedi.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.ResumeBenevoleS.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.ResumeBenevoleS.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ############### Benevoles ###############
        self.ui.supBenevole.clicked.connect(self.supprimer_benevole) #suppresion de ligne dans les tableaux par le bouton supprimer un benevole
        self.ui.tabBenevoles.itemChanged.connect(self.modif_cellule_tabBenevoles)
        self.ui.tabBenevoles.cellClicked.connect(self.modif_cellule_tabBenevoles_combobox)
        self.ui.ajoutBenevole2.clicked.connect(self.ajouter_benevole)
        self.ui.tabBenevoles.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ############### Creneaux ################
        self.ui.ajoutCreneau2.clicked.connect(self.ajouter_creneau) #ajout de ligne dans les tableaux par le bouton ajouter un creneau
        self.ui.supCreneau.clicked.connect(self.supprimer_creneau) #suppresion de ligne dans les tableaux par le bouton supprimer un creneau
        self.ui.tabCreneaux.itemChanged.connect(self.modif_cellule_tabCreneaux)
        self.ui.tabCreneaux.cellClicked.connect(self.modif_cellule_tabCreneaux_combobox)
        self.ui.tabCreneaux.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ############### Outils #################

        self.ui.ajoutCategorie.clicked.connect(self.ajout_categorie_creneau)
        self.ui.supCategorie.clicked.connect(self.supprimer_categorie_creneau)
        self.ui.listHoraire.clicked.connect(self.save_hor)
        self.ui.listCatCre.clicked.connect(self.save_categorie)
        self.ui.ajoutCreneau.clicked.connect(self.ajouter_creneau)
        self.ui.ajoutBenevole.clicked.connect(self.ajouter_benevole)
        self.ui.quantiteCreneau.activated.connect(self.quantite_creneau)
        self.ui.horaireArtistes.cellChanged.connect(self.svg_horaires_artiste_samedi)
        self.ui.horaireArtistes.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.horaireArtistes.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)





        ############### ResumeV #################
        mapsignalActif = QtCore.QSignalMapper(self)
        mapsignalActif.mapped.connect(self.select_all_list_resume)

        mapsignalActif.setMapping(self.ui.allVen0,0)
        mapsignalActif.setMapping(self.ui.allVen1,1)
        mapsignalActif.setMapping(self.ui.allVen2,2)
        mapsignalActif.setMapping(self.ui.allVen3,3)
        mapsignalActif.setMapping(self.ui.allVen4,4)
        mapsignalActif.setMapping(self.ui.allVen5,5)

        mapsignalActif.setMapping(self.ui.allSam0,0)
        mapsignalActif.setMapping(self.ui.allSam1,1)
        mapsignalActif.setMapping(self.ui.allSam2,2)
        mapsignalActif.setMapping(self.ui.allSam3,3)
        mapsignalActif.setMapping(self.ui.allSam4,4)
        mapsignalActif.setMapping(self.ui.allSam5,5)

        self.ui.allVen0.clicked.connect(mapsignalActif.map)
        self.ui.allVen1.clicked.connect(mapsignalActif.map)
        self.ui.allVen2.clicked.connect(mapsignalActif.map)
        self.ui.allVen3.clicked.connect(mapsignalActif.map)
        self.ui.allVen4.clicked.connect(mapsignalActif.map)
        self.ui.allVen5.clicked.connect(mapsignalActif.map)

        self.ui.allSam0.clicked.connect(mapsignalActif.map)
        self.ui.allSam1.clicked.connect(mapsignalActif.map)
        self.ui.allSam2.clicked.connect(mapsignalActif.map)
        self.ui.allSam3.clicked.connect(mapsignalActif.map)
        self.ui.allSam4.clicked.connect(mapsignalActif.map)
        self.ui.allSam5.clicked.connect(mapsignalActif.map)

        mapsignalNonActif = QtCore.QSignalMapper(self)
        mapsignalNonActif.mapped.connect(self.unselect_all_list_resume)

        mapsignalNonActif.setMapping(self.ui.noneVen0,0)
        mapsignalNonActif.setMapping(self.ui.noneVen1,1)
        mapsignalNonActif.setMapping(self.ui.noneVen2,2)
        mapsignalNonActif.setMapping(self.ui.noneVen3,3)
        mapsignalNonActif.setMapping(self.ui.noneVen4,4)
        mapsignalNonActif.setMapping(self.ui.noneVen5,5)

        mapsignalNonActif.setMapping(self.ui.noneSam0,0)
        mapsignalNonActif.setMapping(self.ui.noneSam1,1)
        mapsignalNonActif.setMapping(self.ui.noneSam2,2)
        mapsignalNonActif.setMapping(self.ui.noneSam3,3)
        mapsignalNonActif.setMapping(self.ui.noneSam4,4)
        mapsignalNonActif.setMapping(self.ui.noneSam5,5)

        self.ui.noneVen0.clicked.connect(mapsignalNonActif.map)
        self.ui.noneVen1.clicked.connect(mapsignalNonActif.map)
        self.ui.noneVen2.clicked.connect(mapsignalNonActif.map)
        self.ui.noneVen3.clicked.connect(mapsignalNonActif.map)
        self.ui.noneVen4.clicked.connect(mapsignalNonActif.map)
        self.ui.noneVen5.clicked.connect(mapsignalNonActif.map)

        self.ui.noneSam0.clicked.connect(mapsignalNonActif.map)
        self.ui.noneSam1.clicked.connect(mapsignalNonActif.map)
        self.ui.noneSam2.clicked.connect(mapsignalNonActif.map)
        self.ui.noneSam3.clicked.connect(mapsignalNonActif.map)
        self.ui.noneSam4.clicked.connect(mapsignalNonActif.map)
        self.ui.noneSam5.clicked.connect(mapsignalNonActif.map)

        self.ui.list0CreneauV.clicked.connect(self.maj_list_activation)
        self.ui.list1CreneauV.clicked.connect(self.maj_list_activation)
        self.ui.list2CreneauV.clicked.connect(self.maj_list_activation)
        self.ui.list3CreneauV.clicked.connect(self.maj_list_activation)
        self.ui.list4CreneauV.clicked.connect(self.maj_list_activation)
        self.ui.list5CreneauV.clicked.connect(self.maj_list_activation)

        self.ui.list0CreneauS.clicked.connect(self.maj_list_activation)
        self.ui.list1CreneauS.clicked.connect(self.maj_list_activation)
        self.ui.list2CreneauS.clicked.connect(self.maj_list_activation)
        self.ui.list3CreneauS.clicked.connect(self.maj_list_activation)
        self.ui.list4CreneauS.clicked.connect(self.maj_list_activation)
        self.ui.list5CreneauS.clicked.connect(self.maj_list_activation)



        ######################## RACCOURCIS #################################################################
        self.ui.shortcut_entreeV.activated.connect(self.choix_creneau)
        self.ui.shortcut_returnV.activated.connect(self.choix_creneau)
        self.ui.shortcut_entreeS.activated.connect(self.choix_creneau)
        self.ui.shortcut_returnS.activated.connect(self.choix_creneau)
#        self.ui.shortcut_echapC.activated.connect(self.supprimer_combobox)


        self.ui.rechercheBenevoles.textChanged.connect(self.recherche_benevoles)
        self.ui.rechercheCreneaux.textChanged.connect(self.recherche_creneaux)
        self.ui.radioCreFiltreCat.clicked.connect(self.recherche_creneaux)
        self.ui.radioCreFiltreNom.clicked.connect(self.recherche_creneaux)
        self.ui.radioFiltreCat.clicked.connect(self.recherche_benevoles)
        self.ui.radioFiltreNom.clicked.connect(self.recherche_benevoles)
##########################################################################################################################################################
#                                                           FIN HOME()
##########################################################################################################################################################
#   DEBUT METHODE REACTION AU WIDGET (Chacune de ces méthodes est appelé par Home() elle même appelé par les Widgets de la Fenetre)
##########################################################################################################################################################




    def calcul_auto(self):
        MyWindow.ETAT_SVG = False
        if M.question_calcul_auto() == QtWidgets.QMessageBox.Yes:
            Creneaux.svg_list_creneaux(self.ui.listCatCre)
            self.ui.tabBenevoles.blockSignals(True) #on bloque le signal de modification de la cellule de Benevoles, la valeur  va être changee
            self.ui.tabCreneaux.blockSignals(True)  #on bloque le signal de modification de la cellule de Creneaux, la valeur va être changee
            voeuxA = self.ui.voeuxArtistes.checkState() # on recupere les valeurs de respect des demandes des benevoles
            voeuxC = self.ui.voeuxCreneaux.checkState()
            jour_calcul_auto = Jour(self.ui.creneauVendredi, "V", MyWindow.etatHor, MyWindow.quantiteCreneau,
                            MyWindow.artiste_samediV, voeuxC, voeuxA, self.ui.rechercheV,
                            self.ui.tabBenevoles,self.ui.tabCreneaux)
            jour_calcul_auto.remplissage_auto()
            Creneaux.maj_creneaux(self.ui.tabCreneaux)
            Benevoles.maj_benevoles(self.ui.tabBenevoles,MyWindow.quantiteCreneau)
            MyWindow.resumeVen.maj_resume(MyWindow.quantiteCreneau)
            MyWindow.resumeSam.maj_resume(MyWindow.quantiteCreneau)
            self.ui.tabBenevoles.blockSignals(False)
            self.ui.tabCreneaux.blockSignals(False)
            self.maj_progress_bar()
            self.choix_onglet()


    def modif_cell_tableau_resume(self):
        MyWindow.ETAT_SVG = False
        tab_resume = [self.ui.ResumeBenevoleV, self.ui.ResumeBenevoleS]
        onglet = self.ui.tabWidget.currentIndex()
        tab = tab_resume[onglet]
        column = tab.currentColumn()
        row = tab.currentRow()
        if tab.currentItem():
            select = tab.currentItem().text()
        else:
            select = " "
        if (column == 0 or column == 1 or column == 2) and row == 0:
            if tab.item(row, column):
                item = M.item_combobox(Creneaux.catCreneaux,select)
                tab.setCellWidget(row,column,item)
                loop = QtCore.QEventLoop()
                item.currentTextChanged[str].connect(self.set_valeur_combobox_resume)
                item.currentTextChanged[str].connect(loop.exit)
                tab.currentCellChanged[int, int, int, int].connect(self.supprimer_combobox_resume)
                tab.currentCellChanged[int, int, int, int].connect(loop.exit)
                loop.exec_()

        elif column == 3 and row == 0:
            if tab.item(row, column):
                art = []
                liste_artiste = [MyWindow.artiste_samediV,MyWindow.artiste_samediS, self.ui.ResumeBenevoleS]
                onglet = self.ui.tabWidget.currentIndex()
                artistes = liste_artiste[onglet]
                for i in range(1,len(MyWindow.artiste_samediV),2):
                    art.append(artistes[i])
                item = M.item_combobox(art,select)
                tab.setCellWidget(row,column,item)

                loop = QtCore.QEventLoop()
                item.currentTextChanged[str].connect(self.set_valeur_combobox_resume)
                item.currentTextChanged[str].connect(loop.exit)
                tab.currentCellChanged[int, int, int, int].connect(self.supprimer_combobox_resume)
                tab.currentCellChanged[int, int, int, int].connect(loop.exit)
                loop.exec_()
    

    def action_zoom(self, n):
        print(n)
        if n == 0:
            taille_police = DEFAULT_POLICE_SIZE
        else:
            taille_police = self.ui.creneauVendredi.fontInfo().pointSize()
        self.ui.creneauVendredi.setFont(QtGui.QFont("Calibri", taille_police + n))
        self.ui.creneauSamedi.setFont(QtGui.QFont("Calibri", taille_police + n))
        self.ui.tabBenevoles.setFont(QtGui.QFont("Calibri", taille_police + n))
        self.ui.listCatCre.setFont(QtGui.QFont("Calibri", taille_police + n))
        self.ui.listHoraire.setFont(QtGui.QFont("Calibri", taille_police + n))
        self.ui.tabCreneaux.setFont(QtGui.QFont("Calibri", taille_police + n))
        for val in MyWindow.dictResumeVen.values():
            val.setFont(QtGui.QFont("Calibri", taille_police + n))
        for val in MyWindow.dictResumeSam.values():
            val.setFont(QtGui.QFont("Calibri", taille_police + n))
        self.ui.creneauVendredi.resizeRowsToContents()
        self.ui.creneauSamedi.resizeRowsToContents()
        self.ui.tabBenevoles.resizeRowsToContents()
        self.ui.tabCreneaux.resizeRowsToContents()

    def select_all_list_resume(self,intList):
        MyWindow.ETAT_SVG = False
        if self.ui.tabWidget.currentIndex() == 5 :
            liste = MyWindow.dictResumeVen[str(intList)]
            nbBene = liste.count()
            for i in range(nbBene):
                if liste.item(i).checkState() == QtCore.Qt.Unchecked :
                    liste.item(i).setCheckState(QtCore.Qt.Checked)
                    for k in range(Benevoles.nombreBenevoles):
                        if Benevoles.listBenevoles[k].nom == liste.item(i).text():
                            Benevoles.listBenevoles[k].actif_vendredi = True

        elif self.ui.tabWidget.currentIndex() == 6 :

            liste = MyWindow.dictResumeSam[str(intList)]
            nbBene = liste.count()
            for i in range(nbBene):
                if liste.item(i).checkState() == QtCore.Qt.Unchecked :
                    liste.item(i).setCheckState(QtCore.Qt.Checked)
                    for k in range(Benevoles.nombreBenevoles):
                        if Benevoles.listBenevoles[k].nom == liste.item(i).text():
                            Benevoles.listBenevoles[k].actif_samedi = True
    def unselect_all_list_resume(self,intList):
        MyWindow.ETAT_SVG = False
        if self.ui.tabWidget.currentIndex() == 5 :
            liste = MyWindow.dictResumeVen[str(intList)]
            nbBene = liste.count()
            for i in range(nbBene):
                if liste.item(i).checkState() == QtCore.Qt.Checked :
                    liste.item(i).setCheckState(QtCore.Qt.Unchecked)
                    for k in range(Benevoles.nombreBenevoles):
                        if Benevoles.listBenevoles[k].nom == liste.item(i).text():
                            Benevoles.listBenevoles[k].actif_vendredi = False
        elif self.ui.tabWidget.currentIndex() == 6 :
            liste = MyWindow.dictResumeSam[str(intList)]
            nbBene = liste.count()
            for i in range(nbBene):
                if liste.item(i).checkState() == QtCore.Qt.Checked :
                    liste.item(i).setCheckState(QtCore.Qt.Unchecked)
                    for k in range(Benevoles.nombreBenevoles):
                        if Benevoles.listBenevoles[k].nom == liste.item(i).text():
                            Benevoles.listBenevoles[k].actif_samedi = False

    def svg_horaires_artiste_samedi(self):
        """
        Des qu'une case du tableau artites de l'onglet Outil est mofifié, cette fonction est exécutée
        Permet d'enregistrer le tableau d'artiste
        """
        self.ui.horaireArtistes.blockSignals(True)  # la fonction de modifie la cellule, car ajoute le texte centrée et avec majuscules
        MyWindow.artiste_samediV, MyWindow.artiste_samediS = Svg.Save.svg_horaires_artistes(self.ui.horaireArtistes) # sauvegarde des artistes_samedi
        self.ui.horaireArtistes.blockSignals(False)



    def choix_creneau(self):
        MyWindow.ETAT_SVG = False
        """
        Dans les tableau de chaque jour, dès qu'une case est cliquée ou validée par appuie sur la touche Entree ou Retour, cette fonction est executee
        La fonction ouvre la fenetre de choix du benevole est ajoute la valeur choisit par l'utilisateur
        """
        self.ui.tabBenevoles.blockSignals(True) #on bloque le signal de modification de la cellule de Benevoles, la valeur  va être changee
        self.ui.tabCreneaux.blockSignals(True)  #on bloque le signal de modification de la cellule de Creneaux, la valeur va être changee
        jour = self.ui.tabWidget.currentIndex() #on recherche la valeur 0 == Vendredi ou 1 == Samedi

        if jour == 0 and self.ui.creneauVendredi.currentItem() != None : #Vendredi, on ne s'occupe pas des cases non remplie (aucun creneau)
            self.ui.rechercheV.setCurrentIndex(0)
            listeBenevoles = Vendredi.definir_liste_benevoles(self.ui.creneauVendredi.currentRow(), self.ui.creneauVendredi.currentColumn()) #on définit la liste de benevoles disponibles pour le creneaux choisit
            if listeBenevoles and listeBenevoles[0] != False:
                if self.ui.radioTriVMax.isChecked(): #cas ou on veut faire apparaitre les benevoles ayant le plus de creneaux en premier
                    for i in range(len(listeBenevoles)):
                        val = listeBenevoles[i].split(" ; \n Nb : ")[1]
                        z=i
                        for j in range(i,len(listeBenevoles)):
                            val2 = listeBenevoles[j].split(" ; \n Nb : ")[1]
                            if val2 > val :
                                val = val2
                                z = j
                        listeBenevoles[i],listeBenevoles[z] = listeBenevoles[z],listeBenevoles[i]
                elif self.ui.radioTriVMin.isChecked(): #cas ou on veut faire apparaitre les benevoles ayant le moins de creneaux en premier
                    for i in range(len(listeBenevoles)):
                        val = listeBenevoles[i].split(" ; \n Nb : ")[1]
                        z=i
                        for j in range(i,len(listeBenevoles)):
                            val2 = listeBenevoles[j].split(" ; \n Nb : ")[1]
                            if val2 < val :
                                val = val2
                                z = j
                        listeBenevoles[i],listeBenevoles[z] = listeBenevoles[z],listeBenevoles[i]
                ComboBox = ChoixBenevole(listeBenevoles) #on ouvre la fenetre de choix
                if ComboBox.choix == False: #Si le resultat est False c'est que l'utilisateur à voulu supprimer le creneaux
                    Vendredi.vider_cell() #on appelle la fonction de Vendredi (Jour) qui supprime le benevole
                elif ComboBox.choix != "" :  # Si le resultat est "" l'utilisateur a annule, sinon c'est le nom du benevole choisi
                    Vendredi.benevoleChoisi = ComboBox.choix  #on enregistre la valeur
                    Vendredi.setNomBenevole(self.ui.creneauVendredi.currentRow(), self.ui.creneauVendredi.currentColumn()) #on ajoute le nom du benevole à la liste
            elif len(listeBenevoles) == 0:
                print(listeBenevoles,"a")
                M.aucun_benevole()
            else:
                M.creneau_2e_heure()
            try:
                self.ui.creneauVendredi.currentItem().text().split('\n')[1]
                for benevole in Benevoles.listBenevoles:
                    if benevole.nom == self.ui.creneauVendredi.currentItem().text().split('\n')[1]:
                        remplir_tab_resume(self.ui.ResumeBenevoleV,self.ui.NbCBeneV,benevole,"V")
            except:
                self.ui.ResumeBenevoleV.clear()
                self.ui.ResumeBenevoleV.setSpan(1,0,1,4)
                self.ui.NbCBeneV.setText("Aucun bénévole sélectionné")


            MyWindow.resumeVen.maj_resume(MyWindow.quantiteCreneau)
        elif jour == 1 and self.ui.creneauSamedi.currentItem() != None: # Meme fonction que Vendredi appliquee au samedi
            self.ui.rechercheS.setCurrentIndex(0)
            listeBenevoles = Samedi.definir_liste_benevoles(self.ui.creneauSamedi.currentRow(), self.ui.creneauSamedi.currentColumn())
            if listeBenevoles and listeBenevoles[0] != False:
                if self.ui.radioTriSMax.isChecked(): # cas ou on veut faire apparaitre les benevoles ayant le plus de creneaux en premier
                    for i in range(len(listeBenevoles)):
                        val = listeBenevoles[i].split(" ; \n Nb : ")[1]
                        z=i
                        for j in range(i,len(listeBenevoles)):
                            val2 = listeBenevoles[j].split(" ; \n Nb : ")[1]
                            if val2 > val :
                                val = val2
                                z = j
                        listeBenevoles[i],listeBenevoles[z] = listeBenevoles[z],listeBenevoles[i]
                elif self.ui.radioTriSMin.isChecked(): # cas ou on veut faire apparaitre les benevoles ayant le moins de creneaux en premier
                    for i in range(len(listeBenevoles)):
                        val = listeBenevoles[i].split(" ; \n Nb : ")[1]
                        z=i
                        for j in range(i,len(listeBenevoles)):
                            val2 = listeBenevoles[j].split(" ; \n Nb : ")[1]
                            if val2 < val :
                                val = val2
                                z = j
                        listeBenevoles[i],listeBenevoles[z] = listeBenevoles[z],listeBenevoles[i]
                ComboBox = ChoixBenevole(listeBenevoles)
                if ComboBox.choix == False:
                    Samedi.vider_cell()
                elif ComboBox.choix != "" :
                    Samedi.benevoleChoisi = ComboBox.choix
                    Samedi.setNomBenevole(self.ui.creneauSamedi.currentRow(), self.ui.creneauSamedi.currentColumn())
            elif len(listeBenevoles) == 0:
                print(listeBenevoles,"a")
                M.aucun_benevole()
            else:
                M.creneau_2e_heure()
            try:
                self.ui.creneauSamedi.currentItem().text().split('\n')[1]
                for benevole in Benevoles.listBenevoles:
                    if benevole.nom == self.ui.creneauSamedi.currentItem().text().split('\n')[1]:
                        remplir_tab_resume(self.ui.ResumeBenevoleS,self.ui.NbCBeneS,benevole,"S")
            except:
                self.ui.ResumeBenevoleS.clear()
                self.ui.ResumeBenevoleS.setSpan(1,0,1,4)
                self.ui.NbCBeneS.setText("Aucun bénévole sélectionné")

            MyWindow.resumeSam.maj_resume(MyWindow.quantiteCreneau)
        Creneaux.maj_creneaux(self.ui.tabCreneaux)
        Benevoles.maj_benevoles(self.ui.tabBenevoles, MyWindow.quantiteCreneau)
        self.maj_progress_bar() #mise à jour des bar de progression (onglet Outils)

        self.ui.tabBenevoles.blockSignals(False)
        self.ui.tabCreneaux.blockSignals(False)

    def choix_onglet(self):
        """
        Lorsque l'utilisateur change d'onglet, cette fonctio nest executee,
        Si l'onglet choisit est le vendredi ou le samedi, on construit le tableau permettant d'ajouter des creneaux
        Sinon on remet juste à zéros la fonction de recherche pour qu'elle soit à nouveau fonctionnelle la fois suivante
        """
        self.ui.tabBenevoles.blockSignals(True)
        self.ui.tabCreneaux.blockSignals(True)
        self.ui.tabBenevoles.sortByColumn(0,QtCore.Qt.AscendingOrder)
        global Vendredi, Samedi #variable globale, réutiliser dans choix_creneaux
        onglet = self.ui.tabWidget.currentIndex() #permet de reperer l'onglet ouvert
        voeuxA = self.ui.voeuxArtistes.checkState() # on recupere les valeurs de respect des demandes des benevoles
        voeuxC = self.ui.voeuxCreneaux.checkState()
        if onglet == 0: #Vendredi
            #permet de s'assurer que lorsqu'on quitte un onglet la fonction recherche est réinitialisee
            self.recherche_stop()
            Vendredi = Jour(self.ui.creneauVendredi, "V", MyWindow.etatHor, MyWindow.quantiteCreneau, MyWindow.artiste_samediV, voeuxC, voeuxA, self.ui.rechercheV,self.ui.tabBenevoles,self.ui.tabCreneaux)
        elif onglet == 1: #Samedi
            #permet de s'assurer que lorsqu'on quitte un onglet la fonction recherche est réinitialisee
            self.recherche_stop()
            Samedi =   Jour(self.ui.creneauSamedi,   "S", MyWindow.etatHor, MyWindow.quantiteCreneau, MyWindow.artiste_samediS, voeuxC, voeuxA, self.ui.rechercheS,self.ui.tabBenevoles,self.ui.tabCreneaux)
        if onglet == 2 : #Benevoles
            if self.ui.radioTriVMax.isChecked() :
                self.ui.tabBenevoles.sortByColumn(9,QtCore.Qt.DescendingOrder)
            if self.ui.radioTriVMin.isChecked() :
                self.ui.tabBenevoles.sortByColumn(9,QtCore.Qt.AscendingOrder)
            if self.ui.radioTriSMax.isChecked() :
                self.ui.tabBenevoles.sortByColumn(10,QtCore.Qt.DescendingOrder)
            if self.ui.radioTriSMin.isChecked() :
                self.ui.tabBenevoles.sortByColumn(10,QtCore.Qt.AscendingOrder)
            if self.ui.radioTriNom.isChecked() : #pas utile
                self.ui.tabBenevoles.sortByColumn(0,QtCore.Qt.AscendingOrder)
        self.ui.tabBenevoles.blockSignals(False)
        self.ui.tabCreneaux.blockSignals(False)


    def recherche(self):
        """
        Lorsque l'utilisateur utilise une des deux barres de recherche du Vendredi ou Samedi, cette fonction est executee
        La fonction permet de colorer un benevole en particulier pour el retrouver plus facilement
        """
        jour = self.ui.tabWidget.currentIndex() #Permet de reperer l'onglet ouvert
        if jour == 0 : #Onglet Vendredi
            filtrePrec = Svg.Load.charger_variable(OPTION,"filtreV") # le filtre precedent est enregistré dans le fichier de sauvegarde
            filtre = self.ui.rechercheV.currentText() # le nouveau filtre est celui choisi par l'utilisateur
            Svg.Save.sauvegarder_var(filtre,"filtreV") # on enregistre le nouveau choix de filtre
            if filtrePrec != filtre : #si le filtre a change

                for creneau in Creneaux.listCreneaux :#pour chaque creneaux

                    if creneau.benevole_vendredi == filtre : #si le benevole attribué au creneau est le filtre
                        loc = creneau.loc #on le repère dans le tableau Vendredi
                        item = M.item_recherche(self.ui.creneauVendredi.item(loc[0],loc[1]).text()) #on colorie le creneaux concerné
                        self.ui.creneauVendredi.setItem(loc[0],loc[1],item)

                    if creneau.benevole_vendredi == filtrePrec : #si le benevoles est l'ancienne recherche
                        loc = creneau.loc #on le repere dans le tableau Vendredi
                        item = M.item_rempli(self.ui.creneauVendredi.item(loc[0],loc[1]).text()) # on le remet dans le format classique
                        self.ui.creneauVendredi.setItem(loc[0],loc[1],item)
                for benevole in Benevoles.listBenevoles:
                    if benevole.nom == filtre:
                        remplir_tab_resume(self.ui.ResumeBenevoleV,self.ui.NbCBeneV,benevole,"V")
                        break

        if jour == 1 : #Meme but qu'au dessus pour l'onglet Samedi
            filtrePrec = Svg.Load.charger_variable(OPTION,"filtreS")
            filtre = self.ui.rechercheS.currentText()
            Svg.Save.sauvegarder_var(filtre,"filtreS")
            if filtrePrec != filtre :

                for creneau in Creneaux.listCreneaux :
                    if creneau.benevole_samedi == filtre :
                        loc = creneau.loc
                        item = M.item_recherche(self.ui.creneauSamedi.item(loc[0],loc[1]).text())
                        self.ui.creneauSamedi.setItem(loc[0],loc[1],item)
                    if creneau.benevole_samedi == filtrePrec :
                        loc = creneau.loc
                        item = M.item_rempli(self.ui.creneauSamedi.item(loc[0],loc[1]).text()) # on le remet dans le format classique
                        self.ui.creneauSamedi.setItem(loc[0],loc[1],item)
                for benevole in Benevoles.listBenevoles:
                    if benevole.nom == filtre:
                        remplir_tab_resume(self.ui.ResumeBenevoleS,self.ui.NbCBeneS,benevole,"S")
                        break

    def recherche_benevoles(self):
        li = self.ui.tabBenevoles.rowCount()
        search = self.ui.rechercheBenevoles.text().title()
        if self.ui.radioFiltreNom.isChecked():
            for i in range(li):
                self.ui.tabBenevoles.setRowHidden(i, False)
                nom = self.ui.tabBenevoles.item(i,0).text()
                if search not in nom:
                    self.ui.tabBenevoles.setRowHidden(i, True)
        elif self.ui.radioFiltreCat.isChecked():
            for i in range(li):
                self.ui.tabBenevoles.setRowHidden(i, False)
                cat = self.ui.tabBenevoles.item(i,1).text().title()
                cat += self.ui.tabBenevoles.item(i,2).text().title()
                cat += self.ui.tabBenevoles.item(i,3).text().title()
                if search not in cat:
                    self.ui.tabBenevoles.setRowHidden(i, True)
        else:
            for i in range(li):
                self.ui.tabBenevoles.setRowHidden(i, False)
                artiste = self.ui.tabBenevoles.item(i,4).text().title()
                artiste += self.ui.tabBenevoles.item(i,5).text().title()
                if search not in artiste:
                    self.ui.tabBenevoles.setRowHidden(i, True)

    def recherche_creneaux(self):
        li = self.ui.tabCreneaux.rowCount()
        search = self.ui.rechercheCreneaux.text().title()
        if self.ui.radioCreFiltreNom.isChecked():
            for i in range(li):
                self.ui.tabCreneaux.setRowHidden(i, False)
                nom = self.ui.tabCreneaux.item(i,0).text()
                if search not in nom:
                    self.ui.tabCreneaux.setRowHidden(i, True)
        else:
            for i in range(li):
                self.ui.tabCreneaux.setRowHidden(i, False)
                cat = self.ui.tabCreneaux.item(i,3).text()
                if search not in cat:
                    self.ui.tabCreneaux.setRowHidden(i, True)

    def recherche_stop(self):
        """
        Lorsque l'utilisateur clique sur la croix ou qe l'onglet est change, cette fonction est executee,
        permet de réinitialiser la fonction recherche à "Aucun" (Permier terme de la liste)
        """
        self.ui.rechercheV.setCurrentIndex(0) #on change la valeur de la liste à aucun pour Vendredi
        self.ui.rechercheS.setCurrentIndex(0) #idem Samedi
        self.ui.ResumeBenevoleV.clearContents()
        self.ui.ResumeBenevoleS.clearContents()
        self.ui.ResumeBenevoleV.setSpan(1,0,1,4)
        self.ui.ResumeBenevoleS.setSpan(1,0,1,4)
        self.ui.NbCBeneV.setText("Aucun bénévole sélectionné")
        self.ui.NbCBeneS.setText("Aucun bénévole sélectionné")
        self.recherche() # on execute la fonction recherche, utile pour lorque la croix est enclenché pour colorer remettre à zeros les cases

    def modif_cellule_tabCreneaux_combobox(self):
        MyWindow.ETAT_SVG = False
        column = self.ui.tabCreneaux.currentColumn()
        row = self.ui.tabCreneaux.currentRow()
        if self.ui.tabCreneaux.currentItem():
            select = self.ui.tabCreneaux.currentItem().text()
        else:
            select = " "
        if column == 1 :
            item = M.item_combobox(HORAIRE,select)
            self.ui.tabCreneaux.setCellWidget(row,column,item)
            loop = QtCore.QEventLoop()
            item.currentTextChanged[str].connect(self.set_valeur_combobox_tabCreneaux)
            item.currentTextChanged[str].connect(loop.exit)
            self.ui.tabCreneaux.currentCellChanged[int, int, int, int].connect(self.supprimer_combobox_tabCreneaux)
            self.ui.tabCreneaux.currentCellChanged[int, int, int, int].connect(loop.exit)
            loop.exec_()

        elif column == 2 :
            item = M.item_combobox(['1H','2H'],select)
            self.ui.tabCreneaux.setCellWidget(row,column,item)
            loop = QtCore.QEventLoop()
            item.currentTextChanged[str].connect(self.set_valeur_combobox_tabCreneaux)
            item.currentTextChanged[str].connect(loop.exit)
            self.ui.tabCreneaux.currentCellChanged[int, int, int, int].connect(self.supprimer_combobox_tabCreneaux)
            self.ui.tabCreneaux.currentCellChanged[int, int, int, int].connect(loop.exit)
            loop.exec_()

        if column == 3 :

            item = M.item_combobox(Creneaux.catCreneaux,select)
            self.ui.tabCreneaux.setCellWidget(row,column,item)
            loop = QtCore.QEventLoop()
            item.currentTextChanged[str].connect(self.set_valeur_combobox_tabCreneaux)
            item.currentTextChanged[str].connect(loop.exit)
            self.ui.tabCreneaux.currentCellChanged[int, int, int, int].connect(self.supprimer_combobox_tabCreneaux)
            self.ui.tabCreneaux.currentCellChanged[int, int, int, int].connect(loop.exit)
            loop.exec_()
            
    def set_valeur_combobox_resume(self, index):
        self.ui.tabBenevoles.blockSignals(True)
        tab_resume = [self.ui.ResumeBenevoleV, self.ui.ResumeBenevoleS]
        onglet = self.ui.tabWidget.currentIndex()
        tab = tab_resume[onglet]
        column = tab.currentColumn()
        set_valeur_combobox(index, tab)
        cle = Benevoles.attribut[column + 1]
        if onglet == 1 and column == 3:
            cle = Benevoles.attribut[column + 2]
        label_resume = [self.ui.NbCBeneV,self.ui.NbCBeneS]
        label_resume = label_resume[onglet]
        nom_benevole = label_resume.text().split(" : ")[0]
        for benevole in Benevoles.listBenevoles:
            if benevole.nom == nom_benevole:
                #permet d'appeler l'attribut modifie, celui ci est reférencé dans un objet dict pour chaque creneau
                benevole.__dict__[cle] = index
                Benevoles.remplir_tab_benevoles(self.ui.tabBenevoles,MyWindow.quantiteCreneau)
                break
        self.ui.tabBenevoles.blockSignals(False)

    def set_valeur_combobox_tabCreneaux(self, index):
        set_valeur_combobox(index, self.ui.tabCreneaux)

    def set_valeur_combobox_tabBenevoles(self, index):
        set_valeur_combobox(index, self.ui.tabBenevoles)
        
    def modif_cellule_tabCreneaux(self):
        """
        Lorsque l'utilisateur modifie directement une cellule du tableau Creneaux, cette fonction est executee
        Permet d'ajouter la nouvelle valeur au tableau et de changerla valeur du benevole dans le fichier sauvegarde
        """
        MyWindow.ETAT_SVG = False
        row = self.ui.tabCreneaux.currentRow()
        column = self.ui.tabCreneaux.currentColumn()
        cle = Creneaux.attribut[column]
        Creneaux.listCreneaux[row].__dict__[cle] = self.ui.tabCreneaux.item(row,column).text() #permet d'appeler l'attribut modifie, celui ci est reférencé dans un objet dict pour chaque creneau

    def modif_cellule_tabBenevoles_combobox(self):
        MyWindow.ETAT_SVG = False
        column = self.ui.tabBenevoles.currentColumn()
        row = self.ui.tabBenevoles.currentRow()
        if self.ui.tabBenevoles.currentItem():
            select = self.ui.tabBenevoles.currentItem().text()
        else:
            select = " "
        if column == 1 or column == 2 or column == 3 :
            item = M.item_combobox(Creneaux.catCreneaux,select)
            self.ui.tabBenevoles.setCellWidget(row,column,item)

            loop = QtCore.QEventLoop()
            item.currentTextChanged[str].connect(self.set_valeur_combobox_tabBenevoles)
            item.currentTextChanged[str].connect(loop.exit)
            self.ui.tabBenevoles.currentCellChanged[int, int, int, int].connect(self.supprimer_combobox_tabBenevoles)
            self.ui.tabBenevoles.currentCellChanged[int, int, int, int].connect(loop.exit)
            loop.exec_()
        elif column == 4 :
            art = []
            for i in range(1,len(MyWindow.artiste_samediV),2):
                art.append(MyWindow.artiste_samediV[i])
            item = M.item_combobox(art,select)
            self.ui.tabBenevoles.setCellWidget(row,column,item)

            loop = QtCore.QEventLoop()
            item.currentTextChanged[str].connect(self.set_valeur_combobox_tabBenevoles)
            item.currentTextChanged[str].connect(loop.exit)
            self.ui.tabBenevoles.currentCellChanged[int, int, int, int].connect(self.supprimer_combobox_tabBenevoles)
            self.ui.tabBenevoles.currentCellChanged[int, int, int, int].connect(loop.exit)
            loop.exec_()

        if column == 5 :
            art = []
            for i in range(1,len(MyWindow.artiste_samediS),2):
                art.append(MyWindow.artiste_samediS[i])
            item = M.item_combobox(art,select)
            self.ui.tabBenevoles.setCellWidget(row,column,item)
            loop = QtCore.QEventLoop()
            item.currentTextChanged[str].connect(self.set_valeur_combobox_tabBenevoles)
            item.currentTextChanged[str].connect(loop.exit)
            self.ui.tabBenevoles.currentCellChanged[int, int, int, int].connect(self.supprimer_combobox_tabBenevoles)
            self.ui.tabBenevoles.currentCellChanged[int, int, int, int].connect(loop.exit)
            loop.exec_()

    def supprimer_combobox_tabBenevoles(self,row, column, previousRow, previousColumn):
        supprimer_combobox(self.ui.tabBenevoles, previousRow, previousColumn)
        
    def supprimer_combobox_tabCreneaux(self,row, column, previousRow, previousColumn):
        supprimer_combobox(self.ui.tabCreneaux, previousRow, previousColumn)

    def supprimer_combobox_resume(self,row, column, previousRow, previousColumn):
        tab_resume = [self.ui.ResumeBenevoleV, self.ui.ResumeBenevoleS]
        onglet = self.ui.tabWidget.currentIndex()
        tab = tab_resume[onglet]
        supprimer_combobox(tab, previousRow, previousColumn)        

    def modif_cellule_tabBenevoles(self):
        """
        Lorsque l'utilisateur modifie directement un cellule du tableau Creneaux, cette fonction est executee
        Permet d'ajouter la nouvelle valeur au tableau et de changerla valeur du benevole dans le fichier sauvegarde
        """
        MyWindow.ETAT_SVG = False
        row = self.ui.tabBenevoles.currentRow()
        column = self.ui.tabBenevoles.currentColumn()
        cle = Benevoles.attribut[column]
        Benevoles.listBenevoles[row].__dict__[cle]  = self.ui.tabBenevoles.item(row,column).text() #permet d'appeler l'attribut modifie, celui ci est reférencé dans un objet dict pour chaque benevole

    def quantite_creneau(self):
        """
        Lorsque l'utilisateur change la valeur de la ComboBox "Nombre de creneaux par benevoles", cette fontion est executee
        O met simplement à jour la valeur de cette variable
        """
        MyWindow.ETAT_SVG = False
        if os.path.isfile(OPTION):
            self.ui.tabBenevoles.blockSignals(True)
            MyWindow.quantiteCreneau = int(Svg.Save.sauvegarder_var(self.ui.quantiteCreneau.currentText(),"quantiteCreneau"))
            Benevoles.maj_benevoles(self.ui.tabBenevoles,MyWindow.quantiteCreneau)
            MyWindow.resumeVen = Resume(self.ui.list0CreneauV, self.ui.list1CreneauV, self.ui.list2CreneauV, self.ui.list3CreneauV, self.ui.list4CreneauV, self.ui.list5CreneauV, "V",MyWindow.quantiteCreneau)
            MyWindow.resumeSam = Resume(self.ui.list0CreneauS, self.ui.list1CreneauS, self.ui.list2CreneauS, self.ui.list3CreneauS, self.ui.list4CreneauS, self.ui.list5CreneauS, "S",MyWindow.quantiteCreneau)
            self.ui.tabBenevoles.blockSignals(False)
        else:
            M.aucune_donnees()

    def ajout_categorie_creneau(self):
        MyWindow.ETAT_SVG = False
        if self.ui.categorieSup.text()!="":
            if not(self.ui.categorieSup.text().title() in Creneaux.catCreneaux):
                nvCat = str(self.ui.categorieSup.text()).title()
                item = QtWidgets.QListWidgetItem(nvCat, self.ui.listCatCre)
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
            self.ui.categorieSup.clear()
        Creneaux.maj_categorie_creneau(self.ui.listCatCre)

    def supprimer_categorie_creneau(self):
        MyWindow.ETAT_SVG = False
        for selection in self.ui.listCatCre.selectedItems():
            self.ui.listCatCre.takeItem(self.ui.listCatCre.row(selection))
        Creneaux.maj_categorie_creneau(self.ui.listCatCre)



    def import_donnees(self):
        """Méthode pour importer des Créneaux, lorsqu'on clique sur fichier --> Import Double"""
        MyWindow.ETAT_SVG = False
        self.ui.tabCreneaux.blockSignals(True)
        self.ui.tabBenevoles.blockSignals(True)
#        fenetre d'ouverture d'un fichier
        fileName = QtWidgets.QFileDialog.getOpenFileName(self,"Ouvrir l'excel des Bénévoles&Créneaux",QtCore.QDir.homePath(),"Fichiers Excel (*.xls;*.xlsx;*.xlsm;*.cvs)")
        if fileName[0] != '' :
            fi = open(OPTION,"w")
            fi.close()
            #enregistrement des valeurs de l'excel une liste pour le tableau
            Creneaux.import_creneaux_excel(fileName[0]) #Import de l'excel
            #ecriture des données dans le tableau, la tableau est aussi redimensionné à la taille des données
            Creneaux.remplir_tab_creneau(self.ui.tabCreneaux)
            #enregistrement des valeurs de l'excel dans une liste pour le tableau
            Benevoles.import_benevoles_excel(fileName[0],self.ui.horaireArtistes)
            #ecriture des données dans le tableau, la tableau est aussi redimensionné à la taille des données
            Benevoles.remplir_tab_benevoles(self.ui.tabBenevoles,MyWindow.quantiteCreneau)

        self.ui.tabCreneaux.blockSignals(False)
        self.ui.tabBenevoles.blockSignals(False)
        self.save()
        Creneaux.charger_categorie_creneau(self.ui.listCatCre)
        self.maj_progress_bar()


    def export(self):
        MyWindow.ETAT_SVG = False
        fileName = QtWidgets.QFileDialog.getOpenFileName(self,"Ouvrir l'excel des Bénévoles&Créneaux",QtCore.QDir.homePath(),"Fichiers Excel (*.xls;*.xlsx;*.xlsm;*.cvs)")
        if fileName[0] != '':
            a = time.time()
            Benevoles.export_benevoles_excel(fileName[0])
            Creneaux.export_creneaux_excel(fileName[0])
            print(time.time()-a)
            M.action_realisee("L'export s'est terminé avec succès")
            self.save()

    def nb_benevoles(self):
        nb = len(Benevoles.listBenevoles)
        self.ui.nbBenevoles.setText("Nombre de benevoles : {}".format(nb))
        return nb

    def nb_creneaux(self):
        self.ui.nbCreneaux.setText("Nombre de creneaux : {}".format(self.ui.tabCreneaux.rowCount()))
        return self.ui.tabCreneaux.rowCount()

    def moyenne_nombre_creneau(self):
        cpt = 0
        for creneau in Creneaux.listCreneaux:
            if creneau.duree == '1H':
                cpt += 1
            else:
                cpt += 2
        if Benevoles.nombreBenevoles > 0:
            self.ui.moyenne.setText("Moyenne espérée : {}".format(round(cpt/Benevoles.nombreBenevoles,2)))
        else:
            self.ui.moyenne.setText("Aucun Bénévole")

    def ajouter_creneau(self):
        MyWindow.ETAT_SVG = False
        if os.path.isfile(OPTION):
            self.ui.tabCreneaux.blockSignals(True)
            newCreneau = AjoutCreneau()
            if newCreneau.nom :
                Creneaux(newCreneau.nom.text().title(),newCreneau.plageHor,newCreneau.duree,newCreneau.categorie)
                self.ui.tabCreneaux.setRowCount(self.ui.tabCreneaux.rowCount()+1) #on ajoute une ligne au tableau creneaux
                nbCre = self.nb_creneaux() #on change le nombre de benevoles

                item = M.item_normal(newCreneau.nom.text())#on ajoute chacun des attributs
                self.ui.tabCreneaux.setItem(nbCre-1,0,item)
                item = M.item_normal(newCreneau.plageHor)
                self.ui.tabCreneaux.setItem(nbCre-1,1,item)
                item = M.item_normal(newCreneau.duree)
                self.ui.tabCreneaux.setItem(nbCre-1,2,item)
                item = M.item_normal(newCreneau.categorie)
                self.ui.tabCreneaux.setItem(nbCre-1,3,item)
                item = M.item_normal(newCreneau.benevoles_vendredi)
                self.ui.tabCreneaux.setItem(nbCre-1,4,item)
                item = M.item_normal(newCreneau.benevoles_samedi)
                self.ui.tabCreneaux.setItem(nbCre-1,5,item)

            Creneaux.tri_creneaux()
            Creneaux.remplir_tab_creneau(self.ui.tabCreneaux)
            self.ui.tabCreneaux.blockSignals(False)
        else:
            M.aucune_donnees()



    def ajouter_benevole(self):
        MyWindow.ETAT_SVG = False
        if os.path.isfile(OPTION):
            self.ui.tabBenevoles.blockSignals(True)
            newBenevole = AjoutBenevole()  #creation du nouveau benevoles
            if  newBenevole.nom: #si le benevole à un nom alors il a tout les attributs necessaires qui suivent
                Benevoles(newBenevole.nom, newBenevole.cre1, newBenevole.cre2, newBenevole.cre3, newBenevole.artiste_vendredi, newBenevole.artiste_samedi,newBenevole.remarques)

                self.ui.tabBenevoles.setRowCount(self.ui.tabBenevoles.rowCount()+1) #on ajoute une ligne au tableau benevoles
                nbBene = self.nb_benevoles() #on change le nombre de benevoles

                item = M.item_normal(newBenevole.nom)#on ajoute chacun des attributs
                self.ui.tabBenevoles.setItem(nbBene-1,0,item)
                item = M.item_normal(newBenevole.cre1)
                self.ui.tabBenevoles.setItem(nbBene-1,1,item)
                item = M.item_normal(newBenevole.cre2)
                self.ui.tabBenevoles.setItem(nbBene-1,2,item)
                item = M.item_normal(newBenevole.cre3)
                self.ui.tabBenevoles.setItem(nbBene-1,3,item)
                item = M.item_normal(newBenevole.artiste_vendredi)
                self.ui.tabBenevoles.setItem(nbBene-1,4,item)
                item = M.item_normal(newBenevole.artiste_samedi)
                self.ui.tabBenevoles.setItem(nbBene-1,5,item)
                item = M.item_normal(newBenevole.remarques)
                self.ui.tabBenevoles.setItem(nbBene-1,6,item)

                Benevoles.maj_benevoles(self.ui.tabBenevoles,MyWindow.quantiteCreneau)
            for i in range (Benevoles.nombreBenevoles):
                val = Benevoles.listBenevoles[i].nom
                z=i
                for j in range(i,Benevoles.nombreBenevoles):
                    val2 = Benevoles.listBenevoles[j].nom
                    if val2 < val :
                        val = val2
                        z = j
                Benevoles.listBenevoles[i],Benevoles.listBenevoles[z] = Benevoles.listBenevoles[z],Benevoles.listBenevoles[i]
                self.ui.tabBenevoles.sortByColumn(0,QtCore.Qt.AscendingOrder)
            self.ui.tabBenevoles.blockSignals(False)
        else:
            M.aucune_donnees()

    def supprimer_creneau(self):
        MyWindow.ETAT_SVG = False
        row = self.ui.tabCreneaux.currentRow()
        if self.ui.tabCreneaux.item(row,4).text() or self.ui.tabCreneaux.item(row,5).text():
            M.sup_impossible("creneau","benevole(s)")
        else:
            if M.confirmer_suppression("creneau") == QtWidgets.QMessageBox.Ok:
                Creneaux.listCreneaux.pop(row)
                self.ui.tabCreneaux.removeRow(self.ui.tabCreneaux.currentRow())
            Creneaux.nombreCreneaux = self.nb_creneaux()

    def supprimer_benevole(self):
        MyWindow.ETAT_SVG = False
        row = self.ui.tabBenevoles.currentRow()
        if self.ui.tabBenevoles.item(row,7).text() or self.ui.tabBenevoles.item(row,8).text():
            M.sup_impossible("benevole","creneau(x)")
        else:
            if M.confirmer_suppression("benevole") == QtWidgets.QMessageBox.Ok:
                benevole = self.ui.tabBenevoles.item(row,0).text()
                for i in range(Benevoles.nombreBenevoles):
                    if Benevoles.listBenevoles[i].nom == benevole :
                        Benevoles.listBenevoles.pop(i)
                        Benevoles.nombreBenevoles = self.nb_benevoles()
                        break
                self.ui.tabBenevoles.removeRow(self.ui.tabBenevoles.currentRow())

    def maj_list_activation(self):
        liste = self.sender()
        li = liste.currentRow()
        for i in range(Benevoles.nombreBenevoles):
            if liste.item(li).text() == Benevoles.listBenevoles[i].nom:
                pos = i
                break
        if liste.item(li).checkState() == QtCore.Qt.Unchecked:
            liste.item(li).setCheckState(QtCore.Qt.Checked)
            if self.ui.tabWidget.currentIndex() == 5:
                Benevoles.listBenevoles[pos].actif_vendredi = True
            elif self.ui.tabWidget.currentIndex() == 6:
                Benevoles.listBenevoles[pos].actif_samedi = True
        elif liste.item(li).checkState() == QtCore.Qt.Checked:
            liste.item(li).setCheckState(QtCore.Qt.Unchecked)
            if self.ui.tabWidget.currentIndex() == 5 :
                Benevoles.listBenevoles[pos].actif_vendredi = False
            elif self.ui.tabWidget.currentIndex() == 6:
                Benevoles.listBenevoles[pos].actif_samedi = False

    def save_hor(self):
        li = self.ui.listHoraire.currentRow()
        if self.ui.listHoraire.item(li).checkState() == QtCore.Qt.Unchecked:
            self.ui.listHoraire.item(li).setCheckState(QtCore.Qt.Checked)
        elif self.ui.listHoraire.item(li).checkState() == QtCore.Qt.Checked:
            self.ui.listHoraire.item(li).setCheckState(QtCore.Qt.Unchecked)
        nbVal = self.ui.listHoraire.count() #nb valeur dans la liste
        MyWindow.etatHor = []
        for i in range(nbVal):
            MyWindow.etatHor.append(str(self.ui.listHoraire.item(i).checkState())) #si checkable enregistrement des etat 0 Unchecked , 2 Checked

    def save_categorie(self):
        li = self.ui.listCatCre.currentRow()
        if self.ui.listCatCre.item(li).checkState() == QtCore.Qt.Unchecked:
            self.ui.listCatCre.item(li).setCheckState(QtCore.Qt.Checked)
        elif self.ui.listCatCre.item(li).checkState() == QtCore.Qt.Checked:
            self.ui.listCatCre.item(li).setCheckState(QtCore.Qt.Unchecked)
        Creneaux.maj_categorie_creneau(self.ui.listCatCre)

    def save(self):
        a = time.time()
        if os.path.isfile(OPTION):
            MyWindow.ETAT_SVG = True
            MyWindow.resumeVen.maj_resume(MyWindow.quantiteCreneau)
            MyWindow.resumeSam.maj_resume(MyWindow.quantiteCreneau)
            Creneaux.maj_creneaux(self.ui.tabCreneaux)
            Benevoles.maj_benevoles(self.ui.tabBenevoles, MyWindow.quantiteCreneau)
            self.moyenne_nombre_creneau()
            self.svg_horaires_artiste_samedi()
            Svg.Save.sauvegarder_horaire(self.ui.listHoraire)
            Creneaux.svg_list_creneaux(self.ui.listCatCre)
            Benevoles.svg_tab_benevoles()
        self.maj_progress_bar()
        print(time.time()-a)

    def reset(self):
        MyWindow.ETAT_SVG = False
        a = time.time()
        self.ui.tabBenevoles.blockSignals(True)
        self.ui.tabCreneaux.blockSignals(True)
        for creneau in Creneaux.listCreneaux:
            creneau.benevole_samedi = ""
            creneau.benevole_vendredi = ""
        for benevole in Benevoles.listBenevoles:
            benevole.creneaux_vendredi = []
            benevole.creneaux_samedi = []
        self.maj_progress_bar()
        MyWindow.resumeVen.maj_resume(MyWindow.quantiteCreneau)
        MyWindow.resumeSam.maj_resume(MyWindow.quantiteCreneau)
        Creneaux.maj_creneaux(self.ui.tabCreneaux)
        Benevoles.maj_benevoles(self.ui.tabBenevoles,MyWindow.quantiteCreneau)
        self.choix_onglet()

        self.ui.tabBenevoles.blockSignals(False)
        self.ui.tabCreneaux.blockSignals(False)
        print(time.time()-a," reset")

    def maj_progress_bar(self):
        """        Cette fonction calcul les trois avancements simultanement, Le Vendredi, Le Samedi et le Total"""
        cptV = 0
        cptS =0
        nbCre = len(Creneaux.listCreneaux)
        if nbCre > 0:
            for i in Creneaux.listCreneaux:
                if i.benevole_vendredi != "" : #un benevole = une case de faite
                    cptV +=1
                if i.benevole_samedi != "" : #un benevole = une case de faite
                    cptS +=1

                self.ui.progressBarV.setValue(cptV/nbCre*100)
                self.ui.progressBarS.setValue(cptS/nbCre*100)
                self.ui.progressBarT.setValue((cptV+cptS)/(nbCre*2)*100)
                self.ui.progressBarV.setFormat("Créneaux du vendredi complétés : {} % ({}/{})"
                                               .format(self.ui.progressBarV.value(),cptV,nbCre))
                self.ui.progressBarS.setFormat("Créneaux du samedi complétés : {} % ({}/{})"
                                               .format(self.ui.progressBarS.value(),cptS,nbCre))
                self.ui.progressBarT.setFormat("Créneaux complétés : {} % ({}/{})"
                                               .format(self.ui.progressBarT.value(),cptV+cptS,2*nbCre))

        else:
            self.ui.progressBarV.setFormat("Aucun Créneau")
            self.ui.progressBarS.setFormat("Aucun Créneau")
            self.ui.progressBarT.setFormat("Aucun Créneau")

    def closeEvent(self,evnt):
        if not MyWindow.ETAT_SVG:
            choix = M.question_enregistrer()
            if choix == QtWidgets.QMessageBox.Yes:
                self.save()
        self.close()

class AjoutBenevole(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AjoutBenevole, self).__init__(parent)
        self.Dialog = QtWidgets.QDialog()
        self.di = ajout_benevole_DI.Ui_Ajout_Benevoles()
        self.di.setupUi(self.Dialog)
        self.setWindowTitle("Ajouter un benevole")
        self.nom=''
        self.cre1 = ''
        self.cre2 = ''
        self.cre3 = ''
        self.artiste_vendredi = ''
        self.artiste_samedi = ''
        catCreneau = Creneaux.catCreneaux
        for i in range(len(catCreneau)):
            self.di.cre1.addItem(catCreneau[i].title())
            self.di.cre2.addItem(catCreneau[i].title())
            self.di.cre3.addItem(catCreneau[i].title())
        self.di.cre1.setCurrentIndex(0)
        self.di.cre2.setCurrentIndex(1)
        self.di.cre3.setCurrentIndex(2)
        fi = Qst(OPTION, Qst.IniFormat)
        if fi.contains("List/artistesVendredi"):
            artistesVendredi = fi.value("List/artistesVendredi")
            for i in range(0,len(artistesVendredi),2):
                self.di.artisteV.addItem(artistesVendredi[i].title())
        self.di.artisteV.addItem("Aucun")
        if fi.contains("List/artistesSamedi"):
            artistesSamedi = fi.value("List/artistesSamedi")
            for i in range(0,len(artistesSamedi),2):
                self.di.artisteS.addItem(artistesSamedi[i].title())
        self.di.artisteS.addItem("Aucun")
        self.home()
        self.Dialog.exec_()

    def home(self):
        self.di.ok.clicked.connect(self.ajouter)
        self.di.annuler.clicked.connect(self.annuler)

    def ajouter(self):
        if self.di.nom.text() != "" :
            self.nom = self.di.nom.text().title()
            self.cre1 = self.di.cre1.currentText()
            self.cre2 = self.di.cre2.currentText()
            self.cre3 = self.di.cre3.currentText()
            self.artiste_vendredi = self.di.artisteV.currentText()
            self.artiste_samedi = self.di.artisteS.currentText()
            if self.di.remarques :
                self.remarques = self.di.remarques.text().title()
            self.remarques = self.di.remarques.text()
            self.Dialog.close()

    def annuler(self):
        self.Dialog.close()

class AjoutCreneau(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(AjoutCreneau, self).__init__(parent)
        self.Dialog = QtWidgets.QDialog()
        self.di = ajout_creneau_DI.Ui_Dialog()
        self.di.setupUi(self.Dialog)
        self.setWindowTitle("Ajouter un creneau")
        self.nom =""
        self.plageHor = ""
        self.duree= ""
        self.categorie = ""
        self.benevoles_vendredi = ""
        self.benevoles_samedi= ""

        for horaire in HORAIRE:
            self.di.plageHor.addItem(horaire)

        self.di.duree.addItem('1H')
        self.di.duree.addItem('2H')

        catCreneau = Creneaux.catCreneaux
        if catCreneau:
            for i in range(len(catCreneau)):
                self.di.categorie.addItem(catCreneau[i].title())
                self.di.categorie.setEditable(False)
        else:
            self.di.categorie.setEditable(True)

        self.home()
        self.Dialog.exec_()

    def home(self):
        self.di.annuler.clicked.connect(self.annuler)
        self.di.ok.clicked.connect(self.ajouter)

    def annuler(self):
        self.Dialog.close()

    def ajouter(self):
        if self.di.nom.text() != "" :
            self.nom = self.di.nom
            self.plageHor = self.di.plageHor.currentText()
            self.duree = self.di.duree.currentText()
            self.categorie = self.di.categorie.currentText().title()
            self.Dialog.close()


class ChoixBenevole(QtWidgets.QDialog):
    """
    Class gerant la fenetre de de choix d'attribution d'un benevole à un creaneau
    Cette fenetre renverra :
        Le nom du benevole si un choix a été fait
        False si le benevole doit être supprimer
        "" si l'utilisateur annule
    """
    def __init__(self,listeBenevoles, parent=None): #constructeur
        super(ChoixBenevole, self).__init__(parent)
        self.Dialog = QtWidgets.QDialog()
        self.di = choix_benevole_DI.Ui_Dialog()
        self.di.setupUi(self.Dialog)

        for i in range(len(listeBenevoles)):
            self.di.listBenevoles.addItem(listeBenevoles[i]) #on ajoute tout les benevoles ayant été ajouté à bénévoles disponible

        self.choix = ""  #par défaut le choix du benevoles est  vide
        self.di.shortcut_sup = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Delete),self.Dialog) #raccourci touche suppr
        self.di.shortcut_return = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return),self.Dialog) #raccourci touche retour
        self.di.shortcut_entree = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Enter),self.Dialog)  #raccourci touche entree
        self.di.listBenevoles.setCurrentRow(0)
        self.home() #signaux
        self.Dialog.exec_()

    def home(self):
        self.di.annuler.clicked.connect(self.annuler) #choix annuler
        self.di.supprimer.clicked.connect(self.supprimer) #choix supprimer
        self.di.listBenevoles.itemClicked.connect(self.choix_bene) #choix ajouter
        self.di.shortcut_sup.activated.connect(self.supprimer) #raccourci touche supp pour supprimer un benevole
        self.di.shortcut_return.activated.connect(self.choix_bene)  #raccourci touche retour pour choisir un benevole
        self.di.shortcut_entree.activated.connect(self.choix_bene) #raccourci touche entree pour choisir un benevole

    def choix_bene(self): #fonction choix d'un bénévoles
        """
        Retourne le choix de l'utilisateur dans la fenetre proposant les bénvoles disponibles
        """

        self.choix = self.di.listBenevoles.currentItem().text().split(" ; ")[0] #l'item de choix (on supprime le nombre de creneaux rappelé sous le nom du benevoles)
        self.Dialog.close()

    def annuler(self):
        """
        Si l'utilsaeur choisit d'annuler ; implicitement la touche echap estun raccouri et renvoi le nom du choix vide( == False)
        """
        self.Dialog.close()

    def supprimer(self):
        """
        si l'utilisateur choisit de supprimer un benevole
        """
        self.choix = False
        self.Dialog.close()

if __name__ == '__main__': #différencie le lancement de l'import

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    img_splash = QtGui.QPixmap(IMG_LANCEMENT)
    splash = QtWidgets.QSplashScreen(img_splash,QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(img_splash.mask())
    splash.show()

    splash.finish(window)
    window.showMaximized()
    window.show()
    sys.exit(app.exec_())
    os.system("pause")