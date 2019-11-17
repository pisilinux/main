#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

NoStrip = "/"

WorkDir = "openarena-engine-source-0.8.8"

build_arch = "x86_64" if get.ARCH() == "x86_64" else "i386"

builddir = "build/release-linux-%s" % build_arch

docs = ["CHANGES", "COPYING", "CREDITS", "LINUXNOTES", "README", "WENEED"]
datadir = "/usr/share/openarena"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def build():
    autotools.make('DEFAULT_BASEDIR=/usr/share/openarena BUILD_SERVER=1 BUILD_CLIENT=1 BUILD_CLIENT_SMP=1')

def install():
    pisitools.insinto("/usr/bin", "%s/oa_ded.%s" % (builddir, build_arch), "openarena-server")
    pisitools.insinto("/usr/bin", "%s/openarena.%s" % (builddir, build_arch), "openarena")
    pisitools.insinto("/usr/bin", "%s/openarena-smp.%s" % (builddir, build_arch), "openarena-smp")

    shelltools.cd("openarena-0.8.8")
    for data in ("missionpack", "baseoa"):
        fixperms(data)
        pisitools.insinto(datadir, data)
        
    for doc in docs:
        pisitools.dodoc(doc)
