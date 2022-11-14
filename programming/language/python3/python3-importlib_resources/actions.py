#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules as py3, shelltools, get

shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION", "5.10.0")

def build():
    py3.run("-m build", pyVer = '3')

def install():
    py3.run("-m installer -d %s dist/importlib_resources-5.10.0-py3-none-any.whl" % get.installDIR(), pyVer = '3')
