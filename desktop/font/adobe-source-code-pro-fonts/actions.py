#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/fonts/adobe-source-code-pro-fonts/", "OTF/*.otf")
    pisitools.insinto("/usr/share/fonts/adobe-source-code-pro-fonts/", "VAR/*.otf")

    pisitools.dodoc("LICENSE.md", "README.md")
