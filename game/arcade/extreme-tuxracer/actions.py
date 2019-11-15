#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import zipfile

WorkDir = "etr-%s" %get.srcVERSION()

def myunzip(z):
    zfile = zipfile.ZipFile(z)
    zfile.extractall()
    zfile.close()

def setup():
    #myunzip("etracericons.zip")
    
    shelltools.system("sed -i -e '/^localedir/s:=.*:=@localedir@:' src/Makefile.in")

    autotools.configure("--disable-dependency-tracking \
                         --localedir=/usr/share/locale \
                         --disable-rpath \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #for i in ["16", "22", "32", "48"]:
        #pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps/" % (i,i), "etracericons/etracericon_%s.png" % i, "extreme-tuxracer.png")

    pisitools.insinto("/usr/share/pixmaps/", "resources/etr.svg", "extreme-tuxracer.svg")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
