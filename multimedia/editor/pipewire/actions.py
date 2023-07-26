#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -Wformat" % get.CFLAGS())
    mesontools.configure("-Dman=disabled \
                          -Dgstreamer=enabled \
                          -Ddocs=enabled \
                          -Dsystemd=disabled \
                          -Dbluez5=enabled \
                          -Dffmpeg=enabled \
                          -Dpipewire-alsa=enabled \
                          -D compress-offload=disabled \
                          -Djack=disabled \
                          -Dsession-managers=enabled \
                          -Dlibcamera=disabled")

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    # Use alsa-card-profiles built with Pulseaudio
    pisitools.removeDir("/usr/share/alsa-card-profile")
    
    pisitools.dosym("/usr/share/alsa/alsa.conf.d/50-pipewire.conf", "/etc/alsa/conf.d/50-pipewire.conf")

    #tg_owt
    pisitools.dosym("/usr/include/pipewire-0.3/pipewire", "/usr/include/pipewire")
    pisitools.dosym("/usr/include/spa-0.2/spa", "/usr/include/spa")

    #shelltools.cd("..")
    pisitools.dodoc("LICENSE", "COPYING", "NEWS", "README*")
