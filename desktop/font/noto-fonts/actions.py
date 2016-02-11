#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools


def install():
    pisitools.insinto("/usr/share/fonts/noto", "hinted/Noto*.ttf")
    
    #for noto-fonts-ttf-croscore
    pisitools.insinto("/usr/share/fonts/TTF", "hinted/Arimo*.ttf")
    pisitools.insinto("/usr/share/fonts/TTF", "hinted/Tinos*.ttf")
    pisitools.insinto("/usr/share/fonts/TTF", "hinted/Cousine*.ttf")

    pisitools.dodoc("LICENSE")