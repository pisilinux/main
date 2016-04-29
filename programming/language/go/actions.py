#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("GOROOT", "%s/go-go1.6.2" % get.workDIR())
shelltools.export("GOBIN", "$GOROOT/bin")
shelltools.export("GOPATH", "%s" % get.workDIR())
shelltools.export("GOROOT_FINAL", "/usr/lib/go")
shelltools.export("GOROOT_BOOTSTRAP", "%s/go-go1.6.2/go-linux-amd64-bootstrap" % get.workDIR())

shelltools.export("GOHOSTARCH","amd64")
shelltools.export("GOHOSTOS","linux")
shelltools.export("CC", "gcc")

shelltools.export("GOOS","linux")
shelltools.export("GOARCH","amd64")

shelltools.export("CC_FOR_TARGET", "gcc")
shelltools.export("CXX_FOR_TARGET", "g++")

NoStrip=["/"]

def build():
    shelltools.cd("src")

    shelltools.system("./make.bash")

    #shelltools.cd("%s/go-go1.6.2" % get.workDIR())

    #shelltools.system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/godoc")
    #shelltools.system("$GOROOT/bin/go build -o $GOPATH/godoc golang.org/x/tools/cmd/godoc")

    #for tool in ["godex", "godoc", "goimports", "gomvpkg", "gorename", "gotype", "benchcmp", "bundle", "callgraph", "digraph", "eg", "fiximports", "html2article", "oracle", #"present", "ssadump", "stress", "stringer"]:
    #    shelltools.system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/%s" % tool)
    #    shelltools.system("$GOROOT/bin/go build -v -x -o $GOROOT/pkg/tool/$GOOS\_$GOARCH/%s golang.org/x/tools/cmd/%s" % (tool, tool))


def install():  
    shelltools.cd("%s/go-go1.6.2" % get.workDIR())

    pisitools.dodir("/usr/lib/go")
    pisitools.insinto("/usr/lib/go", "bin")
    
    pisitools.dosym("/usr/lib/go/bin/go", "/usr/bin/go")
    pisitools.dosym("/usr/lib/go/bin/gofmt", "/usr/bin/gofmt")
    
    pisitools.insinto("/usr/lib/go", "doc")
    pisitools.insinto("/usr/lib/go", "lib")
    pisitools.insinto("/usr/lib/go", "pkg")
    pisitools.insinto("/usr/lib/go", "src")

    shelltools.chmod("%s/usr/lib/go/bin" % get.installDIR(), 0755)
    shelltools.chmod("%s/usr/lib/go/pkg/tool" % get.installDIR(), 0755)

    pisitools.insinto("/usr/lib/go", "misc")
    
    pisitools.removeDir("/usr/lib/go/pkg/bootstrap")
 
    pisitools.dodoc("VERSION", "LICENSE", "PATENTS", "README*", "AUTHORS", "CONTRIBUTORS")
