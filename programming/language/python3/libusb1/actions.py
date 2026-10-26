#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def build():
    python3modules.compile()

def check():
    pass
    #python3modules.run("setup.py test", )
    #python3modules.run("test/run_all_unittests.py",)
    #python3modules.run("test/run_examples_test.py",)

def install():
    python3modules.install()

    pisitools.dodoc("COPYING*", "README*")
