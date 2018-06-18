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
NoStrip = "/"

def setup():
    shelltools.move("vendor", "src")
    
    shelltools.makedirs("src/github.com/docker")
        
    shelltools.cd("src/github.com/docker")
    shelltools.system("ln -rsf %s/libnetwork ./libnetwork" % get.workDIR())

def build():
    shelltools.cd("src/github.com/docker/libnetwork")
        
    shelltools.system("GOPATH=%s/libnetwork make build-local" % get.workDIR())

def install():
    pisitools.dobin("bin/dnet")
    pisitools.dobin("bin/docker-proxy")
    
    pisitools.dodoc("MAINTAINERS", "LICENSE", "README*", "ROADMAP.md")
    
    shelltools.unlinkDir("docs/vagrant-systemd")
    
    pisitools.insinto("/usr/share/doc/libnetwork", "docs/*")
