#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def build():
    autotools.make("prefix=/usr")

    # remove bundled packages, use our system libraries
    shelltools.system("rm -rf thirdparty/{curl,freeglut,freetype,harfbuzz,jpeg,lcms2,libjpeg,openjpeg,zlib}")

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("README", "COPYING")
