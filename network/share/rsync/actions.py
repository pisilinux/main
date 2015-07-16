#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="rsync-%s" % get.srcVERSION().replace('_','')

def setup():
    autotools.configure("--without-included-zlib \
                         --with-included-popt=no \
                         --disable-debug")

def build():
    autotools.make()

#def check():
#    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS","README","TODO")
