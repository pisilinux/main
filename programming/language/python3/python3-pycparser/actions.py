#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    pythonmodules.compile(pyVer="3")

    shelltools.cd("pycparser")
    pythonmodules.run("_build_tables.py", pyVer="3")

    shelltools.cd("..")
    
def check():
    pythonmodules.run("tests/test_util.py", pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

    for dirs in ["examples"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)
