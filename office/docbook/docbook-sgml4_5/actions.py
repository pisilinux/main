#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="."

def install():
    shelltools.system("sed -i -e '/ISO 8879/d' \
                                        -e '/gml/d' docbook.cat")

    pisitools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "*.dcl")
    pisitools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "*.dtd")
    pisitools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "*.mod")
    pisitools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "docbook.cat", "catalog")

    pisitools.dodoc("README")
