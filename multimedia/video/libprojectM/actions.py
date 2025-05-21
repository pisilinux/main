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

    cmaketools.configure(sourceDir="..")

def build():
    cmaketools.make("-C build")

def install():
    pisitools.dodoc("README*", "COPYING", "LICENSE*")

    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
