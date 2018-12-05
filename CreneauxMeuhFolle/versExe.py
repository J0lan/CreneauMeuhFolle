# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:45:37 2017

@author: GANJO

pour lancer l'execution du script :
python versExe.py build

"""

from cx_Freeze import setup, Executable
import sys
import os


os.environ['TCL_LIBRARY'] = r'C:\Program Files\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\tcl\tk8.6'
#executables = [Executable("ControlUI.py")]

includes = ["benevoles",
            "creneaux",
            "ajout_benevole_DI",
            "ajout_creneau_DI",
            "choix_benevole_DI",
            "Jour",
            "MessBox",
            "resume",
            "svg_donnees",
            "fenetre_principale_UI"]

excludes = ["numpy", "babel", "Cython", "email", "matplotlib", "pandas",\
            "notebook", "sphinx", "scipy", "webencoding", "pandas_datareader",\
             "concurrent", "ctypes"\
            "et_xmlfile", "html", "http", "lib2to3", "logging",\
            "lxml", "pydoc_data", "tkinter", "osx_support", "PIL", "pycparser",\
            "setuptools", "unittest", "platform",]

buildOptions = {
        "includes" : includes,
        "include_files" : ["doc", "Image"],
        "path" : sys.path,
        "excludes" : excludes,
}

# On appelle la fonction setup
setup(
    name = "Gestion Créneaux MF",
    version = "1",
    description = "Votre programme",
    options = {"build_exe" : buildOptions},
    executables = [Executable("ControlUI.py",base="Win32GUI")],
)

os.system("pause")