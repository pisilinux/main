#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    a = 'install_{bin,include,lib,doc_man}'
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), argument = '%s' % a)

    pisitools.dodoc("ChangeLog", "COPYING")
