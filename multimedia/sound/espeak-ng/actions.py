#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sh ./autogen.sh")
    autotools.configure("--includedir=/usr/include \
                         --with-extdict-{ru,zh,zhy}")

def build():
    autotools.make("src/espeak-ng src/speak-ng")
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.rename("/usr/bin/speak", "speak-ng")
    pisitools.rename("/usr/bin/espeak", "espeak-ng")
    pisitools.removeDir("/usr/include/espeak")

    pisitools.dodoc("AUTHORS", "CHANGELOG*", "COPYING*", "NEWS", "README")
