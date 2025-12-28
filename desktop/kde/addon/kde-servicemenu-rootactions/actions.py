#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# WorkDir = "rootactions_servicemenu_%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-iv")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # pisitools.insinto("/usr/share/kservices5/ServiceMenus", "Root_Actions_%s/dolphin-KDE4/*.desktop" % get.srcVERSION())
    # pisitools.dobin("Root_Actions_%s/rootactions-servicemenu.pl" % get.srcVERSION())

    pisitools.dodoc("README*")
