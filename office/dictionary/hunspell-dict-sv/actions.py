#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def setup():
    shelltools.system("unzip -o ooo_swedish_dict_2-36.oxt")

def install():
    pisitools.insinto("/usr/share/hunspell", "dictionaries/*.dic")
    pisitools.insinto("/usr/share/hunspell", "dictionaries/*.aff")

    pisitools.dodoc("LICENSE*")
