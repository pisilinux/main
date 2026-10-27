#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules, pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","%s" % get.srcVERSION())

def build():
    # shelltools.system("rm -f .git_archival.txt")
    shelltools.cd("vcs-versioning")
    python3modules.compile()
    # shelltools.system("python3 ./setup.py build")

def install():
    shelltools.cd("vcs-versioning")
    python3modules.install()
    # shelltools.system("python3 -m installer --destdir='%s' dist/*.whl" % get.installDIR())
    # pythonmodules.install(pyVer = "3")

    pisitools.dodoc("README.md")
