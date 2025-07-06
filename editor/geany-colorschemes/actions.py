#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/geany/colorschemes", "colorschemes/*")

    pisitools.dodoc("AUTHORS")
