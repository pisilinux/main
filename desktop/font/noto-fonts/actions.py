#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools


def install():
    pisitools.insinto("/usr/share/fonts/noto", "hinted/Noto*.ttf")
    #pisitools.insinto("/usr/share/fonts/noto", "hinted/Noto*.ttc")

    #for noto-fonts-ttf-croscore
    pisitools.insinto("/usr/share/fonts/TTF", "hinted/Arimo*.ttf")
    pisitools.insinto("/usr/share/fonts/TTF", "hinted/Tinos*.ttf")
    pisitools.insinto("/usr/share/fonts/TTF", "hinted/Cousine*.ttf")
    
    pisitools.dosym("/etc/fonts/conf.avail/66-noto-sans.conf", "/etc/fonts/conf.d/66-noto-sans.conf")
    pisitools.dosym("/etc/fonts/conf.avail/66-noto-serif.conf", "/etc/fonts/conf.d/66-noto-serif.conf")
    pisitools.dosym("/etc/fonts/conf.avail/66-noto-mono.conf", "/etc/fonts/conf.d/66-noto-mono.conf")

    pisitools.dodoc("LICENSE", "README.md")
