#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.cflags.add("-fPIC")
    #autotools.autoreconf("-fiv")
    autotools.configure("--enable-openssl \
                         --enable-nss")

def build():
    autotools.make("all")
    autotools.make("shared_library")
    

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "CHANGES", "README*")
