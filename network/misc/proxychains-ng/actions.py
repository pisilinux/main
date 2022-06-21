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
    #shelltools.makedirs("proxychains-ng-4.16")
    autotools.configure("--prefix=/usr --sysconfdir=/etc")

def build():
    #shelltools.makedirs("proxychains-ng-4.16")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.system("ln -s /usr/bin/proxychains4 proxychains")

    pisitools.dodoc("COPYING", "README")
