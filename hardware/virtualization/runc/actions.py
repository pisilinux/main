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

shelltools.export("GOPATH", "%s" % get.workDIR())
shelltools.export("DOCKER_BUILDTAGS","seccomp")
shelltools.export("BINDIR","/usr/bin")

def build():
    autotools.make()

def install():
    pisitools.dobin("runc")
    
    # symlink containerd/run (nice integration with docker)
    pisitools.dosym("/usr/bin/runc", "/usr/bin/docker-runc")
    
    #insert completions in doc
    #pisitools.insinto("/usr/share/doc/runc", "contrib")
     
    pisitools.dodoc("MAINTAINERS", "README*")
