# -*- coding: utf-8 -*-

"""
Created on Thu Jun  8 10:34:56 2017

@author: GANJO
"""

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtGui, QtCore


def confirmer_suppression(types):
    """Boite de dialogue, pour confirmer la suppression de benevoles ou creneaux"""
    msg = QMessageBox()
    msg.setText("Voulez vous vraiment supprimer ce {}".format(types))
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    choix = msg.exec()
    return choix

def action_realisee(texte):
    """Boite de dialogue, pour indiquer que l'export ou l'import est terminé"""
    msg = QMessageBox()
    msg.setText(texte)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def creneau_2e_heure():
    """Boite de dialogue, pour empecher l'utilisateur de mofifier la deuxième heures d'un creneau"""
    msg = QMessageBox()
    msg.setText("Action non autorisé \nCe créneau est la deuxième heure d'un creneau de 2H")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def aucun_benevole():
    """Boite de dialogue, pour empecher l'utilisateur de mofifier la deuxième heures d'un creneau"""
    msg = QMessageBox()
    msg.setText("Aucun Benevole disponible pour ce creneau. \nEssayez d'augmeenter le nombre de creneau par bénévole")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def sup_impossible(texte, texte2):
    """Boite de dialogue pour empecher la suppression d'un creneau ou benevoles
    ayant déjà été utilisé.
    Il faudra d'abord supprimer les créneaux ou le bénévoles est concerné etcefec
    """
    msg = QMessageBox()
    msg.setWindowTitle("Suppression Impossible")
    msg.setText("Impossible de supprimer ce {} possède déjà un ou plusieurs {}.\
                \nVous devez d'abord supprimer le(s) {}".format(texte, texte2, texte2))
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def aucune_donnees():
    msg = QMessageBox()
    msg.setWindowTitle("Aucune données importées")
    msg.setText("Tu dois d'abord importer des données pour avoir accès à cette fonction.\n\
                Pour en savoir plus, se référer à la documentation.")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def question_enregistrer():
    """Boite de dialogue, pour confirmer l'enregistrement"""
    msg = QMessageBox()
    msg.setText("Veux-tu enregistrer avant de quitter ?\n\
                Tu pourrais le regretter !\n\
                (Pour la prochaine fois Ctrl+S)")
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    choix = msg.exec()
    return choix

def question_calcul_auto():
    """Boite de dialogue, pour confirmer le lancement du calcul automatique"""
    msg = QMessageBox()
    msg.setText("Est tu sur de vouloir lancer le calcul automatique ?")
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    choix = msg.exec()
    return choix


### on va définir ici des méthodes à appliquer à des items de QtableWidget en fontion des conditions


### widget normal : Créneaux sans benevoles

def item_entete(texte):
    """Item pour remplir l'entete d'un QTableWidget"""
    item = QtWidgets.QTableWidgetItem(texte)
    item.setFlags(QtCore.Qt.NoItemFlags)
    return item

def item_normal(texte):
    """Item pour remplir un Qtablewidget avec du texte noir"""
    if texte:
        texte = texte.title()
        item = QtWidgets.QTableWidgetItem(texte)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
    else:
        texte = ''
        item = QtWidgets.QTableWidgetItem(texte)
    return item

def item_tab_hor_artistes(texte):
    """Item pour remplir un Qtablewidget avec du texte noir"""
    if texte:
        texte = texte.title()
        item = QtWidgets.QTableWidgetItem(texte)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
    else:
        texte = ''
        item = QtWidgets.QTableWidgetItem(texte)
    return item
def item_normal_non_editable(texte):
    """Item pour remplir un Qtablewidget avec du texte noir.
    Item non modifiable depuis le tableau"""
    if texte:
        texte = texte.title()
        item = QtWidgets.QTableWidgetItem(texte)
        item.setFlags(item.flags()  & ~QtCore.Qt.ItemIsEditable)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
    else:
        texte = ''
        item = QtWidgets.QTableWidgetItem(texte)
        item.setFlags(item.flags()  & ~QtCore.Qt.ItemIsEditable)
    return item

def item_normal_non_actif(texte):
    """Item pour remplir un Qtablewidget avec du texte noir.
    Item non modifiable et non sélectionnable depuis le tableau
    """
    if texte:
        texte = texte.title()
        item = QtWidgets.QTableWidgetItem(texte)
