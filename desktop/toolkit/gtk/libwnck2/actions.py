#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-Dbuildtype=release")

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    pisitools.remove("/usr/bin/wnck-urgency-monitor")
    pisitools.remove("/usr/bin/wnckprop")
    
    #pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "MAINTAINERS")
