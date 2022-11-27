#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

j = ''.join([
    ' --enable-xmltools',
    ' --disable-desktopfiles',
    ' --with-jpeg',
    ' --with-tiff '
    ])

def setup():
    autotools.aclocal("-I config")
    autotools.autoconf("-f")

    autotools.configure(j)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/mime/packages", "desktopfiles/djvulibre-mime.xml")

    for size in ["22", "32", "48", "64"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/mimetypes" %(size, size), "desktopfiles/prebuilt-hi%s-djvu.png" % size, "image-vnd.djvu.png")

    pisitools.dodoc("NEWS")
