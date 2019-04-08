#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./bootstrap")
    autotools.configure("--disable-static \
                         --with-zemberek \
                         --with-aspell \
                         --with-myspell \
                         --with-myspell-dir=/usr/share/hunspell")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.rename("/usr/share/enchant/enchant.ordering", "enchant.ordering-2")
    
    pisitools.dodoc("AUTHORS", "NEWS", "README", "HACKING")
