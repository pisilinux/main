#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-hashes=strong,glibc \
                         --enable-obsolete-api=no \
                         --disable-failure-tokens")

def build():
    autotools.make()

def install():
    autotools.install()
    # Fix conflicts with glibc
    pisitools.rename("/usr/lib/libcrypt.so", "libxcrypt.so")
    pisitools.rename("/usr/include/crypt.h", "xcrypt.h")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING.LIB")
