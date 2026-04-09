#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("DISABLE_WARN_OUTSIDE_CONTAINER", "1")
# shelltools.export("AUTO_GOPATH", "1")
shelltools.export("DOCKER_GITCOMMIT","daa0cb7")
shelltools.export("IAMSTATIC", "false")
shelltools.export("VERSION", "29.4.0")
shelltools.export("GOROOT","/usr/lib/go")
shelltools.export("GO111MODULE","off")

# shelltools.export("GOPATH", "%s/cli-%s" % (get.workDIR(), get.srcVERSION()))

# shelltools.export("GOPATH", "%s" % get.workDIR())
shelltools.export("CGO_CFLAGS", "-I/usr/include")
shelltools.export("CGO_LDFLAGS", "-L/usr/lib")
shelltools.export("DOCKER_BUILDTAGS","seccomp")
  
NoStrip=["/"]

def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("cli-*", "cli")
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("moby-docker-*", "moby-docker")
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("docker-ce-packaging-19.03.13", "packaging")

    # shelltools.copy( "../moby-%s/*" % get.srcVERSION(), "engine")
    shelltools.makedirs("cli/src/github.com/docker/docker")
    shelltools.cd("cli/src/github.com/docker")
    shelltools.system("ln -s ../../../../cli . ")

    # shelltools.cd("%s" % get.workDIR())
    # shelltools.makedirs("moby/github.com/moby/moby")
    # shelltools.cd("moby/src/github.com/moby")
    # shelltools.system("ln -s ../../../../../moby . ")

def build():
    # build
    # shelltools.cd("%s" % get.workDIR())
    # shelltools.cd("cli")
    # shelltools.system("LDFLAGS='' GOPATH=%s/cli ./scripts/build/binary" % get.workDIR())
    # gopath = "%s/go" % get.workDIR()
    # shelltools.cd("%s/go" % get.workDIR())

    # shelltools.cd("%s" % get.workDIR())
    # shelltools.makedirs("%s/src/github.com/docker" % gopath)
    # shelltools.makedirs("moby/src/github.com/moby")
    # shelltools.cd("%s/src/github.com/docker" % gopath)
    # shelltools.system("ln -sf %s/moby docker" % get.workDIR())
    # shelltools.cd("moby/src/github.com/moby")
    # shelltools.system("ln -s ../../../../moby . ")
    # shelltools.cd("moby")

    shelltools.cd("%s" % get.workDIR())

    shelltools.cd("moby-docker")
    shelltools.system("mkdir -p .gopath/src/github.com/moby/moby")
    shelltools.system("ln -sf $(pwd) .gopath/src/github.com/moby/moby/v2")

    shelltools.export("GOPATH", "%s/moby-docker/.gopath" % get.workDIR())
    # shelltools.makedirs("bundles/github.com/moby/moby/v2/cmd/dockerd")
    # shelltools.system("make VERSION=%s dynbinary-daemon" % get.srcVERSION())
    shelltools.system("hack/make.sh dynbinary")
    # shelltools.system("make.sh dynbinary-daemon")
    
    # build
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("cli")
    shelltools.system("LDFLAGS='' GOPATH=%s/cli ./scripts/build/binary" % get.workDIR())

def install():
    shelltools.cd("%s/cli" % get.workDIR())
    
    pisitools.dobin("build/docker*")

    shelltools.cd("%s" % get.workDIR())
    pisitools.dobin("moby-docker/bundles/dynbinary-daemon/*")
       
    # insert udev rules
    # pisitools.insinto("/lib/udev/rules.d", "moby-docker/contrib/udev/*.rules")

    #insert contrib in docs
    pisitools.insinto("/usr/share/doc/docker", "cli/contrib")
    
    pisitools.dobin("moby-docker/contrib/check-config.sh")

    shelltools.cd("%s/cli" % get.workDIR())
    pisitools.dodoc("VERSION", "README.md","CONTRIBUTING.md")
