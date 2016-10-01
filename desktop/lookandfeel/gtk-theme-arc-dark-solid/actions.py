#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "arc-theme/arc-themes/Arc-Dark-Solid"
	
def install():
    pisitools.dodir ("/usr/share/themes/Arc-Dark-Solid")

    for subtheme in ["gtk-2.0", "gtk-3.0", "metacity-1", "xfwm4", "cinnamon", "gnome-shell", "unity"]:
        pisitools.insinto ("/usr/share/themes/Arc-Dark-Solid", subtheme)
        pisitools.insinto ("/usr/share/themes/Arc-Dark-Solid", "index.theme")

   # pisitools.dodoc ("LICENSE", "README")	
	

