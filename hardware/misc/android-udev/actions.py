#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="android-udev-rules-%s" % get.srcVERSION()
ver = get.srcVERSION()

def install():
    shelltools.cd("%s/android-udev-rules-%s" %(get.workDIR(), ver))
    shelltools.chmod("51-android.rules", 0644)
    shelltools.chmod("android-udev.conf", 0644)
    pisitools.insinto("/usr/lib/udev/rules.d/51-android.rules", "51-android.rules")
    pisitools.insinto("/usr/lib/sysusers.d/android-udev.conf", "android-udev.conf")

    pisitools.dodoc("LICENSE")
