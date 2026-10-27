#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import python3modules, cmaketools

j = ''.join([
    ' -DPYBIND11_FINDPYTHON=ON',
    ' -DUSE_PYTHON_INCLUDE_DIR=OFF',
    ' -B_build -L '
    ])

def setup():
    cmaketools.configure(j)

def build():
    cmaketools.make("-C _build")
    python3modules.compile()

def install():
    cmaketools.install("-C _build")
    python3modules.install()
