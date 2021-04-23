#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--prefix=/usr  \
            --enable-gles2 \
            --enable-{kms,wayland,xlib}-egl-platform \
            --enable-wayland-egl-server")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s INSTALL="install -p -c"' % get.installDIR())

