#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS","%s -fpie -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
shelltools.export("LDFLAGS","%s -pie" % get.LDFLAGS())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-mountconfig \
                         --enable-ipv6 \
                         --enable-nfsv3 \
                         --enable-nfsv4 \
                         --enable-gss \
                         --with-krb5=/usr \
                         --with-statedir=/var/lib/nfs")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/nfs/statd/sm")
    pisitools.dodir("/var/lib/nfs/statd/sm.bak")
    pisitools.dodir("/var/lib/nfs/v4recovery")
    pisitools.dodir("/var/lib/nfs/rpc_pipefs")
    # remove conflict man file with nfs-utils
    pisitools.remove("/usr/lib/pkgconfig/libnfsidmap.pc")
    pisitools.remove("/usr/include/nfsidmap_plugin.h")
    pisitools.remove("/usr/include/nfsidmap.h")
    pisitools.remove("/usr/share/man/man5/idmapd.conf.5")
    pisitools.removeDir("/usr/lib/pkgconfig")
    pisitools.removeDir("/usr/include")

    pisitools.insinto("/etc", "utils/mount/nfsmount.conf")

    pisitools.domove("/usr/sbin/rpc.statd", "/sbin/")
    pisitools.dodoc("README", "COPYING")
