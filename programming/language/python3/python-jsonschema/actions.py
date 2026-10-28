#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","%s" % get.srcVERSION())

def build():
    python3modules.compile(pyVer="3")
    # shelltools.system("python3 setup.py build")

def check():
    pass
    #python3modules.run("setup.py test", pyVer="3")
    #python3modules.run("test/run_all_unittests.py",pyVer="3")
    #python3modules.run("test/run_examples_test.py",pyVer="3")

def install():
    python3modules.install(pyVer="3")

    pisitools.dodoc("COPYING", "README*")
