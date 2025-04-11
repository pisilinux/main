#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

libversion = get.srcVERSION()


def setup():
    autotools.configure("--prefix=/usr --enable-shared --with-pkgconfigdir=/usr/lib/pkgconfig --libdir=/lib --bindir=/bin")

def build():
    autotools.make('all CC=%s AR=%s RANLIB=%s CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC"' % (get.CC(), get.AR(), get.RANLIB(), get.CFLAGS()))
    # autotools.make('CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC" -f Makefile-libbz2_so' % get.CFLAGS())

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())
    pisitools.remove("/lib/libbzip3.a")

    # No static libs
    # pisitools.removeDir("/usr/lib")
    # pisitools.domove("/usr/bin/", "/")

    # for link in ("/bin/bunzip2", "/bin/bzcat"):
        # pisitools.remove(link)
        # pisitools.dosym("bzip2", link)

    # for wrong_link in ("/bin/bzcmp", "/bin/bzegrep", "/bin/bzfgrep", "/bin/bzless"):
        # pisitools.remove(wrong_link)

    # pisitools.dosym("bzgrep", "/bin/bzegrep")
    # pisitools.dosym("bzgrep", "/bin/bzfgrep")
    # pisitools.dosym("bzdiff", "/bin/bzcmp")
    # pisitools.dosym("bzmore", "/bin/bzless")

    # pisitools.dolib("libbz3.o.%s" % libversion, "/lib")

    # pisitools.dosym("libbz2.so.1", "/lib/libbz2.so")
    # pisitools.dosym("libbz2.so.1", "/lib/libbz2.so.1.0")
    # pisitools.dosym("libbz2.so.%s" % libversion, "/lib/libbz2.so.1")

    # pisitools.dohtml("manual.html")
    pisitools.dodoc("README*", "NEWS", "LICENSE")
