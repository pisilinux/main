#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Fixup version
    shelltools.echo(".version", get.srcVERSION().split("_")[0])

    # Disable emacs scripts
    shelltools.export("EMACS", "no")
    shelltools.move("autoconf.texi", "autoconf213.texi")
    autotools.configure("--infodir=/usr/share/info --program-suffix=-2.13")

def build():
    autotools.make()



def install():
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/info","autoconf213.info")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README")
