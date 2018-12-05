# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:02:55 2017

@author: GANJO
"""


### Format de clé :
    ##  Qtable : Tableau/nom_entete
    ##  Qtable : Tableau/nom_tableau
    ##  Qlist : List/nom
    ##  Qlist : List/nom_state
    ## Variable simple : Variables/nom


import os

import MessBox as M
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSettings as Qst


PATH = os.getcwd()
OPTION = os.path.join(PATH,"doc","__init.ini")
HORAIRE = ["09H-10H", "10H-11H", "11H-12H", "12H-13H", "13H-14H", "14H-15H", "15H-16H", "16H-17H",
           "17H-18H", "18H-19H", "19H-20H", "20H-21H", "21H-22H", "22H-23H", "23H-00H", "00H-01H", "01H-02H", "02H-03H",
           "03H-04H", "04H-05H", "05H-06H", "06H-07H", "07H-08H", "08H-09H"]



class Save(): #classe pour définir les fonction de sauvegarde

    def sauvegarder_data(fileName,data,nomCle): #sauvegarder une donnees de maniere generale
        if os.path.isfile(OPTION):
            fichier = Qst(fileName, Qst.IniFormat) #fichier d'enregistrement
            fichier.setValue(str(nomCle),data)   #ajout de la valeur

    def sauvegarder_horaire(listwid): #sauvegarder une liste de choix, la liste enquestion, le nom de la liste
        nbVal = listwid.count() #nb valeur dans la liste
        state = []
        for i in range(nbVal):
            state.append(str(listwid.item(i).checkState())) #si checkable enregistrement des etat 0 Unchecked , 2 Checked
        Save.sauvegarder_data(OPTION,state,"List/Horaire_state") #sauvegarde comme n'importe qu'elle données

    def sauvegarder_categorie_creneau(listwid): #sauvegarder une liste de choix, la liste enquestion, le nom de la liste
        nbVal = listwid.count() #nb valeur dans la liste
        val = []
        state = []
        if nbVal > 0:
            for i in range(nbVal):
                val.append(listwid.item(i).text().title()) #enregistrement des valeurs
                state.append(str(listwid.item(i).checkState())) #si checkable enregistrement des etat 0 Unchecked , 2 Checked
            Save.sauvegarder_data(OPTION,state,"List/categorie_Creneau_state") #sauvegarde comme n'importe qu'elle données
            Save.sauvegarder_data(OPTION,val,"List/categorie_Creneau")
        return val, state


    def svg_horaires_artistes(tableau):
        try:
            item = M.item_tab_hor_artistes(tableau.currentItem().text())
            i = tableau.currentRow()
            j = tableau.currentColumn()
            tableau.setItem(i,j,item)
        except:
            None
            artV = []
            artS = []
            for i in range(4):
                try:
                    artV.append(tableau.item(i,0).text().title())
                    artV.append(tableau.item(i,0).text().title())
                    artS.append(tableau.item(i,1).text().title())
                    artS.append(tableau.item(i,1).text().title())
                except:
                    None
            Save.sauvegarder_data(OPTION,artV,"List/artistesVendredi")
            Save.sauvegarder_data(OPTION,artS,"List/artistesSamedi")
            tableau.resizeColumnsToContents()
            return artV,artS

    def sauvegarder_var(variable,nomvariable):  #sauvegarder un variable simple, valeur unique
        cle="Variables/"+str(nomvariable)
        Save.sauvegarder_data(OPTION,variable,cle)
        return variable

class Load(): #Classe Load pour tout ce qui est chargement de donnees

    def charger_horaire(fileName, listwid):   ##fonction pour charger les donnees d'une Qlist
        cleState = "List/Horaire_state"
        fi = Qst(fileName,Qst.IniFormat)
        dejaPresent = []
        if fi.contains(cleState):
            for i in range(listwid.count()):
                dejaPresent.append(listwid.item(i).text().title())
            state = fi.value(cleState)
            for i in range(len(HORAIRE)):
                if not(HORAIRE[i] in dejaPresent) :
                    item = QtWidgets.QListWidgetItem(HORAIRE[i].title(), listwid)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    if int(state[i]) == 2:
                        item.setCheckState(QtCore.Qt.Checked)
                    if int(state[i]) == 0:
                        item.setCheckState(QtCore.Qt.Unchecked)

            return state
        else:
            state = ["0"]*24
            for horaire in HORAIRE:
                if not(horaire in dejaPresent) :
                    item = QtWidgets.QListWidgetItem(horaire.title(), listwid)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item.setCheckState(QtCore.Qt.Unchecked)
            return state
    def charger_variable(fileName,typevariable):  # chargement d'une variable classique
        cle = "Variables/"+str(typevariable)
        fi = Qst(fileName,Qst.IniFormat)
        variable = False
        if fi.contains(cle):
            variable = fi.value(cle)
        return variable  #retourne la variable = False si inexistante

    def charger_combobox(val, combo):  #permet de charger la valeur d'un comboBox lors de l'ouverture, appelle forcément la fct charger_variable
        if val:
            index = combo.findText(val,QtCore.Qt.MatchFixedString)
            if index > 0:
                combo.setCurrentIndex(index)
            return val
        return False

    def charger_horaire_artistes(fileName, tableau):
        cleV = "List/artistesVendredi"
        cleS = "List/artistesSamedi"
        artV, artS = ['','','','','','','',''],  ['','','','','','','','']
        fi = Qst(fileName, Qst.IniFormat)
        if fi.contains(cleV):
            artV = fi.value(cleV)
            for i in range(0,len(artV),2):
                item = M.item_tab_hor_artistes(artV[i])
                tableau.setItem(i//2,0,item)
        if fi.contains(cleS):
            artS = fi.value(cleS)
            for i in range(0,len(artS),2):
                item = M.item_tab_hor_artistes(artS[i])
                tableau.setItem(i//2,1,item)
        tableau.resizeColumnsToContents()
        return artV, artS
