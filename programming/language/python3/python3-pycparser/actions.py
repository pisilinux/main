#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    python3modules.compile(pyVer="3")

    # shelltools.cd("pycparser")
    # python3modules.run("_build_tables.py", pyVer="3")

    # shelltools.cd("..")
    
def check():
    python3modules.run("tests/test_util.py", pyVer="3")

def install():
    python3modules.install(pyVer="3")

    for dirs in ["examples"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)
