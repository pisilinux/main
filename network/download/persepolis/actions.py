#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools



def setup():
    mesontools.configure()


def build():
    mesontools.build()

def check():
    pass
    #pythonmodules.run("setup.py test", pyVer="3")
    #pythonmodules.run("test/run_all_unittests.py",pyVer="3")
    #pythonmodules.run("test/run_examples_test.py",pyVer="3")

def install():
    mesontools.install()

    pisitools.dodoc("LICENSE", "README*")
