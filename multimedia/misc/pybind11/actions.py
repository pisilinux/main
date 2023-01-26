#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules, cmaketools

j = ''.join([
    ' -DPYBIND11_FINDPYTHON=ON',
    ' -DUSE_PYTHON_INCLUDE_DIR=OFF',
    ' -B_build -L '
    ])

def setup():
    cmaketools.configure(j)

def build():
    cmaketools.make("-C _build")
    pythonmodules.compile(pyVer = "3")

def install():
    cmaketools.install("-C _build")
    pythonmodules.install(pyVer = "3")
