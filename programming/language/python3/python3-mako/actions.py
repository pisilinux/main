#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import python3modules

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

WorkDir = "mako-%s" % get.srcVERSION()

def build():
    python3modules.compile()

def install():
    # shelltools.system('sed -i "s:mako-render:&3:g" setup.py')
    python3modules.install()

    #pisitools.dodoc("doc/*.txt")
    pisitools.dohtml("doc/*.html")
    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "doc/build")
    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "examples")
