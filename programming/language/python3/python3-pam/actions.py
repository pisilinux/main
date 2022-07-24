#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pythonmodules, shelltools

def setup():
	pass

def build():
	shelltools.system("python3 setup.py build") #autotools.make()

def install():
	pythonmodules.install(pyVer = '3')

