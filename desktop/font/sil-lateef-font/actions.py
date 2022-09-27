#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def install():
    shelltools.chmod("*.ttf", 0644)
    pisitools.insinto("/usr/share/fonts/sil-lateef", "*.ttf")

    pisitools.dodoc("OFL.txt", "OFL-FAQ.txt", "README.txt", "FONTLOG.txt")
    pisitools.insinto("/usr/share/sil-lateef/documentation","./documentation/pdf/*.pdf")
    pisitools.insinto("/usr/share/sil-lateef/documentation","./documentation/DOCUMENTATION.txt")
    pisitools.insinto("/usr/share/sil-lateef/web","./web/*.html")
    pisitools.insinto("/usr/share/sil-lateef/web","./web/*.css")
    pisitools.insinto("/usr/share/sil-lateef/web","./web/*.woff")
    pisitools.insinto("/usr/share/sil-lateef/web","./web/*.woff2")
    
