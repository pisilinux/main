#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    pisitools.dobin("tini")
    pisitools.dobin("tini-static")
    
    # symlink docker-init (nice integration with docker)
    pisitools.dosym("/usr/bin/tini-static", "/usr/bin/docker-init")
    
    pisitools.dodoc("LICENSE", "README*", "VERSION")
