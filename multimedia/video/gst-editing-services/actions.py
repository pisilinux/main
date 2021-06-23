#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("-D validate=disabled \
                          -D doc=disabled")

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
