#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -Wformat" % get.CFLAGS())
    pisitools.ldflags.add("-Wl,--allow-multiple-definition")
    mesontools.configure("-D docs=true -D gstreamer=disabled")

def build():
    mesontools.build()

def install():
    mesontools.install()    
    pisitools.domove("/usr/share/doc/pipewire/*", "/usr/share/doc/pipewire-0.2/")
    pisitools.removeDir("/usr/share/doc/pipewire/")
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/etc")
    pisitools.dodoc("LICENSE", "NEWS", "README*")
