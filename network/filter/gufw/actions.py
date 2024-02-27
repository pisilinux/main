#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pythonmodules, pisitools, shelltools


def build():
    pythonmodules.compile(pyVer="3")
    shelltools.system("python3 setup.py build")


def check():
    pass
    #pythonmodules.run("setup.py test", pyVer="3")
    #pythonmodules.run("test/run_all_unittests.py",pyVer="3")
    #pythonmodules.run("test/run_examples_test.py",pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    pisitools.dosed("%s/usr/bin/gufw-pkexec" % get.installDIR(), "/usr/share/gufw/gufw/gufw.py","/usr/lib/python3.*/site-packages/gufw/gufw.py")

    pisitools.dodoc("COPYING*", "README*")
