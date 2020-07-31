=============
einfachpython
=============

Source code zum Blog einfachpython.de



Description
===========

This is the source code for a german blog einfachpython.de

Documentation and readme will be in written in german, the source code will be english.

Installation als Entwickler
===========================

Erstelle eine neue virtuelle Python Umgebung

  $ python3 -m venv venv

Aktiviere die virtuelle Umgebung

  $ source venv/bin/activate

Installiere das Package

  (venv)$ pip install -r requirements-dev.txt

oder im editable Modus (installiert wie ein normales Package aber alle
Änderungen werden direkt berücksichtigt ohne neu installieren zu müssen)

  (venv)$ pip install -e .[testing]



Sphinx Documentation
====================

Die Sphinx Docs können über ein make Kommando erstellt werden.

  make -C docs html


Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
In addition a cookiecutter template was used.
https://pyscaffold.org/en/latest/cookiecutter-integration.html

