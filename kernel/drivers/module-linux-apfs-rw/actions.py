#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

KDIR = kerneltools.getKernelVersion()

CONFIGS = "-DCONFIG_APFS_RW_ALWAYS"

def build():
    autotools.make("KERNEL_DIR=/lib/modules/%(kdir)s/build CONFIG=%(configs)s" % { 'kdir': KDIR, 'configs': CONFIGS })

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*.ko")
    pisitools.dodoc("LICENSE", "README*")
