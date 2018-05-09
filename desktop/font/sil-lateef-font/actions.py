#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    pisitools.dobin("LateefGR-Regular.ttf", "/usr/share/fonts/sil-lateef")

    pisitools.dodoc("OFL.txt", "OFL-FAQ.txt", "README.txt", "FONTLOG.txt")
    pisitools.dobin("./documentation/*.pdf", "/usr/share/sil-lateef/documentation")
    pisitools.dobin("./documentation/*.odt", "/usr/share/sil-lateef/documentation")
    pisitools.dobin("./documentation/*.txt", "/usr/share/sil-lateef/documentation")
    pisitools.dobin("./web/*.html", "/usr/share/sil-lateef/web")
    pisitools.dobin("./web/*.css", "/usr/share/sil-lateef/web")
    pisitools.dobin("./web/*.woff", "/usr/share/sil-lateef/web")
    
