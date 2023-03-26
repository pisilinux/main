#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-D efi_sbat_distro_id='pisi' \
                          -D efi_sbat_distro_summary='Pisi Linux' \
                          -D efi_sbat_distro_pkgname='fwupd-efi' \
                          -D efi_sbat_distro_version=%s \
                          --libexecdir=/usr/lib \
                          -D efi_sbat_distro_url='https://github.com/pisilinux/main/issues'" % get.srcVERSION())

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    #shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "COPYING", "README*")
