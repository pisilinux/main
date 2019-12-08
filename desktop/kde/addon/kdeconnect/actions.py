#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("CMakeLists.txt", "5.64.0", "5.62.0")
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()
