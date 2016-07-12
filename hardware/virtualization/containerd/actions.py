#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("GOPATH", "%s" % get.workDIR())
    
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("containerd-*", "containerd")
    
    shelltools.makedirs("src/github.com/docker")
    shelltools.system("ln -rsf containerd*  src/github.com/docker")

    shelltools.cd("src/github.com/docker/containerd")
    
    shelltools.system("LDFLAGS= make")

def install():
    pisitools.dobin("bin/*")
    
    pisitools.dodoc("MAINTAINERS", "README*")
