#!/usr/bin/python
# -*- actions.pycoding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-B build \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DENABLE_DYNAMIC_LINKING=ON \
                            -DBUILD_LIB_STATIC=OFF \
                            -DENABLE_OPENCV=ON")


def build():
    cmaketools.make("-C build")


    cmaketools.rawInstall("-C build DESTDIR=%s/tmp-install" % get.curDIR())

    shelltools.cd("gmic-qt")
    cmaketools.configure("-B build-qt \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DENABLE_DYNAMIC_LINKING=ON \
                            -DBUILD_WITH_QT6=ON \
                            -DCMAKE_PREFIX_PATH=%s/gmic-4.0.2/tmp-install/usr \
                            -DGMIC_QT_HOST=none" % get.workDIR())
    shelltools.cd("build-qt")
    cmaketools.make()

    shelltools.cd("..")
    cmaketools.configure("cmake -B build-gimp \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DENABLE_DYNAMIC_LINKING=ON \
                            -DBUILD_WITH_QT6=ON \
                            -DCMAKE_PREFIX_PATH=%s/gmic-4.0.2/tmp-install/usr \
                            -DGMIC_QT_HOST=gimp3" % get.workDIR())
    cmaketools.make("-C build-gimp")


def install():
    cmaketools.rawInstall("-C build DESTDIR=%s" % get.installDIR())
    cmaketools.rawInstall("-C gmic-qt/build-qt DESTDIR=%s" % get.installDIR())
    cmaketools.rawInstall("-C gmic-qt/build-gimp DESTDIR=%s" % get.installDIR())

    for size in (16, 32, 48, 64):
        pisitools.insinto("/usr/share/icons/hicolor/%dx%d/apps" % (size, size),
                         "gmic-qt/icons/application/%d-gmic_qt.png" % size,
                         "gmic_qt.png")

    pisitools.insinto("/usr/share/icons/hicolor/scalable/apps",
                     "gmic-qt/icons/application/gmic_qt.svg")
    pisitools.insinto("/usr/share/applications",
                     "gmic-qt/gmic_qt.desktop")

    pisitools.doman("man/gmic.1.gz")
    pisitools.dodoc("COPYING", "README")
    pisitools.insinto("/usr/share/doc/gimp-gmic-plugin", "COPYING")
    pisitools.insinto("/etc/bash_completion.d/", "resources/gmic_bashcompletion.sh", destinationFile = "gmic")
    # shelltools.cd("gmic-qt")
    #pisitools.dobin("gmic")
    # pisitools.doexe("gmic_gimp_qt", "/usr/lib/gimp/2.0/plug-ins/")
    #pisitools.insinto("/usr/lib/gimp/2.0/plug-ins/", "gmic_gimp_qt", "gmic_gimp")
    pisitools.dosym("/usr/lib/gimp/3.0/plug-ins/gmic_gimp_qt/gmic_gimp_qt", "/usr/lib/gimp/3.0/plug-ins/gmic_gimp_qt/gmic_gimp")
    
    # shelltools.cd("..")
    shelltools.cd("src")
    pisitools.insinto("/usr/include", "gmic.h")
    # pisitools.dolib("libgmic.so")
    ver = ".%s" % get.srcVERSION()
    while ver:
        pisitools.dosym("libgmic.so", "/usr/lib/libgmic.so%s" % ver)
        ver = ver[:ver.rfind('.')]
