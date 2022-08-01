#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("data/org.freedesktop.Accounts.service.in", "SystemdService", deleteLine=True)
    mesontools.configure("--prefix=/usr \
                             -Dsystemdsystemunitdir=no \
                             -Dadmin_group=wheel \
                             -Ddocbook=true \
                             -Dgtk_doc=true \
                             -Delogind=true \
                             -Dvapi=false \
                             --libexecdir=/usr/libexec")
    
def build():
    mesontools.build()
    
def install():
    mesontools.install()
    
    #shelltools.cd("..")
    pisitools.dodoc("README*", "COPYING", "TODO", "AUTHORS")
