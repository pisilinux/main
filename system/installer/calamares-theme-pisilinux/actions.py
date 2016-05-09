#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    pisitools.dodir("/usr/share/calamares/branding/pisilinux")
    pisitools.insinto("/usr/share/calamares/branding/pisilinux", "branding/pisi-kde/*")
