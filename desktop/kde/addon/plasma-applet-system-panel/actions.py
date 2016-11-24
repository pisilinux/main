#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

WorkDir= "plasma5-applets-system-panel-1.3.0/src"

def setup():
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()
