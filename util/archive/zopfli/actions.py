#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	cmaketools.configure("-DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_LIBDIR=lib")

def build():
	cmaketools.make()

def install():
	cmaketools.install()

	pisitools.dodoc("CONTRIBUTING.md", "COPYING", "README*")

