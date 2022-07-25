#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools, get, pisitools, shelltools

def setup():
    shelltools.system("./autogen.sh -V")
    #autotools.autoreconf("-fi")
    autotools.configure("--with-gtk=3\
                         --disable-static \
                         --enable-introspection")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
