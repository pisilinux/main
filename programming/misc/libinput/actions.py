#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("export LANG=en_US.UTF-8")
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("meson .. --prefix=/usr \
                                -Dtests=false \
                                -Dudev-dir=/lib/udev \
                                -Ddocumentation=false")
    

def build():
    shelltools.cd("build")
    shelltools.system("ninja")
    
#def build():
  #  autotools.make("check")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    pisitools.dosym("libinput.so.10","/usr/lib/libinput.so.0")
    
    #pisitools.remove("/usr/lib/udev/rules.d/80-libinput-device-groups.rules")
    #pisitools.remove("/usr/lib/udev/rules.d/90-libinput-model-quirks.rules")
    shelltools.cd("..")
    pisitools.dodoc("COPYING", "README*")
