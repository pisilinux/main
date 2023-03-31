#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

verMAJOR = "0"
verMINOR = "0"
staticlibfile = "/usr/lib/libx264.a"

pisitools.cflags.sub("-O[\ds]", "-O3")

def getMinorVersion():
    f = file("x264.h").read()
    for i in f.split("\n"):
        if i.startswith("#define X264_BUILD"):
            return i.split()[-1]

    return "0"

def setup():
    shelltools.export("CFLAGS", "%s -O3" % get.CFLAGS())

    # force using shared gpac
    pisitools.dosed("configure", "-lgpac_static", "-lgpac")

    # these disables are here to prevent circular deps, especially with ffmpeg
    # Not delete --bit-depth=8 \
    autotools.rawConfigure("--prefix=/usr \
                            --enable-pic \
                            --disable-asm \
                            --enable-shared \
                            --disable-avs \
                            --disable-ffms \
                            --disable-lavf \
                            --disable-swscale \
                            --bit-depth=10 \
                            --bit-depth=8 \
                           ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #autotools.install()

    # verMINOR = getMinorVersion()
    # pisitools.dosym("libx264.so.%s.%s" % (verMAJOR, verMINOR), "/usr/lib/libx264.so.%s" % verMAJOR)

    # No static libs
    if shelltools.isFile("%s/%s" % (get.installDIR(), staticlibfile)):
        pisitools.remove(staticlibfile)

