#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# def setup():
    # autotools.configure()

def build():
    autotools.make('EXTRA_CFLAGS="%s" -j1' % get.CFLAGS())
    autotools.make("-C Documentation")

def install():
    autotools.rawInstall("libdir_relative=lib prefix=/usr DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C Documentation libdir_relative=lib prefix=/usr DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSES/*")
