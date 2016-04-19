#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools



def setup():    
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release  \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DBURNING=LIBBURNIA ")

def build():
    cmaketools.make()

def install():
    cmaketools.install()    
    
#pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "LICENSE", "TODO")
   
