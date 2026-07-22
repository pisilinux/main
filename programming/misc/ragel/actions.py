#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get, shelltools

def setup():
    autotools.autoreconf("-vif")

    autotools.configure("./configure \
                        --prefix=/usr \
                        --docdir=/usr/share/doc/ragel \
                        --bindir=/usr/bin \
                        --mandir=/usr/share/man \
                        --libdir=/usr/lib \
                        --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/vim/vimfiles/syntax/", "ragel.vim")

    pisitools.dodoc("COPYING")
