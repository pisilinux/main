#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("XDG_DATA_HOME", get.workDIR())
#pisitools.flags.replace("-ggdb3", "-g")

cflags = get.CFLAGS().replace("-ggdb3","")
cxxflags = get.CXXFLAGS().replace("-gddb3", "")

paths = ["JavaScriptCore", "WebCore", "WebKit"]
docs = ["AUTHORS", "ChangeLog", "COPYING.LIB", "THANKS", \
        "LICENSE-LGPL-2", "LICENSE-LGPL-2.1", "LICENSE"]

def setup():
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cxxflags)
    autotools.configure("\
                        --libexecdir=/usr/lib/WebKitGTK \
                        --disable-static \
                        --disable-webkit2 \
                        --disable-gtk-doc \
                        --disable-silent-rules \
                        --disable-wayland-target \
                        --enable-geolocation \
                        --enable-glx \
                        --enable-webgl \
                        --with-gnu-ld \
                        --with-gstreamer=1.0 \
                        --with-gtk=2.0 \
                        --enable-x11-target \
                        --enable-video \
                        --enable-web-audio \
                        --enable-introspection \
                        ")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cxxflags)
    autotools.make("-j1 all stamp-po")

def install():
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cxxflags)
    autotools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/share/gtk-doc/html", "/usr/share/doc/webkit-gtk2")

    pisitools.dodoc("NEWS")
    shelltools.cd("Source")
    for path in paths:
        for doc in docs:
            if shelltools.isFile("%s/%s" % (path, doc)):
                pisitools.insinto("%s/%s/%s" % (get.docDIR(), get.srcNAME(), path),
                                  "%s/%s" % (path, doc))
