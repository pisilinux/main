#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DSUPPORT_JAVA_PROGRAMS=OFF',
    ' -DUSE_SPARSE_LEVMAR=OFF',
    ' -B_build -L '
    ])

def setup():
    cmaketools.configure(j)

def build():
    cmaketools.make("-C _build")

def install():
    cmaketools.install("-C _build")
