#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools, autotools, get

def build():
    shelltools.export("PYTHON", "/usr/bin/python3")
    pythonmodules.run("-m build --wheel --skip-dependency-check --no-isolation", pyVer="3")

def install():
    pythonmodules.run("-m installer  --destdir='%s'  dist/*.whl" % get.installDIR(), pyVer="3")
