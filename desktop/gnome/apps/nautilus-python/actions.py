#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools, pisitools, shelltools, get

def setup():
    shelltools.export("PYTHON","/usr/bin/python3")
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    shelltools.copytree("%s/usr/share/pkgconfig" % get.installDIR(), "%s/usr/lib/pkgconfig" % get.installDIR())
    pisitools.removeDir("/usr/share/pkgconfig")

    pisitools.dodoc("AUTHORS", "COPYING", "README*")
