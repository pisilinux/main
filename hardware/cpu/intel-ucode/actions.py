#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("rm -f intel-ucode{,-with-caveats}/list")
    shelltools.system("mkdir -p kernel/x86/microcode")
    shelltools.system("iucode_tool --write-earlyfw=intel-ucode.img intel-ucode{,-with-caveats}/")
    shelltools.chmod(get.curDIR() + "/intel-ucode.img", 0644)

def install():
    pisitools.insinto("/boot", "intel-ucode.img")