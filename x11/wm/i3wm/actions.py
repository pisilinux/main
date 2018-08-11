#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

def setup():
    autotools.configure()

def build():
    shelltools.cd("x86_64-pc-linux-gnu")
    
    autotools.make()

def install():
    shelltools.cd("x86_64-pc-linux-gnu")
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
