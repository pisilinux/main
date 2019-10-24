#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    
	cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
						  -DOCLICD_COMPAT=0")
    
def build():
    cmaketools.make()

def install():
    
    autotools.rawInstall("DESTDIR=%s" %get.installDIR())
    
     
