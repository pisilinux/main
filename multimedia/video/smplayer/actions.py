#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("Makefile", "^DOC_PATH=.*$", "DOC_PATH=$(PREFIX)/share/doc/smplayer")
    pisitools.dosed("Makefile", "PREFIX=/usr/local", "PREFIX=/usr")

def build():
    autotools.make("PREFIX=/usr QMAKE=/usr/bin/qmake -j1 LRELEASE=/usr/bin/lrelease")
    
    shelltools.cd("smplayer-skins-15.2.0")
    autotools.make("PREFIX=/usr")
    
    shelltools.cd("..")
    shelltools.cd("smplayer-themes-18.6.0")
    autotools.make("PREFIX=/usr")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s DOC_PATH=/usr/share/doc/%s" % (get.installDIR(),get.srcNAME()))
    
    shelltools.cd("smplayer-skins-15.2.0")
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr install" % get.installDIR())
    
    shelltools.cd("..")
    shelltools.cd("smplayer-themes-18.6.0")
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr install" % get.installDIR())
    
