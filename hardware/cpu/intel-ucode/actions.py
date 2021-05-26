#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

def install():
    pisitools.insinto("/lib/firmware/intel-ucode", "Intel-Linux-Processor-Microcode-Data-Files-microcode-" + get.srcVERSION() + "/intel-ucode/*")
    pisitools.dodir("usr/lib/dracut/dracut.conf.d")
    os.system("echo 'early_microcode=yes' >> " + get.installDIR() + "/usr/lib/dracut/dracut.conf.d/intel_ucode.conf")
