#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
	cmaketools.configure("-B build-qt5 \
						  -DUSE_QT6=OFF \
						  -DCMAKE_INSTALL_PREFIX=/usr \
						  -DCMAKE_INSTALL_LIBDIR=lib")

	cmaketools.configure("-B build-qt6 \
						  -DUSE_QT6=ON \
						  -DCMAKE_INSTALL_PREFIX=/usr \
						  -DCMAKE_INSTALL_LIBDIR=lib")

def build():
	cmaketools.make("-C build-qt5")
	cmaketools.make("-C build-qt6")

def install():
	cmaketools.install("-C build-qt5")
	cmaketools.install("-C build-qt6")

	pisitools.dodoc("AUTHORS", "COPYING", "README.md")

