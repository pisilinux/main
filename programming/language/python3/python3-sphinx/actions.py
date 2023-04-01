#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools, autotools, get

# WorkDir="Sphinx-%s" % get.srcVERSION()
# t = "dist/sphinx-5.3.0-py3-none-any.whl"
# shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION", "5.3.0")

def build():
    shelltools.export("PYTHON", "/usr/bin/python3")
    pythonmodules.run("-m build --wheel --skip-dependency-check --no-isolation", pyVer="3")

def install():
     # py3.run("-m installer -d %s " % get.installDIR(), pyVer = '3')
    # shelltools.system("python3 -m installer --wheel  DESTDIR=%s" % get.installDIR())
    pythonmodules.run("-m installer  --destdir='%s'  dist/*.whl" % get.installDIR(), pyVer="3")
