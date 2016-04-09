#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()
    
#def build():
  #  autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("libinput.so.5.0.0","/usr/lib/libinput.so.0")
    
    #pisitools.remove("/usr/lib/udev/rules.d/80-libinput-device-groups.rules")
    #pisitools.remove("/usr/lib/udev/rules.d/90-libinput-model-quirks.rules")
    pisitools.dodoc("COPYING", "README")
