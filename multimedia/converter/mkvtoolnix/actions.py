#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

# Disable automagic curl dep used for online update checking
shelltools.export("CURL_CFLAGS", "")
shelltools.export("CURL_LIBS", "")

# Sets number of threads for a parallel build
shelltools.export("DRAKETHREADS", get.makeJOBS().replace("-j", ""))

pisitools.flags.add("-DBOOST_FILESYSTEM_VERSION=3")

def setup():
    #shelltools.system("rm -rf lib/{boost,fmt,jpcre2,libebml,libmatroska,nlohmann-json,pugixml,utf8-cpp}")
   # pisitools.dosed("configure.in", "curl", deleteLine=True)

    shelltools.system("./autogen.sh")
    autotools.autoreconf("-fiv")
    autotools.configure("--with-flac \
                         --enable-qt5 \
                         --disable-qt6 \
                         --disable-update-check \
                         --with-boost-libdir=/usr/lib ")

def build():
    shelltools.system("rake")

def install():
    shelltools.system('rake install DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("COPYING*", "README*")
