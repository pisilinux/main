#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import python3modules

def build():
    python3modules.compile(pyVer="3")

def install():
    python3modules.install(pyVer="3")
