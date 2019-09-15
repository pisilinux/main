#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
     autotools.configure("--disable-fd-passing \
                          --disable-static \
                          --disable-gpg-test \
                          --disable-gpgsm-test \
                          --enable-languages=cpp,qt,python")
     
     pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.insinto("/usr/lib/cmake/Qgpgme", "lang/qt/src/QGpgmeConfig.cmake")
    pisitools.insinto("/usr/lib/cmake/Qgpgme", "lang/qt/src/QGpgmeConfigVersion.cmake")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
