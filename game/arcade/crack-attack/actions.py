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
    shelltools.system("rpm2targz crack-attack-1.1.14-40.fc30.x86_64.rpm")
    shelltools.system("mkdir sound")
    shelltools.system("tar xvf crack-attack-1.1.14-40.fc30.x86_64.tar.gz -C sound")
	
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-sound \
                         --disable-binreloc \
                         --enable-gtk")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/lib/libenet.a")
    pisitools.removeDir("/usr/include/")
    pisitools.removeDir("/usr/lib")
    
    pisitools.insinto("/usr/share/crack-attack/sounds", "sound/usr/share/crack-attack/sounds/*")
    pisitools.insinto("/usr/share/crack-attack/music", "sound/usr/share/crack-attack/music/*")
    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "COPYING", "COPYRIGHT", "NEWS")
