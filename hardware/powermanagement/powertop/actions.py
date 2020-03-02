#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's:RUN-VERSION-SCRIPT-IN-GIT-REPOSITORY-ONLY:v2.11:' scripts/version")
    shelltools.system("./autogen.sh")
    
    autotools.configure()
    
       
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    pisitools.dodoc('COPYING', 'TODO', 'README')
