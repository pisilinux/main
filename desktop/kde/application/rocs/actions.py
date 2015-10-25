#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

def setup():
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("COPYING.DOC",  "ChangeLog", "AUTHORS", "README", "COPYING.GPL2", "TESTING", "COPYING.LIB.LGPL-2", "COPYING.LIB.LGPL-2.1", "README.developer", "README.packager")
