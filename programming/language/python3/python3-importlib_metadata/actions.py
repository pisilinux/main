#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules, shelltools, get

shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION", "5.0.0")

def build():
    pythonmodules.run("-m build", pyVer = '3')

def install():
    pythonmodules.run("-m installer -d %s dist/importlib_metadata-5.0.0-py3-none-any.whl" % get.installDIR(), pyVer = '3')
