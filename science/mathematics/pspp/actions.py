#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get 


def setup():
    pisitools.dosed("src/ui/gui/gen-dot-desktop.sh", "Math;", "")
    autotools.configure("--disable-rpath \
                         --disable-static")
                         #--without-libreadline-prefix")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    pisitools.dodir("/usr/share/pspp/contrib")
    pisitools.insinto("/usr/share/pspp/contrib" , "pspp-mode.el")
 
