#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
