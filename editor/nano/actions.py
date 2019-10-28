#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fvi")
    autotools.configure("--disable-rpath \
                         --enable-utf8 \
                         --enable-altrcname \
                         --enable-color \
                         --enable-nanorc \
                         --enable-multibuffer \
                         --disable-speller")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/", "doc/sample.nanorc", "nanorc")
    pisitools.dosym("/usr/bin/nano", "/bin/nano")

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("ChangeLog*", "README", "doc/sample.nanorc", "AUTHORS", "NEWS", "TODO", "COPYING*", "THANKS")
