# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 18:44:31 2017

@author: GANJO
"""


import os
from PyQt5 import QtWidgets , QtGui, QtCore

from benevoles import Benevoles
from creneaux import Creneaux

PATH = os.getcwd()
OPTION = os.path.join(PATH,"doc","__init.ini")
HORAIRE = ["09H-10H", "10H-11H", "11H-12H", "12H-13H", "13H-14H", "14H-15H", "15H-16H", "16H-17H",
           "17H-18H", "18H-19H", "19H-20H", "20H-21H", "21H-22H", "22H-23H", "23H-00H", "00H-01H", "01H-02H", "02H-03H",
           "03H-04H", "04H-05H", "05H-06H", "06H-07H", "07H-08H", "08H-09H"]
HORAIRE_ART = ['19H-20H', '20H-21H', "21H-22H", "22H-23H", "23H-00H", "00H-01H", "01H-02H", "02H-03H"]


class Synthese():

    def __init__(self, synV, synS, creneaux, benevoles, catCre, artV, artS, etatHor):

        self.syntheseV = synV
        self.syntheseS = synS
        self.benevoles = benevoles
        self.creneaux = creneaux
        self.categorie_creneaux = catCre
        self.artistes_vendredi = artV
        self.artistes_samedi = artS
        self.horaire_affichee = etatHor
        self.nb_categorie_cre = len(self.categorie_creneaux)
        self.syntheseV.setRowCount(2*self.nb_categorie_cre+1)
        self.syntheseS.setRowCount(2*self.nb_categorie_cre+1)
        nom_ligne = self.categorie_creneaux + ["Benevoles"] + self.categorie_creneaux
        self.syntheseV.setVerticalHeaderLabels(nom_ligne)
        self.syntheseS.setVerticalHeaderLabels(nom_ligne)
        for j in range(24):
            self.syntheseV.setColumnHidden(j, False)
            self.syntheseS.setColumnHidden(j, False)
            if self.horaire_affichee[j]=="0":
                self.syntheseV.setColumnHidden(j, True)
                self.syntheseS.setColumnHidden(j, True)



        for creneau in self.creneaux:
            j = HORAIRE.index(creneau.plage_horaire)
            i = self.categorie_creneaux.index(creneau.categorie)
            if not self.syntheseV.item(i, j):
                item = QtWidgets.QTableWidgetItem("1")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setBackground(QtGui.QColor(200, 200, 200))
                self.syntheseV.setItem(i, j, item)
            else:
                nb = int(self.syntheseV.item(i, j).text())
                nb = str(nb+1)
                item = QtWidgets.QTableWidgetItem(nb)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setBackground(QtGui.QColor(200, 200, 200))
                self.syntheseV.setItem(i, j, item)
            if creneau.duree == "2H":
                if not self.syntheseV.item(i, j+1):
                    item = QtWidgets.QTableWidgetItem("1")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setBackground(QtGui.QColor(200, 200, 200))
                    self.syntheseV.setItem(i, j+1, item)
                else:
                    nb = int(self.syntheseV.item(i, j+1).text())
                    nb = str(nb+1)
                    item = QtWidgets.QTableWidgetItem(nb)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setBackground(QtGui.QColor(200, 200, 200))
                    self.syntheseV.setItem(i, j+1, item)
        print(self.categorie_creneaux)
        for benevole in benevoles:
            lignes = []
            artV = benevole.artiste_vendredi
            indisponible = []
            if artV in self.artistes_vendredi:
                index_art = self.artistes_vendredi.index(artV)
                indisponible = [HORAIRE.index(HORAIRE_ART[index_art]), HORAIRE.index(HORAIRE_ART[index_art+1])]
                print(indisponible)
            lignes.append(self.categorie_creneaux.index(benevole.cre1))
            if self.categorie_creneaux.index(benevole.cre2) not in lignes:
                lignes.append(self.categorie_creneaux.index(benevole.cre2))
            if self.categorie_creneaux.index(benevole.cre3) not in lignes:
                lignes.append(self.categorie_creneaux.index(benevole.cre3))
            for j in range(24):
                if j not in indisponible:
                    i =lignes[0]+self.nb_categorie_cre + 1
                    if not self.syntheseV.item(i, j):
                        item = QtWidgets.QTableWidgetItem("1")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setBackground(QtGui.QColor(150, 150, 150))
                        self.syntheseV.setItem(i, j, item)
                    else:
                        nb = int(self.syntheseV.item(i, j).text())
                        nb = str(nb+1)
                        item = QtWidgets.QTableWidgetItem(nb)
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setBackground(QtGui.QColor(150, 150, 150))
                        self.syntheseV.setItem(i, j, item)














