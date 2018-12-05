# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 21:46:40 2017

@author: GANJO
"""
import os
from PyQt5 import QtWidgets , QtGui, QtCore

from benevoles import Benevoles

PATH = os.getcwd()
OPTION = os.path.join(PATH,"doc","__init.ini")

class Resume():


    def __init__(self,list0,list1,list2,list3,list4,list5,jour,qCre):


        self.list0 = list0
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
        self.list4 = list4
        self.list5 = list5

        self.jour = jour


        self.list0.clear()
        self.list1.clear()
        self.list2.clear()
        self.list3.clear()
        self.list4.clear()
        self.list5.clear()




        if self.jour == "V":

            for i in range(Benevoles.nombreBenevoles):
                nbCre = len(Benevoles.listBenevoles[i].creneaux_vendredi)
                if nbCre > 5 :
                    nbCre = 5
                nom = Benevoles.listBenevoles[i].nom
                actif = Benevoles.listBenevoles[i].actif_vendredi
                item = QtWidgets.QListWidgetItem(nom, self.__dict__["list"+str(nbCre)])
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                if len(Benevoles.listBenevoles[i].creneaux_vendredi) >= qCre :
                    item.setCheckState(QtCore.Qt.Unchecked)
                elif actif :
                    item.setCheckState(QtCore.Qt.Checked)
                else :
                    item.setCheckState(QtCore.Qt.Unchecked)

        if self.jour == "S":

            for i in range(Benevoles.nombreBenevoles):
                nbCre = len(Benevoles.listBenevoles[i].creneaux_samedi)
                if nbCre > 5 :
                    nbCre = 5
                nom = Benevoles.listBenevoles[i].nom
                actif = Benevoles.listBenevoles[i].actif_samedi
                item = QtWidgets.QListWidgetItem(nom, self.__dict__["list"+str(nbCre)])
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                if len(Benevoles.listBenevoles[i].creneaux_samedi) >= qCre :
                    item.setCheckState(QtCore.Qt.Unchecked)
                elif actif :
                    item.setCheckState(QtCore.Qt.Checked)
                else :
                    item.setCheckState(QtCore.Qt.Unchecked)




    def maj_resume(self, qCre):

        self.list0.clear()
        self.list1.clear()
        self.list2.clear()
        self.list3.clear()
        self.list4.clear()
        self.list5.clear()




        if self.jour == "V":

            for benevole in Benevoles.listBenevoles:
                nbCre = len(benevole.creneaux_vendredi)
                if nbCre > 5 :
                    nbCre = 5
                nom = benevole.nom
                actif = benevole.actif_vendredi
                item = QtWidgets.QListWidgetItem(nom, self.__dict__["list"+str(nbCre)])
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                if len(benevole.creneaux_vendredi) >= qCre :
                    item.setCheckState(QtCore.Qt.Unchecked)
                elif actif :
                    item.setCheckState(QtCore.Qt.Checked)

                else :
                    item.setCheckState(QtCore.Qt.Unchecked)

        if self.jour == "S":

            for benevole in Benevoles.listBenevoles:
                nbCre = len(benevole.creneaux_samedi)
                if nbCre > 5 :
                    nbCre = 5
                nom = benevole.nom
                actif = benevole.actif_samedi
                item = QtWidgets.QListWidgetItem(nom, self.__dict__["list"+str(nbCre)])
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                if len(benevole.creneaux_samedi) >= qCre :
                    item.setCheckState(QtCore.Qt.Unchecked)
                elif actif :
                    item.setCheckState(QtCore.Qt.Checked)
                else :
                    item.setCheckState(QtCore.Qt.Unchecked)









