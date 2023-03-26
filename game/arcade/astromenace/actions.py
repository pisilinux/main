#!/usr/bin/env python
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

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
      -DDATADIR=/usr/share/astromenace", sourceDir="..")

def build():
    cmaketools.make("-C build")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/astromenace", "/usr/bin")
    pisitools.domove("/usr/gamedata.vfs", "/usr/share/astromenace")
    pisitools.dosym("/usr/bin/astromenace", "/usr/bin/AstroMenace")

    # pisitools.dodoc("README.md", "LICENSE.md")


