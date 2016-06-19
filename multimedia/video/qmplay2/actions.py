#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():    
     shelltools.system("qmake-qt5  QMPlay2.pro")         
    

def build():      
    qt5.make()

def install():    
    qt5.install()
    pisitools.insinto("/usr/bin/", "./app/bin/QMPlay2")
    pisitools.insinto("/usr/lib/", "./app/lib/libqmplay2.so")
    pisitools.insinto("/usr/share/qmplay2/modules/", "./app/share/qmplay2/modules/*")
    pisitools.insinto("/usr/share/qmplay2/lang/", "./lang/*")

    pisitools.dodoc( "README.md", "COPYING", "ChangeLog*")
