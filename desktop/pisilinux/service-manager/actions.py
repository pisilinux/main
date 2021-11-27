#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

def build():
    shelltools.system("python setup.py build")

def install():
    pythonmodules.install()
