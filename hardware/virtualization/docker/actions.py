#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# shelltools.export("DISABLE_WARN_OUTSIDE_CONTAINER", "1")
shelltools.export("AUTO_GOPATH", "1")
shelltools.export("DOCKER_GITCOMMIT","b40c2f6")
shelltools.export("IAMSTATIC", "false")
shelltools.export("VERSION", "20.10.18")
shelltools.export("GOROOT","/usr/lib/go")
shelltools.export("GO111MODULE","off")

# shelltools.export("GOPATH", "%s/cli-%s" % (get.workDIR(), get.srcVERSION()))

shelltools.export("GOPATH", "%s" % get.workDIR())
shelltools.export("CGO_CFLAGS", "-I/usr/include")
shelltools.export("CGO_LDFLAGS", "-L/usr/lib")
shelltools.export("DOCKER_BUILDTAGS","seccomp")
  
NoStrip=["/"]

def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("cli-*", "cli")
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("moby-*", "engine")
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("docker-ce-packaging-19.03.13", "packaging")

    # shelltools.copy( "../moby-%s/*" % get.srcVERSION(), "engine")
    shelltools.makedirs("cli/src/github.com/docker/docker")
    shelltools.cd("cli/src/github.com/docker")
    shelltools.system("ln -s ../../../../cli . ")

def build():
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("engine")
    # shelltools.makedirs("github.com/docker/docker")
    # shelltools.system("make VERSION=%s dynbinary-daemon" % get.srcVERSION())
    shelltools.system("hack/make.sh dynbinary-daemon")
    # shelltools.system("make.sh dynbinary-daemon")
    
    # build
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("cli")
    shelltools.system("LDFLAGS='' GOPATH=%s/cli ./scripts/build/binary" % get.workDIR())

def install():
    shelltools.cd("%s/cli" % get.workDIR())
    
    pisitools.dobin("build/docker*")

    shelltools.cd("%s" % get.workDIR())
    pisitools.dobin("engine/bundles/dynbinary-daemon/*")
       
    # insert udev rules
    pisitools.insinto("/lib/udev/rules.d", "engine/contrib/udev/*.rules")

    #insert contrib in docs
    pisitools.insinto("/usr/share/doc/docker", "cli/contrib")
    
    pisitools.dobin("engine/contrib/check-config.sh")

    shelltools.cd("%s/cli" % get.workDIR())
    pisitools.dodoc("VERSION", "README.md","CONTRIBUTING.md")
