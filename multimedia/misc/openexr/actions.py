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
    pisitools.flags.add("-pthread -I/usr/include/OpenEXR -I/usr/include/libdrm")
    pisitools.ldflags.add("-lImath -lHalf -lIex -lIexMath -lIlmThread -lpthread")
    
    shelltools.cd("OpenEXR")
    shelltools.system("./bootstrap")
    autotools.configure("--enable-shared \
                         --disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.cd("OpenEXR")
    autotools.make()

def install():
    shelltools.cd("OpenEXR")
    # documents and examples go to "/usr/share/OpenEXR" without these parameters
    docdir = "/usr/share/doc/%s" % get.srcNAME()
    examplesdir = "%s/examples" % docdir
    autotools.rawInstall("DESTDIR=%s docdir=%s examplesdir=%s" % (get.installDIR(), docdir, examplesdir))
    
    shelltools.cd("..")
    pisitools.dodoc("README*","LICENSE*")
