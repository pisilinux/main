#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, python3modules, shelltools

def setup():
	pass

def build():
	shelltools.system("python3 -m build --wheel --no-isolation") #autotools.make()

def install():
	python3modules.install()

