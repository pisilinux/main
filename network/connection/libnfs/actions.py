#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-DCMAKE_BUILD_TYPE=release \
     -DCMAKE_INSTALL_PREFIX=/usr \
     -DENABLE_DOCUMENTATION=ON \
     -DBUILD_SHARED_LIBS=ON \
     -DENABLE_UTILS=ON -L \
    "

def setup():
	shelltools.system("./bootstrap")
	cmaketools.configure(j)

def build():
	cmaketools.make()

def install():
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
	for t in ["utils/nfs-cat", "utils/nfs-cp", "utils/nfs-ls"]:
		pisitools.dobin(t)

	pisitools.dodoc("COPYING", "README")

