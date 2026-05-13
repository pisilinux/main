#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-Dudevrulesdir=/usr/lib/udev/rules.d", sourceDir="..")

def build():
    cmaketools.make("-C build")
    # cmaketools.make("-C build doc")

def install():
    pisitools.dodoc("LICENSE", "README*", "./doc/*")

    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
