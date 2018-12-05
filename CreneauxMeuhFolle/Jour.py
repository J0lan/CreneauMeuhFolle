# -*- coding: utf-8 -*-
#pylint: disable=E1101
"""
Created on Tue Jun 13 23:26:36 2017

@author: GANJO
"""

from random import randrange

from PyQt5 import QtCore#, QtWidgets, QtGui
from creneaux import Creneaux

from benevoles import Benevoles
import MessBox as M

HORAIRE = ["09H-10H", "10H-11H", "11H-12H", "12H-13H", "13H-14H", "14H-15H", "15H-16H", "16H-17H",
           "17H-18H", "18H-19H", "19H-20H", "20H-21H", "21H-22H", "22H-23H", "23H-00H", "00H-01H", "01H-02H", "02H-03H",
           "03H-04H", "04H-05H", "05H-06H", "06H-07H", "07H-08H", "08H-09H"]
HOR_ARTISTES =  ['19H-20H', '20H-21H', "21H-22H", "22H-23H", "23H-00H", "00H-01H", "01H-02H", "02H-03H"]
CHECK = QtCore.Qt.Checked
UNCHECK = QtCore.Qt.Unchecked


def nom_proposition(nom,cre):
    return nom + " ; \n Nb : " + str(len(cre))


def creneau_benevole_occupe(tableau, col, liste_creneau_par_hor, duree):
    benevoles_occupes = []
    for i in range(liste_creneau_par_hor[col]):
        try:
            benevoles_occupes.append(tableau.item(i, col).text().split("\n")[1])
        except:
            None
    if duree == "2H":
        for i in range(liste_creneau_par_hor[col+1]):
            try:
                benevoles_occupes.append(tableau.item(i, col+1).text().split("\n")[1])
            except:
                None
    elif duree == '1H' and col%2 == 1:
        for i in range(liste_creneau_par_hor[col-1]):
            if tableau.columnSpan(i,col-1) == 2:
                try:
                    benevoles_occupes.append(tableau.item(i, col-1).text().split("\n")[1])
                except:
                    None
    return benevoles_occupes

def creneau_consecutif(indice_horaire, creneaux_benevole, duree):
    indice_complet = []
    for creneau in creneaux_benevole:
        creneau = creneau.split(" : ")
        indice_complet.append(HORAIRE.index(creneau[0]))
    if duree == "1H":
        if indice_horaire-1 in indice_complet and indice_horaire-2 in indice_complet:
            return False
        elif indice_horaire+1 in indice_complet and indice_horaire+2 in indice_complet:
            return False
        elif indice_horaire-1 in indice_complet and indice_horaire+1 in indice_complet:
            return False
        return True
    elif duree == "2H":
        if indice_horaire-1 in indice_complet:
            return False
        elif indice_horaire+2 in indice_complet:
            return False
        return True

def creneau_depassement(quantite_creneau, creneaux_benevole, duree):
    nb_creneau = len(creneaux_benevole)
    if duree == '1H':
        if nb_creneau < quantite_creneau:
            return True
        return False
    elif duree == '2H':
        if nb_creneau < quantite_creneau-1:
            return True
        return False

def creneau_categorie(voeux, categorie, benevole):
    voeux_cat = [benevole.cre1, benevole.cre2, benevole.cre3]
    if voeux == UNCHECK:
        return True
    elif voeux == CHECK:
        if categorie in voeux_cat:
            return True
        return False

def creneau_artistes(voeux, artistes, horaire, benevole_artiste):
    if voeux == UNCHECK:
        return True
    elif voeux == CHECK:
        if horaire in HOR_ARTISTES:
            if benevole_artiste != artistes[HOR_ARTISTES.index(horaire)]:
                return True
            else:
                return False

        return True

def mef_nom_creneau(cat, nom, plage_hor):
    nom_creneau = str(plage_hor) + " : " + str(cat) + " : " + str(nom)
    return nom_creneau



