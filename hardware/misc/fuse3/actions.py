#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-Dexamples=false")

def build():
    mesontools.build()

def install():
    mesontools.install()
        
    pisitools.removeDir("/dev")
    pisitools.removeDir("/etc")
    
    # Make compat symlinks into /usr/bin
    pisitools.dosym("/usr/bin/fusermount3", "/bin/fusermount3")
    pisitools.dosym("/usr/sbin/mount.fuse3", "/sbin/mount.fuse3")
    
    pisitools.dosym("/usr/lib/libfuse3.so", "/lib/libfuse3.so")
    pisitools.dosym("/usr/lib/libfuse3.so", "/lib/libfuse3.so.3")
    pisitools.dosym("/usr/lib/libfuse3.so", "/lib/libfuse3.so.3.12.0")
    
    # Move pkgconfig file to /usr/lib
    #pisitools.domove("/lib/pkgconfig", "/usr/lib/")
    
    pisitools.dodoc("AUTHORS", "ChangeLog*", "README*")
