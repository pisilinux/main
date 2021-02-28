#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr ")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.remove("/usr/sbin/fsck.exfat")
    pisitools.remove("/usr/sbin/mkfs.exfat")

    pisitools.dodoc("ChangeLog", "COPYING", "README")
