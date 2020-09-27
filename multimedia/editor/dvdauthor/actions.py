#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

#from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "dvdauthor"

def setup():
    # disable ImageMagick, use GraphicsMagick
    #shelltools.export("MAGICKCONFIG", "/bin/true")
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-rpath \
                         --with-graphicsmagick \
                         --enable-default-video-format=NTSC")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
