# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.copytree("../wxWidgets-%s" % (get.srcVERSION().replace("_", "~")), "../wxWidgets-%s-gtk3" % get.srcVERSION())
    
    pisitools.flags.add("-fno-strict-aliasing")

    autotools.configure("--enable-shared \
                         --disable-optimise \
                         --disable-debug \
                         --disable-rpath \
                         --enable-intl \
                         --enable-geometry \
                         --enable-timer \
                         --enable-unicode \
                         --enable-sound \
                         --enable-mediactrl \
                         --enable-xrc \
                         --enable-graphics_ctx \
                         --enable-display \
                         --enable-joystick \
                         --disable-gtktest \
                         --disable-sdltest \
                         --disable-precomp-headers \
                         --with-gtk=2 \
                         --with-libpng=sys \
                         --with-libjpeg=sys \
                         --with-libtiff=sys \
                         --with-libxpm=sys \
                         --with-sdl \
                         --without-gnomevfs \
                         --with-opengl \
                         --with-regex=builtin \
                         --with-zlib=sys \
                         --with-expat=sys")
    
    #shelltools.cd("%s" % get.workDIR())
    shelltools.cd("../wxWidgets-%s-gtk3" % get.srcVERSION())
    
    pisitools.flags.add("-fno-strict-aliasing")
    autotools.configure("--enable-shared \
                         --disable-optimise \
                         --disable-debug \
                         --disable-rpath \
                         --enable-intl \
                         --enable-geometry \
                         --enable-timer \
                         --enable-unicode \
                         --enable-sound \
                         --enable-mediactrl \
                         --enable-xrc \
                         --enable-graphics_ctx \
                         --enable-display \
                         --enable-joystick \
                         --disable-gtktest \
                         --disable-sdltest \
                         --disable-precomp-headers \
                         --with-gtk=3 \
                         --with-libpng=sys \
                         --with-libjpeg=sys \
                         --with-libtiff=sys \
                         --with-libxpm=sys \
                         --with-sdl \
                         --without-gnomevfs \
                         --with-opengl \
                         --with-regex=builtin \
                         --with-zlib=sys \
                         --with-expat=sys")
    

def build():
    autotools.make()
    autotools.make("-C locale allmo")
    
    shelltools.cd("../wxWidgets-%s-gtk3" % get.srcVERSION())
    autotools.make()

def install():
    shelltools.cd("../wxWidgets-%s-gtk3" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/bin/wx-config","wx-config-gtk3")
    
    shelltools.cd("../wxWidgets-%s" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #autotools.install()

    pisitools.insinto("/usr/share/pixmaps", "art/wxlogo.svg")

    pisitools.dodoc("docs/*.txt", "docs/*.htm")
    
    