class Jour():
    """Cette Class représente est l'objet tableau qui permet
    d'attribuer des benevoles aux creneaux
    """
    def __init__(self, jour, j, etatHor, qCre, artistes, voeuxC,
                 voeuxA, filtre, tabBenevoles, tabCreneaux):
        self.jour = jour #QtableWidget de l'onglet ouvert
        self.j = j #indice pour Vendredi : "V" ou Samedi : "S"
        self.etatHoraire = etatHor #coché ou non
        self.qCre = qCre #nombre de creneaux par soir
        self.horaireCochee = [] # plage horaire cochés
        self.listNbCreparHor = [] #combien de créneaux par colonne
        self.benevoleChoisi = '' #Attribuer bénévole à la case en cours
        self.artistes = artistes
        self.etatCatCre = Creneaux.etatCatCre
        self.catCre = Creneaux.catCreneaux
        self.catCoches = []
        self.voeuxC = voeuxC
        self.voeuxA = voeuxA
        self.filtre = filtre
        self.tabBenevoles = tabBenevoles
        self.tabCreneaux = tabCreneaux


        #création des horaires à afficher
        self.jour.clearContents()
        self.jour.clearSpans()
        for i in range(24):
            #création de la liste des valeurs des horaires cochés
            if self.etatHoraire[i] == '2':
                self.horaireCochee.append(HORAIRE[i])
                self.jour.setColumnHidden(i, False)
            else:
                self.horaireCochee.append(False)
                self.jour.setColumnHidden(i, True)
        for i in range(len(self.catCre)):
            #création de la liste des valeurs des creneaux cochés
            if self.etatCatCre[i] == '2':
                self.catCoches.append(self.catCre[i])
            else:
                self.catCoches.append(False)
        #nombre de ligne maximum
        maxNbCreparHor = 0
        for creneau in Creneaux.listCreneaux:
            creneau.loc = ['', '']
        #on construit le nombre de ligne du tableau
        for j in range(24):
            nbCreparHor = 0
            for creneau in Creneaux.listCreneaux:
                #important de faire attention à la mise en forme des donnees !!
                if creneau.plage_horaire == self.horaireCochee[j]:
                    if creneau.categorie in self.catCoches:
                        if j%2 == 0:
                        #on donne au créneaux une localisation dans le tableau, pour le retrouver
                            creneau.loc = [nbCreparHor, j]
                            nbCreparHor += 1

                        elif creneau.duree == '1H':
                            for cre in Creneaux.listCreneaux:
                                if cre.loc == [nbCreparHor, j-1]:
                                    if cre.duree == '2H':
                                        nbCreparHor +=1

                            creneau.loc = [nbCreparHor, j]
                            nbCreparHor += 1
            #nombre de créneaux par colonne
            self.listNbCreparHor.append(nbCreparHor)
            if maxNbCreparHor < nbCreparHor:
                maxNbCreparHor = nbCreparHor
        #ajout du nombre de ligne maximal
        self.jour.setRowCount(0)
        self.jour.setRowCount(maxNbCreparHor)

        for creneau in Creneaux.listCreneaux:
            if creneau.loc != ['', '']:
                li = creneau.loc[0]
                col = creneau.loc[1]
                horaire = HORAIRE[col]
                if creneau.duree == '2H' and HORAIRE.index(horaire)%2 == 0:
                    self.jour.setSpan(li,col,1,2)
                if self.j == "V" and creneau.benevole_vendredi != "":
                    item = M.item_rempli(creneau.categorie +" : "+
                                             creneau.nom + "\n" +
                                             creneau.benevole_vendredi)
                    self.jour.setItem(li, col, item)
                elif self.j == "S" and creneau.benevole_samedi != "":
                    item = M.item_rempli(creneau.categorie +" : "+
                                             creneau.nom + "\n" +
                                             creneau.benevole_samedi)
                    self.jour.setItem(li, col, item)
                else:
                    item = M.item_normal_non_actif(creneau.categorie +" : "+ creneau.nom)
                    self.jour.setItem(li, col, item)

        for benevole in Benevoles.listBenevoles:
            self.filtre.addItem(benevole.nom)
        self.jour.resizeRowsToContents()

    def definir_liste_benevoles(self, li, col):
        """Definit la liste de benevoles disponible pour le creneau considéré"""
        benevolesDispo = []
        if li >= 0 and col >= 0:
            for creneau in Creneaux.listCreneaux:
                if creneau.loc == [li, col]:
                    duree = creneau.duree
                    categorie = creneau.categorie
                    horaire = creneau.plage_horaire
                    break
            #horaire du creneau sélectionné
            creneau = self.jour.item(li, col).text()
            #categorie du creneau selectionné
            benevolesOccupe = creneau_benevole_occupe(self.jour, col, self.listNbCreparHor, duree)
            if self.j == "V":
                for benevole in Benevoles.listBenevoles:
                    # permet de vérifier que le benevole est bien activé par l'utilisateur
                    # le benevole ne doit pas avoir plus de créneaux que définit
                    if benevole.actif_vendredi:
                        if creneau_depassement(self.qCre, benevole.creneaux_vendredi, duree):
                            if creneau_consecutif(col, benevole.creneaux_vendredi, duree):
                                #le benevole ne doit pas déjà avoir d'autre créneau dans la même heure
                                if not(benevole.nom in benevolesOccupe):
                                    if creneau_categorie(self.voeuxC,categorie, benevole):
                                        if creneau_artistes(self.voeuxA, self.artistes, horaire, benevole.artiste_vendredi):
                                            benevolesDispo.append(nom_proposition(benevole.nom, benevole.creneaux_vendredi))
            elif self.j == "S":
                for benevole in Benevoles.listBenevoles:
                    # permet de vérifier que le benevole est bien activé par l'utilisateur
                    if benevole.actif_samedi:
                        # le benevole ne doit pas avoir plus de créneaux que définit
                        if creneau_depassement(self.qCre, benevole.creneaux_samedi, duree):
                            if creneau_consecutif(col, benevole.creneaux_samedi, duree):
                                #le benevole ne doit pas déjà avoir d'autre créneau dans la même heure
                                if not(benevole.nom in benevolesOccupe):
                                    if creneau_categorie(self.voeuxC,categorie,benevole):
                                            if creneau_artistes(self.voeuxA, self.artistes, horaire, benevole.artiste_samedi):
                                                benevolesDispo.append(nom_proposition(benevole.nom, benevole.creneaux_samedi))

        return benevolesDispo


    def setNomBenevole(self, li, col):
        """Enregistre et met en forme le benevole choisit pour le creneau sélectionné"""
        nomCreneauH2 = ''
        cat_creneau = self.jour.item(li, col).text().split("\n")[0].split(" : ")[0]
        nom_creneau = self.jour.item(li, col).text().split("\n")[0].split(" : ")[1]
        hor_creneau = HORAIRE[col]
        nomCreneau = mef_nom_creneau(cat_creneau, nom_creneau, hor_creneau)
