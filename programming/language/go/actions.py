#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/"]

def build():
    shelltools.export("go_platform","linux-amd64")
    shelltools.export("go_linker","/lib/ld-linux-x86-64.so.2")

    shelltools.export("GOROOT", "%s/go-go1.11.9" % get.workDIR()) #0

    shelltools.export("GOBIN", "$GOROOT/bin") #1
    shelltools.export("GOPATH", "%s" % get.workDIR())
    shelltools.export("GOROOT_FINAL", "/usr/lib/go")
    shelltools.export("GOROOT_BOOTSTRAP", "%s/go-go1.11.9/go-linux-amd64-bootstrap" % get.workDIR())  #2

    shelltools.export("GOOS","linux")
    shelltools.export("GOARCH","amd64")
    
    shelltools.cd("src")

    shelltools.system("./make.bash")

def install():
    shelltools.export("GOROOT_FINAL", "/usr/lib/go")
    shelltools.cd("%s/go-go1.11.9" % get.workDIR())

    pisitools.dodir("/usr/lib/go")
    shelltools.system("cp -r api bin doc lib pkg src  %s/usr/lib/go" % get.installDIR())
    shelltools.system("chown -R  root:root %s/usr" % get.installDIR())

    pisitools.dosym("/usr/lib/go/bin/go", "/usr/bin/go")
    pisitools.dosym("/usr/lib/go/bin/gofmt", "/usr/bin/gofmt")

    pisitools.dosym("/usr/lib/go/doc", "/usr/share/doc/%s/doc" % get.srcNAME())
    pisitools.dosym("/usr/lib/go/api", "/usr/share/doc/%s/api" % get.srcNAME())

    shelltools.system("cp -r misc  %s/usr/lib/go" % get.installDIR())

    pisitools.removeDir("/usr/lib/go/pkg/bootstrap")

    # remove testdata, which hit cave fix-linkage
    pisitools.remove("/usr/lib/go/src/debug/elf/testdata/gcc-386-freebsd-exec")
    pisitools.removeDir("/usr/lib/go/pkg/obj")

    # dirty fix thanks @erturk
    pisitools.removeDir("/usr/lib/go/pkg/linux_amd64")
    

    pisitools.dodoc("VERSION", "LICENSE", "PATENTS", "README*", "AUTHORS", "CONTRIBUTORS")