#        item.setFlags(item.flags() & QtCore.Qt.ItemIsEnabled)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtCore.Qt.transparent)
    else:
        texte = ''
        item = QtWidgets.QTableWidgetItem(texte)
        item.setFlags(item.flags() & QtCore.Qt.ItemIsEnabled)
    return item

def item_normal_2e_heure(texte):
    """Item pour remplir un Qtablewidget avec du texte noir.
    Le fond est grisé pour signaler que le creneaux est la
    deuxième heures d'un creneau à ne pas essayer de modifier.
    Item non modifiable et non sélectionnable depuis le tableau
    """
    if texte:
        texte = texte.title()
        item = QtWidgets.QTableWidgetItem(texte)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setBackground(QtGui.QColor(200, 200, 200))
        item.setFlags(item.flags() & QtCore.Qt.ItemIsEnabled)
    else:
        texte = ''
        item = QtWidgets.QTableWidgetItem(texte)
        item.setFlags(item.flags() & QtCore.Qt.ItemIsEnabled)
    return item

def item_recherche(texte):
    """Item pour remplir un QTableWidget avec du texte noir.
    Le fond est jaune pour le démarquer des autres et retrouver
    le benevole recherché.
    """
    if texte:
        texte = texte.title()
        item = QtWidgets.QTableWidgetItem(texte)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setBackground(QtGui.QColor(0, 255, 0))
    else:
        texte = ''
        item = QtWidgets.QTableWidgetItem(texte)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
    return item

### widget vert : Créneaux avec benevoles
def item_rempli(texte):
    """Item si le créneaux possède un bénévole dans
    Vendredi ou Samedi, l'item sera coloré en vert clair
    Cette fonction est utilisé uniqement pour les créneaux
    d'1 heure ou la première heure d'un creneaux de 2 heures
    """
    item = QtWidgets.QTableWidgetItem(texte)
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    item.setBackground(QtGui.QColor(230, 200, 0))
    item.setForeground(QtGui.QColor(0, 0, 0))
#    item.setFlags(item.flags() & QtCore.Qt.ItemIsEnabled)
    return item

def item_rempli_2e_heure(texte):
    """Item si le créneaux possède un bénévole dans
    Vendredi ou Samedi, l'item sera coloré en vert foncé
    Cette fonction est utilisé uniqement pour la 2eme
    heures d'un creneau de 2H
    """
    item = QtWidgets.QTableWidgetItem(texte)
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    item.setBackground(QtGui.QColor(150, 0, 150))
    item.setForeground(QtGui.QColor(255, 255, 255))
    item.setFlags(item.flags() & QtCore.Qt.ItemIsEnabled)
    return item

def item_combobox(list_texte, select):
    """Item ajoutant une liste de déroulante dans les cases choisis
    Permet de limiter les soucis d'écriture et de syntaxe
    utilisé pour les plage_horaire, duree, categorie de creneaux et artistes
    """
    nb_valeur = len(list_texte)
    item = QtWidgets.QComboBox()
    if nb_valeur > 0:
        for i in range(nb_valeur):
            item.addItem(list_texte[i].title())
            item.setCurrentText(select.title())
    else:
        item.addItem("")
    return item

def item_normal_nb_creneaux(nb_creneau, quantite_creneau):
    """Cette item est utilisé exclusivement dans le tableau Benevoles
    Il permet de colorer le nombre de créneaux en fonction de ce nombre
    """
    texte = str(nb_creneau)
    if texte:
        texte = texte.title()
        item = QtWidgets.QTableWidgetItem(texte)
        item.setFlags(item.flags()  & ~QtCore.Qt.ItemIsEditable)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        if nb_creneau != 0:
            green_color = 255-nb_creneau*255/(quantite_creneau+4)
            item.setBackground(QtGui.QColor(0, green_color, 0))
    else:
        texte = ''
        item = QtWidgets.QTableWidgetItem(texte)
        item.setFlags(item.flags() & QtCore.Qt.ItemIsEnabled)
    return item


def nombre_format_horaire(temps_passe):
    """Définition du format horaire pour l'affichage du temps passé"""
    heures = temps_passe // 3600
    minutes = (temps_passe % 3600) / 60
    return str(int(heures)) + ":" + str(int(minutes))
