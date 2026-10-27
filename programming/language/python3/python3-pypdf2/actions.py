#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import python3modules

def build():
    shelltools.system("sed -i 's/,<4//' pyproject.toml")
    python3modules.compile()
    
#def check():
#    python3modules.run("-m unittest Tests.tests", )

def install():
    python3modules.install()

    # for dirs in ["PDF_Samples", "Sample_Code"]:
        # pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)
