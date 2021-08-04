#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("AUTO_GOPATH", "1")
shelltools.export("DOCKER_GITCOMMIT","99e3ed8")
shelltools.export("IAMSTATIC", "false")
shelltools.export("VERSION", "19.03.15")
shelltools.export("GOROOT","/usr/lib/go")

shelltools.export("GOPATH", "%s" % get.workDIR())
shelltools.export("CGO_CFLAGS", "-I/usr/include")
shelltools.export("CGO_LDFLAGS", "-L/usr/lib")
shelltools.export("DOCKER_BUILDTAGS","seccomp")
  
NoStrip=["/"]

def setup():
    shelltools.makedirs("components/cli/src/github.com/docker")
    shelltools.cd("components/cli/src/github.com/docker")
    shelltools.system("ln -s ../../../../cli . ")

def build():
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("docker-ce-%s/components/engine" % get.srcVERSION())
    shelltools.system("hack/make.sh dynbinary-daemon")
    
    # build cli
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("docker-ce-%s/components/cli" % get.srcVERSION())
    shelltools.system("LDFLAGS='' GOPATH=%s/docker-ce-%s/components/cli ./scripts/build/dynbinary" % (get.workDIR(), get.srcVERSION()))

def install():
    shelltools.cd("%s/docker-ce-%s" % (get.workDIR(), get.srcVERSION()))
    
    pisitools.dobin("components/cli/build/docker*")
    pisitools.dobin("components/engine/bundles/dynbinary-daemon/*")
       
    # insert udev rules
    pisitools.insinto("/lib/udev/rules.d", "components/engine/contrib/udev/*.rules")

    #insert contrib in docs
    pisitools.insinto("/usr/share/doc/docker", "components/cli/contrib")
    
    pisitools.dobin("components/engine/contrib/check-config.sh")

    pisitools.dodoc("VERSION", "README.md","CONTRIBUTING.md", "CHANGELOG.md")
