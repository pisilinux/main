
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
                        --sysconfdir=/etc \
                        --enable-debug=no \
                        --enable-xrandr \
                        --enable-xinerama \
                        --enable-xft \
                        --enable-alsa \
                        --enable-oss \
                        --enable-sndfile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
