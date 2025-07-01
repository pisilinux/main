#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","%s" % get.srcVERSION())

def build():
    shelltools.system("python3 -m build --wheel --no-isolation")
    shelltools.system("python3 setup.py build")
    # python3modules.compile()

def install():
    shelltools.system("python3 -m installer --destdir=%s dist/*.whl" % get.installDIR())
    # python3modules.install()

    pisitools.dodoc("LICENSE", "README.md")
