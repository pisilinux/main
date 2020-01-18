#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("./bootstrap")
    
    #suppress g++ warnings
    pisitools.cxxflags.add("-Wno-useless-cast -Wno-old-style-cast -Wno-deprecated-declarations\
							-Wno-effc++ -Wno-abi")
    #suppress gcc warnings
    pisitools.cflags.add("-fno-stack-protector -Wno-suggest-attribute=malloc")
    autotools.configure("--disable-static \
                         --with-zemberek \
                         --with-aspell \
                         --with-myspell \
                         --with-myspell-dir=/usr/share/hunspell")

    #fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.rename("/usr/share/enchant/enchant.ordering", "enchant.ordering-2")
    
    pisitools.dodoc("AUTHORS", "NEWS", "README", "HACKING")