#        nomCreneau = self.jour.item(li, col).text().split("\n")[0] + " : " + self.jour.horizontalHeaderItem(col).text()
        try:
            ancien_benevole = self.jour.item(li, col).text().split("\n")[1]
        except:
            ancien_benevole = False
        #si l'horaire est un début de créneau de deux heures
        if HORAIRE.index(self.jour.horizontalHeaderItem(col).text())%2 == 0:
            for creneau in Creneaux.listCreneaux:
                if creneau.loc[0] == li and creneau.loc[1] == col:
                    if creneau.duree == "2H":
#                        cat_creneauH2 = self.jour.item(li, col).text().split("\n")[0].split(" : ")[0]
#                        nom_creneauH2 = self.jour.item(li, col).text().split("\n")[0].split(" : ")[1]
                        hor_creneauH2 = HORAIRE[col+1]
                        nomCreneauH2 = mef_nom_creneau(cat_creneau, nom_creneau, hor_creneauH2)
#                        nomCreneauH2 = self.jour.item(li, col).text().split("\n")[0] + " : "+ str(self.jour.horizontalHeaderItem(col+1).text())
                    break
        self.benevoleChoisi = self.benevoleChoisi.split(" ;")[0]
        #permet d'ajouter le nouveau benevole dans le tableau
        if self.j == "V":
            for creneau in Creneaux.listCreneaux:
                if creneau.loc[0] == li and creneau.loc[1] == col:
                    creneau.benevole_vendredi = str(self.benevoleChoisi)
                    item = M.item_rempli(creneau.categorie + " : "
                                         + creneau.nom + "\n"
                                         + creneau.benevole_vendredi)
                    self.jour.setItem(li, col, item)
                    break
            for benevole in Benevoles.listBenevoles:
                if benevole.nom == self.benevoleChoisi:
                    benevole.creneaux_vendredi.append(nomCreneau)
                    if nomCreneauH2:
                        benevole.creneaux_vendredi.append(nomCreneauH2)
                #permet de supprimer l'ancien benevole
                if benevole.nom == ancien_benevole:
                    if nomCreneau in benevole.creneaux_vendredi:
                        benevole.creneaux_vendredi.remove(nomCreneau)
                    if nomCreneauH2 and nomCreneauH2 in benevole.creneaux_vendredi:
                        benevole.creneaux_vendredi.remove(nomCreneauH2)
        elif self.j == "S":
            for creneau in Creneaux.listCreneaux:
                if creneau.loc[0] == li and creneau.loc[1] == col:
                    creneau.benevole_samedi = str(self.benevoleChoisi)
                    item = M.item_rempli(creneau.categorie + " : "
                                         + creneau.nom + "\n"
                                         + creneau.benevole_samedi)
                    self.jour.setItem(li, col, item)
            for benevole in Benevoles.listBenevoles:
                if benevole.nom == str(self.benevoleChoisi):
                    benevole.creneaux_samedi.append(nomCreneau)
                    if nomCreneauH2:
                        benevole.creneaux_samedi.append(nomCreneauH2)
                # permet de supprimer l'ancien benevole
                if benevole.nom == ancien_benevole:
                    if nomCreneau in benevole.creneaux_samedi:
                        benevole.creneaux_samedi.remove(nomCreneau)
                    if nomCreneauH2 and nomCreneauH2 in benevole.creneaux_samedi:
                        benevole.creneaux_samedi.remove(nomCreneauH2)

        Benevoles.maj_benevoles(self.tabBenevoles, self.qCre)
        Creneaux.maj_creneaux(self.tabCreneaux)
        self.jour.resizeRowsToContents()

    def vider_cell(self):
        """Supprime le benevole"""
        li = self.jour.currentRow()
        col = self.jour.currentColumn()
        nomCreneau = self.jour.item(li, col).text().split("\n")[0]
        cat_creneau = nomCreneau.split(" : ")[0]
        nom_creneau = nomCreneau.split(" : ")[1]
        horaire = HORAIRE[col]
        nom_complet_creneau = mef_nom_creneau(cat_creneau, nom_creneau, horaire)
        nomCreneauH2 = ''
         #self.jour.horizontalHeaderItem(col+1).text()
        #si l'horaire est un début de créneau de deux heures
        if HORAIRE.index(horaire)%2 == 0:
            for creneau in Creneaux.listCreneaux:
                if creneau.loc[0] == li and creneau.loc[1] == col:
                    if creneau.duree == "2H":
                                nomCreneauH2 = self.jour.item(li, col).text().split("\n")[0]
                                cat_creneauH2 = nomCreneauH2.split(" : ")[0]
                                nom_creneauH2 = nomCreneauH2.split(" : ")[1]
                                horaireH2 = HORAIRE[col+1]
                                nom_complet_creneauH2 = mef_nom_creneau(cat_creneauH2, nom_creneauH2, horaireH2)
                                break
        if self.j == "V":
            for creneau in Creneaux.listCreneaux:
                if creneau.loc[0] == li and creneau.loc[1] == col:
                    if creneau.benevole_vendredi != "":
                        benevole_en_cours = self.jour.item(li, col).text().split("\n")[1]
                        creneau.benevole_vendredi = ""
                        for benevole in Benevoles.listBenevoles:
                            if benevole.nom == benevole_en_cours:

                                if nom_complet_creneau in benevole.creneaux_vendredi:
                                    benevole.creneaux_vendredi.remove(nom_complet_creneau)
                                if creneau.duree == '2H':
                                    if nom_complet_creneauH2 in benevole.creneaux_vendredi:
                                        benevole.creneaux_vendredi.remove(nom_complet_creneauH2)
                                break
        elif self.j == "S":
            for creneau in Creneaux.listCreneaux:
                if creneau.loc[0] == li and creneau.loc[1] == col:
                    if creneau.benevole_samedi != "":
                        benevole_en_cours = self.jour.item(li, col).text().split("\n")[1]
                        creneau.benevole_samedi = ""
                        for benevole in Benevoles.listBenevoles:
                            if benevole.nom == benevole_en_cours:
                                if nom_complet_creneau in benevole.creneaux_samedi:
                                    benevole.creneaux_samedi.remove(nom_complet_creneau)
                                if creneau.duree == '2H':
                                    if nom_complet_creneauH2 in benevole.creneaux_samedi:
                                        benevole.creneaux_samedi.remove(nom_complet_creneauH2)
                                    break



        item = M.item_normal(nomCreneau)
        self.jour.setItem(li, col, item)
        Benevoles.maj_benevoles(self.tabBenevoles, self.qCre)
        Creneaux.maj_creneaux(self.tabCreneaux)
        self.jour.resizeRowsToContents()

    def remplissage_auto(self):
        """Rempli automatiquement les creneaux vides"""
        Creneaux.tri_creneaux_auto()
        benevole_precedent_vendredi = False
        benevole_precedent_samedi = False
        for creneau in Creneaux.listCreneaux:
            benevolesDispoV = []
            benevolesDispoV_qte = []
            benevolesDispoS = []
            benevolesDispoS_qte = []
            benevolesV = []
            benevolesS = []
            for benevole in Benevoles.listBenevoles:
                # permet de vérifier que le benevole est bien activé par l'utilisateur
                if benevole.actif_vendredi:
                    # le creneau doit être vide
                    if not creneau.benevole_vendredi:
                        #teste pour savoir si le creneau est de 2h et de le debut
                        if creneau_depassement(self.qCre, benevole.creneaux_vendredi, creneau.duree):
                            if creneau_consecutif(HORAIRE.index(creneau.plage_horaire), benevole.creneaux_vendredi, creneau.duree):
                                if creneau_categorie(self.voeuxC, creneau.categorie, benevole):
                                        if creneau_artistes(self.voeuxA, self.artistes, creneau.plage_horaire, benevole.artiste_vendredi):
                                                    benevolesDispoV.append(benevole.nom)
                                                    benevolesDispoV_qte.append(len(benevole.creneaux_vendredi))
                if benevole.actif_samedi:
                    # le creneau doit être vide
                    if not creneau.benevole_samedi:
                        #teste pour savoir si le creneau est de 2h et de le debut
                        if creneau_depassement(self.qCre, benevole.creneaux_samedi, creneau.duree):
                            if creneau_consecutif(HORAIRE.index(creneau.plage_horaire), benevole.creneaux_samedi, creneau.duree):
                                if creneau_categorie(self.voeuxC, creneau.categorie, benevole):
                                        if creneau_artistes(self.voeuxA, self.artistes, creneau.plage_horaire, benevole.artiste_samedi):
                                                    benevolesDispoS.append(benevole.nom)
                                                    benevolesDispoS_qte.append(len(benevole.creneaux_samedi))

            for cre in Creneaux.listCreneaux:
                if cre.plage_horaire == creneau.plage_horaire:
                    if cre.benevole_vendredi in benevolesDispoV:
                        benevolesDispoV_qte.pop(benevolesDispoV.index(cre.benevole_vendredi))
                        benevolesDispoV.remove(cre.benevole_vendredi)
                    if cre.benevole_samedi in benevolesDispoS:
                        benevolesDispoS_qte.pop(benevolesDispoS.index(cre.benevole_samedi))
                        benevolesDispoS.remove(cre.benevole_samedi)
                if  creneau.duree == '1H':
                    if cre.duree == '2H' and cre.plage_horaire == HORAIRE[HORAIRE.index(creneau.plage_horaire)-1]:
                        if cre.benevole_vendredi in benevolesDispoV:
                            benevolesDispoV_qte.pop(benevolesDispoV.index(cre.benevole_vendredi))
                            benevolesDispoV.remove(cre.benevole_vendredi)
                        if cre.benevole_samedi in benevolesDispoS:
                            benevolesDispoS_qte.pop(benevolesDispoS.index(cre.benevole_samedi))
                            benevolesDispoS.remove(cre.benevole_samedi)
                if creneau.duree == '2H':
                    if cre.duree == '1H' and cre.plage_horaire == HORAIRE[HORAIRE.index(creneau.plage_horaire)+1]:
                        if cre.benevole_vendredi in benevolesDispoV:
                            benevolesDispoV_qte.pop(benevolesDispoV.index(cre.benevole_vendredi))
                            benevolesDispoV.remove(cre.benevole_vendredi)
                        if cre.benevole_samedi in benevolesDispoS:
                            benevolesDispoS_qte.pop(benevolesDispoS.index(cre.benevole_samedi))
                            benevolesDispoS.remove(cre.benevole_samedi)

            if benevolesDispoV_qte:
                min_vendredi = min(benevolesDispoV_qte)
                for i in range(len(benevolesDispoV_qte)):
                    if benevolesDispoV_qte[i] == min_vendredi:
                        benevolesV.append(benevolesDispoV[i])
            else:
                benevolesV = benevolesDispoV

            if benevolesDispoS_qte:
                min_samedi = min(benevolesDispoS_qte)
                for i in range(len(benevolesDispoS_qte)):
                    if benevolesDispoS_qte[i] == min_samedi:
                        benevolesS.append(benevolesDispoS[i])
            else:
                benevolesS = benevolesDispoS

            if benevolesV:
                if benevole_precedent_vendredi:
                    for benevole in Benevoles.listBenevoles:
                        if benevole_precedent_vendredi in benevole.remarques:
                            if benevole.nom in benevolesV:
                                creneau.benevole_vendredi = benevole.nom
                                benevole_precedent_vendredi = creneau.benevole_vendredi
                                break

                if not creneau.benevole_vendredi:
                    nombre_aleatoire = randrange(0,len(benevolesV))
                    creneau.benevole_vendredi = benevolesV[nombre_aleatoire]
                    benevole_precedent_vendredi = creneau.benevole_vendredi
                for benevole in Benevoles.listBenevoles:
                    if benevole.nom == creneau.benevole_vendredi:
                        cat_creneau = creneau.categorie
                        nom_creneau = creneau.nom
                        horaire = creneau.plage_horaire
                        nom_complet_creneau = mef_nom_creneau(cat_creneau, nom_creneau, horaire)
                        benevole.creneaux_vendredi.append(nom_complet_creneau)
                        if creneau.duree == '2H':
                            horaire = HORAIRE[HORAIRE.index(creneau.plage_horaire)+1]
                            nom_complet_creneauH2 = mef_nom_creneau(cat_creneau, nom_creneau, horaire)
                            benevole.creneaux_vendredi.append(nom_complet_creneauH2)
                        break

            if benevolesS:
                if benevole_precedent_samedi:
                    for benevole in Benevoles.listBenevoles:

                        if benevole_precedent_samedi in benevole.remarques:
                            if benevole.nom in benevolesS:
                                creneau.benevole_samedi = benevole.nom
                                benevole_precedent_samedi = creneau.benevole_samedi
                                break

                if not creneau.benevole_samedi:
                    nombre_aleatoire = randrange(0,len(benevolesS))
                    creneau.benevole_samedi = benevolesS[nombre_aleatoire]
                    benevole_precedent_samedi = creneau.benevole_samedi
                for benevole in Benevoles.listBenevoles:
                    if benevole.nom == creneau.benevole_samedi:
                        cat_creneau = creneau.categorie
                        nom_creneau = creneau.nom
                        horaire = creneau.plage_horaire
                        nom_complet_creneau = mef_nom_creneau(cat_creneau, nom_creneau, horaire)
                        benevole.creneaux_samedi.append(nom_complet_creneau)
                        if creneau.duree == '2H':
                            horaire = HORAIRE[HORAIRE.index(creneau.plage_horaire)+1]
                            nom_complet_creneauH2 = mef_nom_creneau(cat_creneau, nom_creneau, horaire)
                            benevole.creneaux_samedi.append(nom_complet_creneauH2)
                        break
        self.jour.resizeRowsToContents()
        Creneaux.tri_creneaux()
