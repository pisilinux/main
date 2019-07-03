#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
	shelltools.system("sed -e 's|-Werror||' -i Makefile")
	
	autotools.make("RELEASE=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.makedirs("%s/usr/bin" %get.installDIR())
    shelltools.move("%s/usr/games/blobwars" %get.installDIR(), "%s/usr/bin/" %get.installDIR())
    pisitools.removeDir("/usr/games")
