#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.cd("squashfs-tools")
    #Chakra features
    #reduce memory requirements of unsquashfs to support installation on systems with 256 MB RAM 
    cmd1='sed -i -e "s/BUFFER_DEFAULT [0-9]*/BUFFER_DEFAULT 32/" unsquashfs.h'
    cmd2="sed -i 's|^#XZ_SUPPORT = 1|XZ_SUPPORT = 1|' Makefile"
    cmd3="sed -i 's|^#LZO_SUPPORT = 1|LZO_SUPPORT = 1|' Makefile"
    cmd4="sed -i 's|^#LZ4_SUPPORT = 1|LZ4_SUPPORT = 1|' Makefile"
    cmd5="sed -i 's|^#XATTR_SUPPORT = 1|XATTR_SUPPORT = 1|' Makefile"
    cmd6="sed -i 's|^#ZSTD_SUPPORT = 1|ZSTD_SUPPORT = 1|' Makefile"
    cmd7="sed -i 's|^#LZMA_XZ_SUPPORT = 1|LZMA_XZ_SUPPORT = 1|' Makefile"
    cmd8="sed -i 's|^COMP_DEFAULT = gzip|COMP_DEFAULT = xz|' Makefile"
    cmds=[cmd1,cmd2,cmd3,cmd4,cmd5,cmd6,cmd7,cmd8]
        
    for cmd in cmds:
        shelltools.system(cmd)
    autotools.make('RPM_OPT_FLAGS="%s"' % get.CFLAGS())

def install():
    shelltools.cd("squashfs-tools")
    autotools.install("INSTALL_PREFIX='%s/usr' INSTALL_MANPAGES_DIR='%s/usr/share/man/man1' INSTALL_DIR='%s/usr/sbin'" % (get.installDIR(), get.installDIR(), get.installDIR()))
