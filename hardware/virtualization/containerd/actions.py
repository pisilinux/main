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
    
    shelltools.cd("containerd")
    shelltools.move("vendor", "src")
    
    shelltools.makedirs("src/github.com/containerd")
    shelltools.system("ln -rsf %s/containerd*  src/github.com/containerd" % get.workDIR())

    shelltools.cd("src/github.com/containerd/containerd")
    
    #shelltools.system("LDFLAGS= GOPATH=%s make GIT_COMMIT=72cec4b" % get.curDIR())

    shelltools.system("LDFLAGS= make GIT_COMMIT=a17ec49 EXTRA_LDFLAGS='-buildid='")

def install():
    shelltools.cd("%s/containerd" % get.workDIR())

    #pisitools.dobin("bin/*")
    autotools.rawInstall("DESTDIR=%s/usr" % get.installDIR())

    # symlink containerd/run (nice integration with docker)
    pisitools.dosym("/usr/bin/containerd", "/usr/bin/docker-containerd")
    pisitools.dosym("/usr/bin/containerd-shim", "/usr/bin/docker-containerd-shim")
    pisitools.dosym("/usr/bin/ctr", "/usr/bin/docker-containerd-ctr")
    
    pisitools.dodoc("LICENSE", "README*")
