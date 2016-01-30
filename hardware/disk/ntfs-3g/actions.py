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
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    autotools.configure("--prefix=/usr \
                        --sbin=/usr/bin \
                        --mandir=/usr/share/man \
                        --disable-ldconfig \
                        --disable-static \
                        --with-fuse=external \
                        --enable-posix-acls \
                        --enable-extras")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s rootbindir=/usr/bin rootsbindir=/usr/bin rootlibdir=/usr/lib" % get.installDIR())
    
    pisitools.domove("/usr/bin/ntfs-3g.*", "/bin")

    # Create some compat symlinks
    pisitools.dosym("/usr/bin/ntfs-3g", "/sbin/mount.ntfs")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "CREDITS", "NEWS", "README")
    pisitools.dosym("/usr/share/doc/ntfs-3g", "/usr/share/doc/ntfsprogs")
