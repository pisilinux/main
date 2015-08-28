#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.cd("libraries/liblmdb")
    autotools.make("prefix=/usr")

def install():
    shelltools.cd("libraries/liblmdb")
    
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/man/man1")
    pisitools.dodir("/usr/share")
    pisitools.dodir("/usr/include")
    
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())
    
    pisitools.domove("/usr/man", "/usr/share")
    pisitools.dodoc("LICENSE", "CHANGES", "COPYRIGHT")
