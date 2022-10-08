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

import os

WorkDir = "qtbase-everywhere-src-%s" % get.srcVERSION().replace('_','-').replace('pre1', 'tp')

qtbase = qt6.prefix
absoluteWorkDir = "%s/%s" % (get.workDIR(), WorkDir)

#Temporary bindir to avoid qt5 conflicts
bindirQt6="/usr/lib/qt6/bin"

def setup():
    #shelltools.system("patch -Rp1 < qt6-base-nouveau-freeze.patch")
    
    checkdeletepath="%s/qtbase/src/3rdparty"  % absoluteWorkDir
    for dir in ('libjpeg', 'freetype', 'libpng', 'zlib', "xcb", "sqlite"):
        if os.path.exists(checkdeletepath+dir):
            shelltools.unlinkDir(checkdeletepath+dir)

    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    vars = {"PISILINUX_CC" :       get.CC() + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_CXX":       get.CXX() + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_CFLAGS":    filteredCFLAGS + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_LDFLAGS":   get.LDFLAGS() + (" -m32" if get.buildTYPE() == "emul32" else "")}

    for k, v in vars.items():
        pisitools.dosed("mkspecs/common/g++-base.conf", k, v)
        pisitools.dosed("mkspecs/common/g++-unix.conf", k, v)

    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)
    #check that dosed commands without releated patches
    pisitools.dosed("mkspecs/common/gcc-base-unix.conf", "\-Wl,\-rpath,")
    pisitools.dosed("mkspecs/common/gcc-base.conf", "\-O2", filteredCFLAGS)
    pisitools.dosed("mkspecs/common/gcc-base.conf", "^(QMAKE_LFLAGS\s+\+=)", r"\1 %s" % get.LDFLAGS())

    if not get.buildTYPE() == "emul32":
        #-no-pch makes build ccache-friendly
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
                    -DQT_FEATURE_journald=ON \
                    -DQT_FEATURE_system_zlib=ON \
                    -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON \
                    -DCMAKE_MESSAGE_LOG_LEVEL=STATUS \
                    -DQT_FEATURE_openssl_linked=ON" % (qt6.prefix, bindirQt6, qt6.headerdir, qt6.archdatadir, qt6.docdir, qt6.datadir, qt6.mkspecsdir, qt6.examplesdir)
                    #-G Ninja \
                    #-DQT_FEATURE_directfb=ON \
    else:
        pisitools.dosed("mkspecs/linux-g++-64/qmake.conf", "-m64", "-m32")
        shelltools.export("LDFLAGS", "-m32 %s" % get.LDFLAGS())
        options = "-no-pch -v -confirm-license -opensource -no-use-gold-linker\
                   -platform linux-g++-32 \
                   -xplatform linux-g++-32 \
                   -prefix /usr/lib32 \
                   -bindir /usr/lib32/qt6/bin \
                   -docdir /usr/share/doc/qt \
                   -headerdir /usr/lib32/qt6/include/qt6 \
                   -datadir /usr/share/qt6 \
                   -sysconfdir /etc/xdg \
                   -examplesdir /usr/share/doc/qt/examples \
                   -system-sqlite \
                   -openssl-linked \
                   -nomake examples \
                   -no-xcb \
                   -no-rpath \
                   -optimized-qmake \
                   -dbus-linked \
                   -system-harfbuzz \
                   -libdir /usr/lib32/ \
                   -archdatadir /usr/lib32/qt6/"

    qt6.configure(options)

def build():
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    qt6.make()

def install():
    if get.buildTYPE() == "emul32":
        qt6.install("INSTALL_ROOT=%s32" % get.installDIR())
        shelltools.move("%s32/usr/lib32" % get.installDIR(), "%s/usr" % get.installDIR())
        return

    pisitools.dodir(qt6.libdir)
    qt6.install()

    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt6/bin" % get.installDIR()):
        pisitools.dosym("/usr/lib/qt6/bin/%s" % bin, "/usr/bin/%s-qt6" % bin)

    mkspecPath = "%s/mkspecs" %  qt6.archdatadir

    pisitools.dodoc("LICENSES/*")
