#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import qt6
from pisi.actionsapi import get

bindirQt6="/usr/lib/qt6/bin"

def setup():
    options = " -DCMAKE_INSTALL_PREFIX=%s \
                    -DCMAKE_BUILD_TYPE=Release \
                    -DINSTALL_BINDIR=%s \
                    -DINSTALL_INCLUDEDIR=%s \
                    -DINSTALL_ARCHDATADIR=%s \
                    -DINSTALL_DOCDIR=%s \
                    -DINSTALL_DATADIR=%s \
                    -DINSTALL_MKSPECSDIR=%s \
                    -DINSTALL_EXAMPLESDIR=%s \
                    -DQT_FEATURE_libproxy=ON \
                    -DQT_FEATURE_vulkan=ON \
                    -DQT_FEATURE_system_freetype=ON \
                    -DQT_FEATURE_system_harfbuzz=ON \
                    -DQT_FEATURE_system_sqlite=ON \
                    -DQT_FEATURE_dbus_linked=ON \
                    -DQT_FEATURE_openssl_linked=ON" % (qt6.prefix, bindirQt6, qt6.headerdir, qt6.archdatadir, qt6.docdir, qt6.datadir, qt6.mkspecsdir, qt6.examplesdir)
    
    cmaketools.configure(options)

def build():
    qt6.make()
    #qt6.make("docs")

def install():
    qt6.install("INSTALL_ROOT=%s" % get.installDIR())

    #I hope qtchooser will manage this issue
    #for bin in shelltools.ls("%s/usr/lib/qt6/bin" % get.installDIR()):
        #pisitools.dosym("/usr/lib/qt6/bin/%s" % bin, "/usr/bin/%s-qt6" % bin)

    pisitools.dodoc("LICENSE*")
