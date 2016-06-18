#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    pisitools.dosed("data/service-manager.desktop", "NotShowIn=KDE;", "")
    shelltools.system("python setup.py build")

def install():
    pythonmodules.install()

