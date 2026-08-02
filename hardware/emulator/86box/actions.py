#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

build_dir = "_build"

flags = " ".join([
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_TOOLCHAIN_FILE=cmake/flags-gcc-x86_64.cmake",
    "-DRELEASE=on",
    "-DUSE_QT6=on",
    "-DSLIRP_EXTERNAL=on",
    "-DRTMIDI=off",
    "-DDISCORD=off",
])

def setup():
    cmaketools.configure("-S . -B %s %s" % (build_dir, flags))

def build():
    cmaketools.make("-C %s" % build_dir)

def install():
    cmaketools.install("-C %s" % build_dir)

    pisitools.insinto("/usr/share/applications", "src/unix/assets/net.86box.86Box.desktop")

    for size in ("16", "20", "24", "32", "40", "48", "64", "72", "128", "256"):
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (size, size),
                          "src/unix/assets/%sx%s/net.86box.86Box.png" % (size, size))

    pisitools.dodoc("COPYING", "README.md")
