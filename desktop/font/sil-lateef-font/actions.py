#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools


def install():
    pisitools.insinto("/usr/share/fonts/sil-lateef", "LateefGR-Regular.ttf")

    pisitools.dodoc("OFL.txt", "OFL-FAQ.txt", "README.txt", "FONTLOG.txt")
    pisitools.insinto("/usr/share/sil-lateef/documentation", "./documentation/*.pdf")
    pisitools.insinto("/usr/share/sil-lateef/documentation", "./documentation/*.odt")
    pisitools.insinto("/usr/share/sil-lateef/documentation", "./documentation/*.txt")
    pisitools.insinto("/usr/share/sil-lateef/web", "./web/*.html")
    pisitools.insinto("/usr/share/sil-lateef/web", "./web/*.css")
    pisitools.insinto("/usr/share/sil-lateef/web", "./web/*.woff")
