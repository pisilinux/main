#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#def setup():
    #autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr", "usr/*")
    shelltools.chmod(get.installDIR() + "/usr/lib/*")
    shelltools.chmod(get.installDIR() + "/usr/bin/*")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*")
