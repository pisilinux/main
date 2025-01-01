#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()
